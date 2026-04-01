import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import threading
import time

class ServoControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Điều Khiển Servo SG90")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Thiết lập style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.serial_port = None
        self.is_connected = False
        self.current_angle = 90
        
        # ===== PHẦN KẾT NỐI =====
        connection_frame = ttk.LabelFrame(root, text="Kết Nối Arduino", padding=10)
        connection_frame.pack(padx=10, pady=10, fill="x")
        
        # Chọn COM Port
        ttk.Label(connection_frame, text="COM Port:").grid(row=0, column=0, sticky="w")
        self.port_combo = ttk.Combobox(connection_frame, width=20, state="readonly")
        self.port_combo.grid(row=0, column=1, padx=5)
        self.refresh_ports()
        
        # Nút làm mới danh sách port
        ttk.Button(connection_frame, text="Làm Mới", 
                  command=self.refresh_ports).grid(row=0, column=2, padx=5)
        
        # Chọn Baud Rate
        ttk.Label(connection_frame, text="Baud Rate:").grid(row=1, column=0, sticky="w", pady=5)
        self.baud_combo = ttk.Combobox(connection_frame, width=20, state="readonly",
                                       values=["9600", "115200", "38400", "19200"])
        self.baud_combo.set("9600")
        self.baud_combo.grid(row=1, column=1, padx=5)
        
        # Nút kết nối
        self.connect_btn = ttk.Button(connection_frame, text="Kết Nối",
                                      command=self.connect_port)
        self.connect_btn.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        # Trạng thái
        self.status_label = ttk.Label(connection_frame, text="Chưa kết nối",
                                      foreground="red", font=("Arial", 10, "bold"))
        self.status_label.grid(row=2, column=2, padx=5)
        
        # ===== PHẦN ĐIỀU KHIỂN =====
        control_frame = ttk.LabelFrame(root, text="Điều Khiển Góc Xoay", padding=10)
        control_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Slider điều khiển góc
        ttk.Label(control_frame, text="Góc xoay (0-180°):").pack(pady=5)
        
        self.angle_slider = ttk.Scale(control_frame, from_=0, to=180, orient="horizontal",
                                      command=self.on_slider_change)
        self.angle_slider.set(90)
        self.angle_slider.pack(fill="x", padx=10, pady=5)
        
        # Hiển thị góc hiện tại
        self.angle_display = ttk.Label(control_frame, text="Góc hiện tại: 90°",
                                       foreground="blue", font=("Arial", 14, "bold"))
        self.angle_display.pack(pady=10)
        
        # ===== NGOÀI CẢM NHANH =====
        quick_frame = ttk.LabelFrame(control_frame, text="Ngoài Cảm Nhanh", padding=10)
        quick_frame.pack(fill="x", padx=10, pady=10)
        
        button_frame = ttk.Frame(quick_frame)
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="MIN (0°)",
                  command=lambda: self.send_command("MIN")).pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(button_frame, text="Trung Tâm (90°)",
                  command=lambda: self.send_command("MID")).pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(button_frame, text="MAX (180°)",
                  command=lambda: self.send_command("MAX")).pack(side="left", padx=5, fill="x", expand=True)
        
        # ===== NHẬP LIỆU TRỰC TIẾP =====
        input_frame = ttk.LabelFrame(control_frame, text="Nhập Góc Trực Tiếp", padding=10)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        input_inner = ttk.Frame(input_frame)
        input_inner.pack(fill="x")
        
        ttk.Label(input_inner, text="Góc:").pack(side="left", padx=5)
        self.angle_input = ttk.Entry(input_inner, width=10)
        self.angle_input.pack(side="left", padx=5)
        self.angle_input.insert(0, "90")
        
        ttk.Button(input_inner, text="Gửi",
                  command=self.send_input_angle).pack(side="left", padx=5)
        
        # ===== LOG =====
        log_frame = ttk.LabelFrame(root, text="Log", padding=10)
        log_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Scrollbar cho log
        scrollbar = ttk.Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.log_text = tk.Text(log_frame, height=8, width=60, 
                               yscrollcommand=scrollbar.set, state="disabled")
        self.log_text.pack(fill="both", expand=True, side="left")
        scrollbar.config(command=self.log_text.yview)
        
        self.add_log("Ứng dụng điều khiển Servo SG90 đã sẵn sàng!")
        
    def refresh_ports(self):
        """Làm mới danh sách COM port"""
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_combo['values'] = ports if ports else ["No ports found"]
        if ports:
            self.port_combo.set(ports[0])
    
    def connect_port(self):
        """Kết nối với Arduino"""
        if self.is_connected:
            self.disconnect_port()
            return
        
        try:
            port = self.port_combo.get()
            baud = int(self.baud_combo.get())
            
            if port == "No ports found":
                messagebox.showerror("Lỗi", "Không tìm thấy COM port!")
                return
            
            self.serial_port = serial.Serial(port, baud, timeout=1)
            self.is_connected = True
            
            self.status_label.config(text=f"✓ Kết nối: {port}", foreground="green")
            self.connect_btn.config(text="Ngắt Kết Nối")
            self.add_log(f"Kết nối thành công tới {port} @ {baud} baud")
            
            # Bắt đầu thread đọc dữ liệu từ Arduino
            read_thread = threading.Thread(target=self.read_from_arduino, daemon=True)
            read_thread.start()
            
        except Exception as e:
            messagebox.showerror("Lỗi Kết Nối", f"Không thể kết nối: {str(e)}")
            self.is_connected = False
    
    def disconnect_port(self):
        """Ngắt kết nối với Arduino"""
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.is_connected = False
            self.status_label.config(text="✗ Chưa kết nối", foreground="red")
            self.connect_btn.config(text="Kết Nối")
            self.add_log("Đã ngắt kết nối")
    
    def read_from_arduino(self):
        """Đọc dữ liệu từ Arduino trong luồng riêng"""
        while self.is_connected:
            try:
                if self.serial_port and self.serial_port.in_waiting > 0:
                    message = self.serial_port.readline().decode('utf-8').strip()
                    if message:
                        self.add_log(f"Arduino: {message}")
            except Exception as e:
                self.add_log(f"Lỗi đọc: {str(e)}")
                break
            time.sleep(0.1)
    
    def on_slider_change(self, value):
        """Khi thay đổi slider"""
        angle = int(float(value))
        self.current_angle = angle
        self.angle_display.config(text=f"Góc hiện tại: {angle}°")
        self.angle_input.delete(0, "end")
        self.angle_input.insert(0, str(angle))
        
        # Gửi tự động
        if self.is_connected:
            self.send_command(str(angle))
    
    def send_input_angle(self):
        """Gửi góc từ input"""
        try:
            angle = int(self.angle_input.get())
            if 0 <= angle <= 180:
                self.angle_slider.set(angle)
                self.send_command(str(angle))
            else:
                messagebox.showwarning("Lỗi", "Góc phải từ 0-180!")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
    
    def send_command(self, command):
        """Gửi lệnh tới Arduino"""
        if not self.is_connected:
            messagebox.showwarning("Cảnh báo", "Chưa kết nối Arduino!")
            return
        
        try:
            self.serial_port.write((command + '\n').encode('utf-8'))
            self.add_log(f"Gửi: {command}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi lệnh: {str(e)}")
            self.is_connected = False
    
    def add_log(self, message):
        """Thêm message vào log"""
        self.log_text.config(state="normal")
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {message}\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ServoControlApp(root)
    root.mainloop()
