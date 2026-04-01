# Hướng Dẫn Điều Khiển Servo SG90 với Arduino

## 📋 Danh Sách Các File

1. **servo_control.ino** - Code Arduino để điều khiển servo
2. **servo_gui.py** - Ứng dụng GUI Python điều khiển servo từ máy tính

## ⚙️ Yêu Cầu Phần Cứng

- Arduino Uno (hoặc tương tự)
- Servo SG90
- Cáp USB để kết nối Arduino với máy tính
- Dây nối (jumper wires)
- Nguồn điện 5V cho servo (khuyến cáo dùng power supply riêng)

## 🔌 Sơ Đồ Kết Nối

```
Servo SG90 có 3 dây:
┌─────────────────────────────────────────┐
│ Servo Signal (Cam/Yellow)  → Arduino Pin 9 (PWM)
│ Servo Power (Đỏ)          → 5V
│ Servo Ground (Nâu/Đen)    → GND
└─────────────────────────────────────────┘

Arduino ← USB → Máy Tính
```

## 🚀 Hướng Dẫn Cài Đặt

### 1. Cài Đặt Arduino IDE
- Tải từ: https://www.arduino.cc/en/software
- Cài đặt bình thường

### 2. Upload Code Arduino
1. Mở Arduino IDE
2. Mở file `servo_control.ino`
3. Chọn Board: **Arduino Uno**
4. Chọn COM Port (máy tính sẽ tự nhận diện)
5. Nhấn **Upload** (mũi tên phải)
6. Chờ "Done uploading"

### 3. Kiểm Tra Cổng Serial
Mở Arduino IDE → Tools → Serial Monitor → Baud: 9600
- Bạn sẽ thấy "Servo Control Ready!"

### 4. Chạy Ứng Dụng Python
```bash
# Ngư trong folder chứa servo_gui.py
python servo_gui.py
```

**Yêu cầu thư viện Python:**
- tkinter (đã có sẵn trong Python)
- pyserial (cài bằng: `pip install pyserial`)

## 📱 Cách Sử Dụng Ứng Dụng

### Kết Nối
1. Cắm Arduino vào USB
2. Chọn COM port từ dropdown (ví dụ: COM3, COM4)
3. Chọn Baud Rate: **9600**
4. Nhấn **Kết Nối**
5. Trạng thái sẽ hiển thị "✓ Kết nối: COMx"

### Điều Khiển Servo
**Có 4 cách điều khiển:**

1. **Slider** - Kéo thanh slider để thay đổi góc (0-180°)
2. **Ngoài Cảm Nhanh** - Nhấn các nút:
   - MIN (0°) - Servo xoay sang trái
   - Trung Tâm (90°) - Servo ở vị trí giữa
   - MAX (180°) - Servo xoay sang phải
3. **Nhập Trực Tiếp** - Nhập số từ 0-180 vào ô input và nhấn Gửi
4. **Serial Monitor** - Gửi lệnh qua Serial Monitor của Arduino IDE

### Lệnh Serial
Nếu dùng Serial Monitor, có thể gửi:
- Số: `0`, `45`, `90`, `135`, `180`
- Text: `MIN`, `MID`, `CENTER`, `MAX`

## 🐛 Khắc Phục Sự Cố

### Arduino không xuất hiện trong danh sách COM
- Cài CH340 Driver hoặc CP2102 Driver (tùy chip trên Arduino clone)
- Tải từ: https://sparks.gogo.co.nz/ch340.html

### Python không tìm dùng pyserial
```bash
pip install pyserial
```

### Servo không hoạt động
- Kiểm tra kết nối dây
- Kiểm tra Baud Rate (phải là 9600)
- Thử upload lại code Arduino
- Kiểm tra nguồn điện servo

### Đọc "Invalid angle"
- Nhập giá trị từ 0-180
- Không có khoảng trắng

## 💡 Mẹo

1. **Nguồn điện riêng:** Servo SG90 nên dùng pin 5V riêng, không lấy từ Arduino để tránh sụt điện áp
2. **Bảo vệ servo:** Không cho góc > 180° hoặc < 0° để tránh hỏng servo
3. **Dây dẫn ngắn:** Dùng dây USB chất lượng tốt để tránh mất dữ liệu serial

## 📞 Thông Số Servo SG90

| Thông Số | Giá Trị |
|----------|--------|
| Điện áp | 4.8 - 6 V |
| Tốc độ | 0.12 sec/60° (4.8V) |
| Torque | 1.8 kg/cm (4.8V) |
| Góc xoay | 0 - 180° |

---

**Thành công! Bây giờ bạn có thể điều khiển servo SG90 từ máy tính! 🎉**
