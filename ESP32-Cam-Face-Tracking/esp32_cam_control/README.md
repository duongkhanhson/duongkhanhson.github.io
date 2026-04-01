# ESP32-CAM Stream + HTTP Control Firmware

Firmware này chạy trên ESP32-CAM AI Thinker và cung cấp:

- MJPEG stream tại `/stream`
- HTTP endpoint điều khiển servo tại `/control`
- Trang gốc `/` để kiểm tra kết nối

## Cài đặt

1. Mở Arduino IDE.
2. Cài ESP32 board (File > Preferences > Additional Boards Manager URLs: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`).
3. Chọn board `AI Thinker ESP32-CAM`.
4. Đặt `Upload Speed` 115200.

## Cấu hình

- Mở Arduino IDE và mở sketch trong thư mục `esp32_cam_control/esp32_cam_stream_control`.
- Đảm bảo `esp32_cam_stream_control.ino` và `camera_pins.h` nằm cùng thư mục.
- Thay `YOUR_SSID` và `YOUR_PASSWORD` bằng WiFi của bạn.
- Nếu cần, chỉnh `SERVO_PIN` theo chân servo trên bo mạch.

## Sử dụng

1. Upload sketch lên ESP32-CAM.
2. Mở Serial Monitor ở `115200`.
3. Khi ESP32-CAM đã kết nối WiFi, xem địa chỉ IP hiển thị.
4. Trên máy tính cùng mạng, mở `esp32_cam_face_gui.py`.
5. Điền URL stream:
   - `http://<IP>/stream`
6. Điền URL lệnh:
   - `http://<IP>/control?cmd={cmd}`
   - hoặc `http://<IP>/control?angle={angle}`

### Kết nối phần cứng

- Servo signal (màu vàng) → `GPIO 13`
- Servo Vcc (màu đỏ) → nguồn `5V`
- Servo GND (màu nâu/đen) → GND chung với ESP32-CAM
- ESP32-CAM Vcc → nguồn `5V`
- ESP32-CAM GND → nối chung với GND nguồn servo

> Nên dùng nguồn 5V riêng cho servo, nhưng GND phải chung với ESP32-CAM.

### Các nút điều khiển trên GUI

- `Kết nối`: mở luồng video.
- `Ngắt kết nối`: dừng luồng.
- `TRÁI`: gửi lệnh `LEFT` (servo về 0°).
- `TRUNG TÂM`: gửi lệnh `CENTER` (servo về 90°).
- `PHẢI`: gửi lệnh `RIGHT` (servo về 180°).
- `GỬI GÓC`: nhập số 0-180 và gửi góc trực tiếp.

### Ví dụ lệnh HTTP

- `http://<IP>/control?cmd=LEFT`
- `http://<IP>/control?cmd=RIGHT`
- `http://<IP>/control?cmd=CENTER`
- `http://<IP>/control?cmd=120`
- `http://<IP>/control?angle=120`

## Ghi chú

- ESP32-CAM nên dùng nguồn 5V ổn định.
- Nếu không dùng servo, bạn có thể bỏ phần PWM.
- Module AI Thinker sử dụng `camera_pins.h` trong cùng thư mục.
