import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import urllib.request
import urllib.error
import cv2
from PIL import Image, ImageTk


class ESP32CamFaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESP32-CAM Face Control")
        self.root.geometry("920x760")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        self.stream_url = tk.StringVar(value="http://192.168.1.100:81/stream")
        self.command_url = tk.StringVar(value="http://192.168.1.100:81/control?cmd={cmd}")
        self.angle_value = tk.StringVar(value="90")
        self.face_detection_enabled = tk.BooleanVar(value=True)

        self.video_capture = None
        self.video_thread = None
        self.current_frame = None
        self.running = False
        self.video_width = 640
        self.video_height = 360
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        self._build_ui()

    def _build_ui(self):
        top_frame = ttk.LabelFrame(self.root, text="Kết nối ESP32-CAM", padding=10)
        top_frame.place(x=10, y=10, width=900, height=150)

        ttk.Label(top_frame, text="URL stream:").grid(row=0, column=0, sticky="w")
        self.url_entry = ttk.Entry(top_frame, textvariable=self.stream_url, width=80)
        self.url_entry.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=2)

        ttk.Button(top_frame, text="Kết nối", command=self.connect_stream).grid(row=1, column=1, pady=10, sticky="ew")
        ttk.Button(top_frame, text="Ngắt kết nối", command=self.disconnect_stream).grid(row=1, column=2, pady=10, sticky="ew")

        self.status_label = ttk.Label(top_frame, text="Trạng thái: Chưa kết nối", foreground="red")
        self.status_label.grid(row=1, column=3, padx=10, sticky="w")

        ttk.Checkbutton(
            top_frame,
            text="Bật nhận dạng khuôn mặt",
            variable=self.face_detection_enabled,
            onvalue=True,
            offvalue=False,
        ).grid(row=2, column=1, columnspan=2, pady=2, sticky="w")

        ttk.Button(top_frame, text="Chụp ảnh", command=self.save_snapshot).grid(row=2, column=3, pady=2, sticky="e")

        ttk.Label(top_frame, text="Lưu ý: Servo signal -> GPIO13, Vcc 5V, GND chung.").grid(row=3, column=0, columnspan=4, sticky="w", pady=2)
        ttk.Label(top_frame, text="Lệnh điều khiển: /control?cmd={cmd} hoặc /control?angle={angle}").grid(row=4, column=0, columnspan=4, sticky="w")

        control_frame = ttk.LabelFrame(self.root, text="Điều khiển ESP32", padding=10)
        control_frame.place(x=10, y=170, width=900, height=190)

        ttk.Label(control_frame, text="URL lệnh:").grid(row=0, column=0, sticky="w")
        self.command_entry = ttk.Entry(control_frame, textvariable=self.command_url, width=80)
        self.command_entry.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=2)

        ttk.Button(control_frame, text="TRÁI", command=lambda: self.send_command('LEFT')).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(control_frame, text="TRUNG TÂM", command=lambda: self.send_command('CENTER')).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(control_frame, text="PHẢI", command=lambda: self.send_command('RIGHT')).grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        ttk.Label(control_frame, text="Góc (0-180):").grid(row=2, column=0, sticky="w")
        self.angle_entry = ttk.Entry(control_frame, textvariable=self.angle_value, width=8)
        self.angle_entry.grid(row=2, column=1, sticky="w", padx=5)
        ttk.Button(control_frame, text="GỬI GÓC", command=self.send_angle_command).grid(row=2, column=2, padx=5, pady=5, sticky="ew")

        ttk.Label(control_frame, text="Dưới đây là các lệnh điều khiển servo:").grid(row=3, column=0, columnspan=4, sticky="w", pady=(5, 0))
        ttk.Label(control_frame, text="LEFT = 0°, CENTER = 90°, RIGHT = 180°, hoặc nhập số 0-180").grid(row=4, column=0, columnspan=4, sticky="w")

        self.command_log = tk.Text(control_frame, height=4, state="disabled", wrap="word")
        self.command_log.grid(row=5, column=0, columnspan=4, sticky="nsew", pady=5)
        control_frame.rowconfigure(5, weight=1)

        video_frame = ttk.LabelFrame(self.root, text="Video ESP32-CAM", padding=10)
        video_frame.place(x=10, y=370, width=900, height=380)

        self.video_label = ttk.Label(video_frame)
        self.video_label.place(x=10, y=10, width=self.video_width, height=self.video_height)

        self.add_log("Ứng dụng ESP32-CAM Face Control đã sẵn sàng.")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def connect_stream(self):
        if self.running:
            messagebox.showinfo("Thông báo", "Đã đang kết nối")
            return

        url = self.stream_url.get().strip()
        if not url:
            messagebox.showwarning("Lỗi", "Vui lòng nhập URL stream ESP32-CAM")
            return

        self.video_capture = cv2.VideoCapture(url)
        if not self.video_capture.isOpened():
            messagebox.showerror("Lỗi kết nối", "Không thể mở luồng video. Kiểm tra URL và ESP32-CAM.")
            self.video_capture.release()
            self.video_capture = None
            return

        self.running = True
        self.video_thread = threading.Thread(target=self._video_loop, daemon=True)
        self.video_thread.start()
        self.status_label.config(text="Trạng thái: Đang kết nối", foreground="green")
        self.add_log(f"Kết nối tới {url}")

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

    def _video_loop(self):
        while self.running and self.video_capture:
            try:
                ret, frame = self.video_capture.read()
                if not ret:
                    time.sleep(0.05)
                    continue

                frame = cv2.resize(frame, (self.video_width, self.video_height))

                if self.face_detection_enabled.get():
                    frame = self._draw_face_boxes(frame)

                self.current_frame = frame.copy()
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image_tk = ImageTk.PhotoImage(image=image)
                self.root.after(0, self._update_image, image_tk)

            except Exception as e:
                self.add_log(f"Lỗi stream: {e}")
                break

        self.disconnect_stream()

    def _draw_face_boxes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
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
            f"Khuon mat: {len(faces)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
            cv2.LINE_AA,
        )
        return frame

    def _update_image(self, image_tk):
        self.video_label.imgtk = image_tk
        self.video_label.config(image=image_tk)

    def save_snapshot(self):
        if self.current_frame is None:
            messagebox.showwarning("Lỗi", "Không có hình ảnh để lưu")
            return

        now = time.strftime("%Y%m%d_%H%M%S")
        filename = f"esp32_snapshot_{now}.png"

        try:
            cv2.imwrite(filename, self.current_frame)
            self.add_log(f"Đã lưu ảnh: {filename}")
            messagebox.showinfo("Lưu ảnh", f"Đã lưu ảnh: {filename}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu ảnh:\n{e}")

    def send_command(self, cmd):
        url_template = self.command_url.get().strip()
        if not url_template:
            messagebox.showwarning("Lỗi", "Vui lòng nhập URL lệnh ESP32")
            return

        angle = self.angle_value.get().strip()
        try:
            url = url_template.format(cmd=cmd, angle=angle)
        except Exception as e:
            messagebox.showerror("Lỗi URL", f"Định dạng URL lệnh không hợp lệ:\n{e}")
            return

        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                response_text = response.read().decode('utf-8', errors='ignore')
                self.add_log(f"Gửi lệnh '{cmd}' tới ESP32: {url}")
                self.add_log(f"Phản hồi: {response_text[:120]}")
        except urllib.error.URLError as e:
            messagebox.showerror("Lỗi lệnh", f"Không thể gửi lệnh:\n{e}")
            self.add_log(f"Lỗi lệnh: {e}")

    def send_angle_command(self):
        angle = self.angle_value.get().strip()
        if not angle.isdigit() or not (0 <= int(angle) <= 180):
            messagebox.showwarning("Lỗi", "Góc phải là số từ 0 đến 180")
            return
        self.send_command(angle)

    def add_log(self, message):
        self.command_log.config(state="normal")
        timestamp = time.strftime("%H:%M:%S")
        self.command_log.insert("end", f"[{timestamp}] {message}\n")
        self.command_log.see("end")
        self.command_log.config(state="disabled")

    def on_close(self):
        self.running = False
        if self.video_capture:
            self.video_capture.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ESP32CamFaceApp(root)
    root.mainloop()
