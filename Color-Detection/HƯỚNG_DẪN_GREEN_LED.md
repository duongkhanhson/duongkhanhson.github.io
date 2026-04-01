# Hướng Dẫn: Phát Hiện Màu Xanh & Điều Khiển LED

## 📋 Phân Tích detect_green.py

**Chương trình làm gì:**
- Mở camera từ máy tính
- Chuyển ảnh sang HSV color space
- Phát hiện vùng màu **xanh lá** (HSV: 35-85)
- Tìm **contours** (đường viền) có diện tích > 500 pixels
- Vẽ **khung bao quanh** và **tâm** của vùng phát hiện
- Hiển thị **tọa độ (X, Y)** của tâm

**Dải màu xanh (HSV):**
```
Lower: H=35  S=50   V=50
Upper: H=85  S=255  V=255
```

---

## 🔧 Cập Nhật detect_green.py

Đã bổ sung:
✅ Kết nối Arduino qua serial
✅ Gửi lệnh `'1'` khi phát hiện xanh → **Bật LED**
✅ Gửi lệnh `'0'` khi không phát hiện → **Tắt LED**
✅ Hiển thị "LED ON" trên màn hình
✅ Tắt LED an toàn khi thoát chương trình

---

## 📝 Sơ Đồ Kết Nối LED

```
Arduino Pin 13 ──→ LED dương (Cathode dài)
Arduino GND ──→ LED âm (Cathode ngắn) ──→ 330Ω Resistor ──→ GND

Hoặc dùng LED module (3 chân):
- VCC → 5V
- GND → GND  
- IN → Pin 13
```

---

## 🚀 Các Bước Thực Hiện

### 1️⃣ Upload Code Arduino
```
1. Mở Arduino IDE
2. Tạo file mới, paste code từ green_led_control.ino
3. Chọn Board: Arduino Uno
4. Chọn COM port (ví dụ COM3)
5. Nhấn Upload (Ctrl+U)
6. Mở Serial Monitor (Ctrl+Shift+M) → Baud: 9600
   → Sẽ thấy "LED Control Ready!"
```

### 2️⃣ Xác định COM Port của Arduino
Trong Serial Monitor của Arduino IDE:
- Nếu thấy "LED Control Ready!" → Port đúng
- Ghi nhớ COM port (ví dụ: **COM3**)

### 3️⃣ Cập Nhật COM Port trong Python
Mở `detect_green.py`, tìm dòng:
```python
arduino = serial.Serial('COM3', 9600, timeout=1)
```
Thay `'COM3'` bằng COM port của bạn (ví dụ: `'COM5'`)

### 4️⃣ Chạy Chương Trình
```bash
python detect_green.py
```

### 5️⃣ Test
- Giơ vật **màu xanh** lên camera
- → LED sẽ **bật sáng** ✓
- Di vật đi / không có xanh
- → LED sẽ **tắt** ✓

---

## 📊 Luồng Hoạt Động

```
┌─────────┐
│ Camera  │
└────┬────┘
     │ Đọc frame
     ↓
┌──────────────────┐
│ HSV Conversion   │
└────┬─────────────┘
     │ Phát hiện xanh
     ↓
┌──────────────────┐
│ Find Contours    │
│ Area > 500?      │
└────┬─────────────┘
     │
    YES              NO
     │                │
     ↓                ↓
┌────────────┐  ┌────────────┐
│ green_     │  │ green_     │
│ detected   │  │ detected   │
│ = TRUE     │  │ = FALSE    │
└────┬───────┘  └────┬───────┘
     │                │
     ↓                ↓
┌─────────────────────────────┐
│ Arduino Serial:             │
│ Gửi '1' (ON)      Gửi '0'  │
│                             │
│ DigitalWrite(LED, HIGH) or  │
│ DigitalWrite(LED, LOW)      │
└─────────────────────────────┘
     │
     ↓
┌─────────────┐
│  LED: ON/OFF│
└─────────────┘
```

---

## 🔍 Cách Thay Đổi Dải Màu Xanh

Nếu muốn phát hiện màu khác, sửa trong `detect_green.py`:

```python
# Màu xanh lá (hiện tại)
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Nếu thay đổi:
# Đỏ:       lower=[0, 50, 50]    upper=[10, 255, 255]
# Vàng:     lower=[20, 50, 50]   upper=[35, 255, 255]
# Lam/Xanh: lower=[90, 50, 50]   upper=[130, 255, 255]
```

---

## 🐛 Khắc Phục Sự Cố

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-----------|----------|
| **"port does not exist"** | COM port sai | Kiểm tra lại COM port |
| **LED không bật** | Arduino không nhận lệnh | Kiểm tra kết nối USB |
| **Không phát hiện xanh** | Dải màu sai | Điều chỉnh HSV range |
| **Python timeout** | Chậm kết nối | Tăng timeout lên 2 |

---

## 💡 Mẹo Nâng Cao

1. **Hiệu chuỉnh dải màu xanh:**
   - Dùng `cv2.imshow("Mask", mask)` để xem
   - Thay đổi lower/upper cho đến khi chỉ có phần xanh

2. **Tăng độ nhạy:**
   ```python
   area > 500  # Giảm thành 300 để nhạy hơn
   ```

3. **Bộ lộc nhiễu:**
   ```python
   kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
   mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
   ```

---

**Hoàn tất! Bây giờ bạn có hệ thống phát hiện màu xanh + điều khiển LED! 🎉**
