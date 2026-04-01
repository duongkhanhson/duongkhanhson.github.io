import tkinter as tk
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import os
import sys
import urllib.request
import numpy as np

# Thêm hàm tìm đường dẫn thực tế khi chạy file EXE
def resource_path(relative_path):
    """ Lấy đường dẫn tuyệt đối đến tài nguyên, hoạt động cho cả môi trường dev và PyInstaller """
    try:
        # PyInstaller tạo một thư mục tạm và lưu đường dẫn trong _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Cấu hình giao diện
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Đường dẫn file model
MODEL_FILENAME = "hand_landmarker.task"
MODEL_PATH = resource_path(MODEL_FILENAME)
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print(f"Đang tải file model: {MODEL_FILENAME}... Vui lòng đợi.")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Tải xong!")

# Thử import mediapipe kiểu mới
try:
    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision
    MEDIAPIPE_AVAILABLE = True
except ImportError:
    MEDIAPIPE_AVAILABLE = False

class WebcamApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Webcam Hand Analysis - Antigravity")
        self.geometry("850x850")

        self.detector = None
        if MEDIAPIPE_AVAILABLE:
            try:
                download_model()
                base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
                options = vision.HandLandmarkerOptions(
                    base_options=base_options,
                    num_hands=2,
                    min_hand_detection_confidence=0.5,
                    min_hand_presence_confidence=0.5,
                    min_tracking_confidence=0.5
                )
                self.detector = vision.HandLandmarker.create_from_options(options)
            except Exception as e:
                print(f"Lỗi khởi tạo detector: {e}")

        # Biến trạng thái
        self.cap = None
        self.is_running = False
        self.hand_detection_enabled = tk.BooleanVar(value=True if self.detector else False)

        # Giao diện
        self.setup_ui()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Tiêu đề
        self.label_title = ctk.CTkLabel(self, text="AI HAND ANALYSIS SYSTEM", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.grid(row=0, column=0, pady=20)

        # Khung hiển thị Video
        self.video_frame = ctk.CTkFrame(self, width=640, height=480, corner_radius=15, border_width=2, border_color="#3b3b3b")
        self.video_frame.grid(row=1, column=0, padx=20, pady=10)
        self.video_frame.grid_propagate(False)

        self.video_label = tk.Label(self.video_frame, bg="#1a1a1a")
        self.video_label.pack(expand=True, fill="both")

        # Công tắc bật tắt nhận diện
        self.switch_hand = ctk.CTkSwitch(self, text="Kích hoạt AI Vision", variable=self.hand_detection_enabled, 
                                          progress_color="#28a745")
        self.switch_hand.grid(row=2, column=0, pady=10)
        
        # Nút điều khiển
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=3, column=0, pady=20)

        self.btn_open = ctk.CTkButton(self.button_frame, text="MỞ CAMERA", command=self.start_webcam,
                                       width=180, height=50, font=ctk.CTkFont(size=14, weight="bold"),
                                       fg_color="#28a745", hover_color="#218838")
        self.btn_open.grid(row=0, column=0, padx=20)

        self.btn_close = ctk.CTkButton(self.button_frame, text="TẮT CAMERA", command=self.stop_webcam,
                                        width=180, height=50, font=ctk.CTkFont(size=14, weight="bold"),
                                        fg_color="#dc3545", hover_color="#c82333")
        self.btn_close.grid(row=0, column=1, padx=20)
        self.btn_close.configure(state="disabled")

        self.status_label = ctk.CTkLabel(self, text="Trạng thái: Sẵn sàng", font=ctk.CTkFont(size=13))
        self.status_label.grid(row=4, column=0, pady=10)

    def count_fingers(self, hand_landmarks, handedness):
        """Logic đếm ngón tay: 1 là giơ, 0 là gập"""
        fingers = []
        
        # Ngón cái: Kiểm tra theo trục X (ngang)
        # Vì ảnh đã lật gương (flip), ta cần chú ý logic trái/phải
        is_right = handedness[0].category_name == "Right"
        
        # Ngón cái (Thumb tip: 4, Thumb IP: 3)
        if is_right:
            fingers.append(1 if hand_landmarks[4].x < hand_landmarks[3].x else 0)
        else:
            fingers.append(1 if hand_landmarks[4].x > hand_landmarks[3].x else 0)

        # 4 ngón còn lại: So sánh trục Y (dọc)
        # Tip IDs: Trỏ(8), Giữa(12), Nhẫn(16), Út(20)
        for tip_id in [8, 12, 16, 20]:
            if hand_landmarks[tip_id].y < hand_landmarks[tip_id - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
                
        return fingers

    def start_webcam(self):
        if not self.is_running:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.status_label.configure(text="Lỗi: Không tìm thấy Camera", text_color="#dc3545")
                return
            self.is_running = True
            self.btn_open.configure(state="disabled")
            self.btn_close.configure(state="normal")
            self.status_label.configure(text="AI đang xử lý hình ảnh...", text_color="#28a745")
            self.update_video()

    def update_video(self):
        if self.is_running and self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (640, 480))
                frame = cv2.flip(frame, 1)
                
                total_fingers = 0
                if self.hand_detection_enabled.get() and self.detector:
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                    results = self.detector.detect(mp_image)
                    
                    if results.hand_landmarks:
                        for i, hand_landmarks in enumerate(results.hand_landmarks):
                            # Vẽ xương tay màu trắng
                            for start, end in [(0,1),(1,2),(2,3),(3,4),(0,5),(5,6),(6,7),(7,8),(0,9),(9,10),(10,11),(11,12),(0,13),(13,14),(14,15),(15,16),(0,17),(17,18),(18,19),(19,20),(5,9),(9,13),(13,17)]:
                                p1 = (int(hand_landmarks[start].x*640), int(hand_landmarks[start].y*480))
                                p2 = (int(hand_landmarks[end].x*640), int(hand_landmarks[end].y*480))
                                cv2.line(frame, p1, p2, (255, 255, 255), 1)

                            # Tính toán ngón tay
                            fingers = self.count_fingers(hand_landmarks, results.handedness[i])
                            total_fingers += fingers.count(1)
                            
                            # Vẽ các điểm khớp (Xanh dương cho ngón gập, Xanh lá cho ngón giơ)
                            tip_ids = [4, 8, 12, 16, 20]
                            for idx, tip_id in enumerate(tip_ids):
                                color = (0, 255, 0) if fingers[idx] == 1 else (0, 0, 255)
                                center = (int(hand_landmarks[tip_id].x*640), int(hand_landmarks[tip_id].y*480))
                                cv2.circle(frame, center, 8, color, -1)

                # HIỂN THỊ KẾT QUẢ ĐẾM (To và Rõ)
                cv2.rectangle(frame, (0, 0), (250, 80), (0, 0, 0), -1)
                cv2.putText(frame, f"FINGERS: {total_fingers}", (20, 55), 
                            cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)

                # Convert to Tkinter
                frame_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_display)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            
            self.after(20, self.update_video)

    def stop_webcam(self):
        if self.is_running:
            self.is_running = False
            if self.cap: self.cap.release()
            self.video_label.configure(image="")
            self.btn_open.configure(state="normal")
            self.btn_close.configure(state="disabled")
            self.status_label.configure(text="Đã dừng Camera", text_color="white")

    def on_closing(self):
        self.stop_webcam()
        self.destroy()

if __name__ == "__main__":
    app = WebcamApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
