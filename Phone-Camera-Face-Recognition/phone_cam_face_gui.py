import tkinter as tk
from tkinter import ttk, messagebox
import time
import cv2
from PIL import Image, ImageTk


class PhoneCamFaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Camera Điện thoại + Nhận dạng khuôn mặt")
        self.root.geometry("920x700")
        self.root.resizable(False, False)
        self.root.option_add("*Font", "Arial 10")

        style = ttk.Style()
        style.theme_use('clam')

        self.stream_url = tk.StringVar(value="http://192.168.1.100:8080/video")
        self.face_detection_enabled = tk.BooleanVar(value=True)

        self.video_capture = None
        self.current_frame = None
        self.running = False
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        self._build_ui()

    def _build_ui(self):
        top_frame = ttk.LabelFrame(self.root, text="Kết nối camera điện thoại", padding=10)
        top_frame.place(x=10, y=10, width=900, height=130)

        ttk.Label(top_frame, text="URL stream:").grid(row=0, column=0, sticky="w")
        self.url_entry = ttk.Entry(top_frame, textvariable=self.stream_url, width=80)
        self.url_entry.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=2)

        ttk.Button(top_frame, text="Kết nối", command=self.connect_stream).grid(row=1, column=1, pady=10, sticky="ew")
        ttk.Button(top_frame, text="Ngắt kết nối", command=self.disconnect_stream).grid(row=1, column=2, pady=10, sticky="ew")

        self.status_label = ttk.Label(top_frame, text="Trạng thái: Chưa kết nối", foreground="red")
        self.status_label.grid(row=1, column=3, padx=10, sticky="w")

        self.face_check = ttk.Checkbutton(
            top_frame,
            text="Bật nhận dạng khuôn mặt",
            variable=self.face_detection_enabled,
            onvalue=True,
            offvalue=False,
        )
        self.face_check.grid(row=2, column=1, columnspan=2, pady=2, sticky="w")

        ttk.Button(top_frame, text="Chụp ảnh", command=self.save_snapshot).grid(row=2, column=3, pady=2, sticky="e")

        info_label = ttk.Label(
            self.root,
            text="Lưu ý: Sử dụng ứng dụng camera IP trên điện thoại rồi nhập URL stream (ví dụ http://192.168.1.5:8080/video)",
            foreground="blue",
            wraplength=900,
            justify="left",
        )
        info_label.place(x=10, y=145)

        video_frame = ttk.LabelFrame(self.root, text="Video camera", padding=10)
        video_frame.place(x=10, y=175, width=900, height=455)

        self.video_label = ttk.Label(video_frame)
        self.video_label.place(x=0, y=0, width=880, height=430)

        log_frame = ttk.LabelFrame(self.root, text="Nhật ký hoạt động", padding=10)
        log_frame.place(x=10, y=640, width=900, height=90)

        self.log_box = tk.Text(log_frame, height=4, state="disabled", wrap="word", font=("Arial", 10))
        self.log_box.pack(fill="both", expand=True)

        self.add_log("Ứng dụng đã sẵn sàng. Nhập URL camera và nhấn Kết nối.")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def connect_stream(self):
        if self.running:
            messagebox.showinfo("Thông báo", "Đã đang kết nối")
            return

        url = self.stream_url.get().strip()
        if not url:
            messagebox.showwarning("Lỗi", "Vui lòng nhập URL stream camera điện thoại")
            return

        self.video_capture = cv2.VideoCapture(url)
        if not self.video_capture.isOpened():
            messagebox.showerror("Lỗi kết nối", "Không thể mở luồng video. Kiểm tra URL và đảm bảo điện thoại và máy tính cùng mạng WiFi.")
            if self.video_capture is not None:
                self.video_capture.release()
                self.video_capture = None
            return

        self.running = True
        self.status_label.config(text="Trạng thái: Đang kết nối", foreground="green")
        self.add_log(f"Kết nối tới {url}")
        self.root.after(10, self._video_loop)

    def disconnect_stream(self):
        if not self.running:
            return

        self.running = False
        if self.video_capture:
            self.video_capture.release()
            self.video_capture = None

        self.status_label.config(text="Trạng thái: Đã ngắt kết nối", foreground="orange")
        self.add_log("Đã ngắt kết nối stream")
        self.video_label.config(image='')
        self.video_label.imgtk = None

    def _video_loop(self):
        if not self.running or not self.video_capture:
            return

        try:
            ret, frame = self.video_capture.read()
            if not ret or frame is None:
                self.root.after(50, self._video_loop)
                return

            frame = cv2.resize(frame, (880, 430))
            if self.face_detection_enabled.get():
                frame = self._draw_face_boxes(frame)

            self.current_frame = frame.copy()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image_tk = ImageTk.PhotoImage(image=image)
            self.video_label.imgtk = image_tk
            self.video_label.config(image=image_tk)
        except Exception as e:
            self.add_log(f"Loi stream: {e}")
            self.disconnect_stream()
            return

        self.root.after(15, self._video_loop)

    def _draw_face_boxes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "Khuon mat",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

        cv2.putText(
            frame,
            f"So mat: {len(faces)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
            cv2.LINE_AA,
        )
        return frame

    def save_snapshot(self):
        if self.current_frame is None:
            messagebox.showwarning("Lỗi", "Không có hình ảnh để lưu")
            return

        now = time.strftime("%Y%m%d_%H%M%S")
        filename = f"phonecam_snapshot_{now}.png"

        try:
            cv2.imwrite(filename, self.current_frame)
            self.add_log(f"Đã lưu ảnh: {filename}")
            messagebox.showinfo("Lưu ảnh", f"Đã lưu ảnh: {filename}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu ảnh:\n{e}")

    def add_log(self, message):
        self.log_box.config(state="normal")
        timestamp = time.strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{timestamp}] {message}\n")
        self.log_box.see("end")
        self.log_box.config(state="disabled")

    def on_close(self):
        self.running = False
        if self.video_capture:
            self.video_capture.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneCamFaceApp(root)
    root.mainloop()
