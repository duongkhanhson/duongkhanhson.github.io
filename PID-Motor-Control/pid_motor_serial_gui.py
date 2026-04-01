import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import threading
import time


class PIDMotorSerialGUI:
    HOME_ANGLE = 0
    AUTO_SEND_DELAY_MS = 150

    def __init__(self, root):
        self.root = root
        self.root.title("Điều Khiển Động Cơ PID qua Serial")
        self.root.geometry("560x620")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        self.serial_port = None
        self.is_connected = False
        self.send_after_id = None
        self.last_sent_angle = None

        self._build_connection_panel()
        self._build_control_panel()
        self._build_log_panel()

        self.add_log("Ứng dụng điều khiển động cơ PID qua Serial đã sẵn sàng.")
        self.refresh_ports()

    def _build_connection_panel(self):
        connection_frame = ttk.LabelFrame(self.root, text="Kết Nối Arduino", padding=12)
        connection_frame.pack(fill="x", padx=12, pady=10)

        ttk.Label(connection_frame, text="COM Port:").grid(row=0, column=0, sticky="w")
        self.port_combo = ttk.Combobox(connection_frame, width=20, state="readonly")
        self.port_combo.grid(row=0, column=1, padx=6, pady=4)

        refresh_btn = ttk.Button(connection_frame, text="Làm Mới", command=self.refresh_ports)
        refresh_btn.grid(row=0, column=2, padx=6, pady=4)

        ttk.Label(connection_frame, text="Baud Rate:").grid(row=1, column=0, sticky="w")
        self.baud_combo = ttk.Combobox(connection_frame, width=20, state="readonly",
                                       values=["115200", "9600", "38400", "19200"])
        self.baud_combo.set("115200")
        self.baud_combo.grid(row=1, column=1, padx=6, pady=4)

        self.connect_btn = ttk.Button(connection_frame, text="Kết Nối", command=self.toggle_connection)
        self.connect_btn.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew", padx=6)

        self.status_label = ttk.Label(connection_frame, text="Chưa kết nối", foreground="red",
                                      font=("Arial", 10, "bold"))
        self.status_label.grid(row=2, column=2, padx=6)

    def _build_control_panel(self):
        control_frame = ttk.LabelFrame(self.root, text="Điều Khiển Góc", padding=12)
        control_frame.pack(fill="both", expand=True, padx=12, pady=10)

        ttk.Label(control_frame, text="Góc điều khiển (-180 đến 360°):").pack(anchor="w")
        self.angle_slider = ttk.Scale(control_frame, from_=-180, to=360, orient="horizontal",
                                      command=self.on_slider_change)
        self.angle_slider.set(self.HOME_ANGLE)
        self.angle_slider.pack(fill="x", pady=8)

        self.current_angle_label = ttk.Label(control_frame, text=f"Góc chọn: {self.HOME_ANGLE}°",
                                             font=("Arial", 12, "bold"))
        self.current_angle_label.pack(pady=4)

        self.status_info_label = ttk.Label(control_frame, text="Target: 0° | Current: 0°",
                                           font=("Arial", 10))
        self.status_info_label.pack(pady=4)

        button_frame = ttk.Frame(control_frame)
        button_frame.pack(fill="x", pady=10)

        ttk.Button(button_frame, text="Home", command=self.send_home).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(button_frame, text="Gửi góc slider", command=self.send_slider_angle).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(button_frame, text="Nhận góc PC", command=self.send_input_angle).pack(side="left", expand=True, fill="x", padx=4)

        input_frame = ttk.LabelFrame(control_frame, text="Góc từ máy tính", padding=10)
        input_frame.pack(fill="x", pady=10)

        angle_label = ttk.Label(input_frame, text="Góc: ")
        angle_label.grid(row=0, column=0, sticky="w")

        self.angle_entry = ttk.Entry(input_frame, width=10)
        self.angle_entry.grid(row=0, column=1, padx=6)
        self.angle_entry.insert(0, str(self.HOME_ANGLE))

        ttk.Button(input_frame, text="Gửi", command=self.send_input_angle).grid(row=0, column=2, padx=6)

        command_frame = ttk.LabelFrame(control_frame, text="Lệnh nhanh", padding=10)
        command_frame.pack(fill="x", pady=10)

        ttk.Button(command_frame, text="Về Home", command=self.send_home).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(command_frame, text="Góc 0°", command=lambda: self.send_command("0")).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(command_frame, text="Góc 180°", command=lambda: self.send_command("180")).pack(side="left", expand=True, fill="x", padx=4)

        feedback_frame = ttk.LabelFrame(control_frame, text="Phản hồi từ Arduino", padding=10)
        feedback_frame.pack(fill="x", pady=10)

        self.feedback_label = ttk.Label(feedback_frame, text="Chưa nhận dữ liệu", font=("Arial", 11))
        self.feedback_label.pack(anchor="w")

    def _build_log_panel(self):
        log_frame = ttk.LabelFrame(self.root, text="Log", padding=10)
        log_frame.pack(fill="both", expand=True, padx=12, pady=10)

        self.log_text = tk.Text(log_frame, height=10, state="disabled", wrap="word")
        self.log_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=scrollbar.set)

    def refresh_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_combo['values'] = ports if ports else ["Không tìm thấy port"]
        if ports:
            self.port_combo.set(ports[0])
        else:
            self.port_combo.set("Không tìm thấy port")
            self.add_log("Không tìm thấy COM port.")

    def toggle_connection(self):
        if self.is_connected:
            self.disconnect_port()
        else:
            self.connect_port()

    def connect_port(self):
        port = self.port_combo.get()
        if not port or port == "Không tìm thấy port":
            messagebox.showerror("Lỗi", "Vui lòng chọn COM port hợp lệ.")
            return

        try:
            baud = int(self.baud_combo.get())
            self.serial_port = serial.Serial(port, baud, timeout=1)
            time.sleep(1)
            self.is_connected = True
            self.connect_btn.config(text="Ngắt Kết Nối")
            self.status_label.config(text=f"✓ Kết nối: {port}", foreground="green")
            self.add_log(f"Kết nối thành công: {port} @ {baud} baud.")
            threading.Thread(target=self.read_from_arduino, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Lỗi kết nối", f"Không thể mở cổng: {e}")
            self.add_log(f"Lỗi khi kết nối: {e}")
            self.is_connected = False

    def disconnect_port(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        self.is_connected = False
        self.connect_btn.config(text="Kết Nối")
        self.status_label.config(text="✗ Chưa kết nối", foreground="red")
        self.add_log("Đã ngắt kết nối." )

    def read_from_arduino(self):
        while self.is_connected and self.serial_port and self.serial_port.is_open:
            try:
                if self.serial_port.in_waiting > 0:
                    raw = self.serial_port.readline().decode('utf-8', errors='ignore').strip()
                    if raw:
                        self.add_log(f"Nhận: {raw}")
                        self._process_arduino_message(raw)
            except Exception as e:
                self.add_log(f"Lỗi đọc serial: {e}")
                break
            time.sleep(0.05)

    def _process_arduino_message(self, message):
        if message.startswith("Target_Pulses:") and ",Current_Pulses:" in message:
            try:
                parts = message.split(",")
                values = {}
                for part in parts:
                    if ':' in part:
                        key, val = part.split(':', 1)
                        values[key.strip()] = float(val)
                target_deg = values.get('Target_Pulses', 0.0) / 8418.0 * 360.0
                current_deg = values.get('Current_Pulses', 0.0) / 8418.0 * 360.0
                self.status_info_label.config(text=f"Target: {target_deg:.1f}° | Current: {current_deg:.1f}°")
                return
            except Exception:
                pass

        if message.startswith("Target:") and message.endswith("deg"):
            try:
                angle = float(message.replace("Target:", "").replace("deg", "").strip())
                self.status_info_label.config(text=f"Target: {angle:.1f}° | Current: --°")
                return
            except Exception:
                pass

        self.feedback_label.config(text=f"Arduino: {message}")

    def on_slider_change(self, value):
        angle = int(float(value))
        self.current_angle_label.config(text=f"Góc chọn: {angle}°")
        self.angle_entry.delete(0, tk.END)
        self.angle_entry.insert(0, str(angle))

        if self.is_connected:
            if self.send_after_id:
                self.root.after_cancel(self.send_after_id)
            self.send_after_id = self.root.after(self.AUTO_SEND_DELAY_MS, lambda: self.send_command(str(angle)))

    def send_slider_angle(self):
        angle = int(float(self.angle_slider.get()))
        self.send_command(str(angle))

    def send_input_angle(self):
        text = self.angle_entry.get().strip()
        try:
            angle = float(text)
            self.angle_slider.set(angle)
            self.send_command(str(angle))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

    def send_home(self):
        self.angle_slider.set(self.HOME_ANGLE)
        self.angle_entry.delete(0, tk.END)
        self.angle_entry.insert(0, str(self.HOME_ANGLE))
        self.send_command(str(self.HOME_ANGLE))

    def send_command(self, command):
        if not self.is_connected or not self.serial_port or not self.serial_port.is_open:
            messagebox.showwarning("Cảnh báo", "Arduino chưa được kết nối.")
            return

        try:
            self.serial_port.write((command + '\n').encode('utf-8'))
            self.add_log(f"Gửi: {command}")
            self.last_sent_angle = command
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi lệnh: {e}")
            self.add_log(f"Lỗi gửi lệnh: {e}")
            self.is_connected = False
            self.disconnect_port()

    def add_log(self, message):
        self.log_text.config(state="normal")
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {message}\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")


if __name__ == '__main__':
    root = tk.Tk()
    app = PIDMotorSerialGUI(root)
    root.mainloop()
