# Hướng Dẫn: Chương Trình Nhận Dạng Mắt & Mặt

## 📋 Chức Năng

Chương trình `eye_detection.py` có khả năng:
- ✅ **Phát hiện mặt** từ camera real-time
- ✅ **Phát hiện mắt** trong khuôn mặt
- ✅ **Hiển thị tọa độ** của tâm mắt
- ✅ **Đếm số lượng** mặt và mắt
- ✅ **Lưu ảnh** kết quả
- ✅ **FPS hiển thị** chất lượng xử lý

## 🔧 Yêu Cầu

**Thư viện Python:**
- opencv-python (cv2) - có sẵn trong workspace của bạn
- numpy - có sẵn

**Phần cứng:**
- Webcam / Camera máy tính

## 🚀 Cách Chạy

```bash
python eye_detection.py
```

## 🎮 Kiểm Soát

| Phím | Chức Năng |
|------|-----------|
| `q` | Thoát chương trình |
| `s` | Chụp ảnh kết quả (lưu thành JPG) |

## 📊 Hiển Thị Trên Màn Hình

```
┌─────────────────────────────────────┐
│                                     │
│  Mắt: 2 | Mặt: 1                  │
│  Frame: 145                         │
│                                     │
│    [Khung xanh]  <- Mặt              │
│    [Khung đỏ]    <- Mắt              │
│    • Tâm mắt                        │
│    (X,Y) Tọa độ                    │
│                                     │
│  Press 'q' to exit | 's' to save  │
└─────────────────────────────────────┘
```

## 🎨 Màu Sắc

- **Xanh lá (Green)**: Khung mặt, nhãn "Face"
- **Đỏ (Red)**: Khung mắt
- **Xanh dương (Blue)**: Tâm mắt (tròn nhỏ)
- **Vàng (Yellow)**: Thông tin "Mắt & Mặt"

## 📈 Ví Dụ Output

```
════════════════════════════════════════
   CHƯƠNG TRÌNH NHẬN DẠNG MẮT & MẶT
════════════════════════════════════════
Nhấn 'q' để thoát
Nhấn 's' để chụp ảnh kết quả
════════════════════════════════════════

✓ Đã lưu ảnh: eye_detection_145.jpg
✓ Thoát chương trình

════════════════════════════════════════
Tổng frame xử lý: 234
════════════════════════════════════════
```

## 🔍 Cách Hoạt Động

### Bước 1: Đọc Frame từ Camera
```python
ret, frame = cap.read()
```

### Bước 2: Chuyển sang Grayscale
```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

### Bước 3: Phát Hiện Mặt (Haar Cascade)
```python
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

### Bước 4: Trong Mỗi Mặt, Phát Hiện Mắt
```python
roi_gray = gray[y:y+h, x:x+w]  # Vùng mặt
eyes = eye_cascade.detectMultiScale(roi_gray, ...)
```

### Bước 5: Vẽ Khung & Tôi Đó
```python
cv2.rectangle()  # Khung
cv2.circle()     # Tâm
cv2.putText()    # Tọa độ
```

## 💡 Tham Số Điều Chỉnh

### Độ Nhạy Phát Hiện
Trong code:
```python
# Phát hiện mặt
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1,      # Nhỏ = nhạy hơn (0.9-1.3)
    minNeighbors=5,       # Nhỏ = nhạy hơn (3-7)
    minSize=(30, 30)      # Kích thước tối thiểu
)

# Phát hiện mắt
eyes = eye_cascade.detectMultiScale(
    roi_gray,
    scaleFactor=1.05,     # Nhỏ hơn = chính xác hơn
    minNeighbors=5,       # Lớn = chặt chẽ hơn
    minSize=(15, 15)      # Kích thước tối thiểu mắt
)
```

**Mẹo:**
- `scaleFactor` nhỏ → nhạy hơn nhưng chậm hơn
- `minNeighbors` lớn → ít hơn false positive nhưng dễ miss

## 🖼️ Lưu Ảnh

Nhấn `s` trong chương trình:
- Ảnh sẽ lưu ở thư mục hiện tại
- Tên: `eye_detection_XXX.jpg` (XXX = frame số)
- Nội dung: Frame hiện tại + tất cả khung & tọa độ

## 🐛 Khắc Phục Sự Cố

| Vấn Đề | Nguyên Nhân | Giải Pháp |
|--------|-----------|----------|
| **Không phát hiện mắt** | Ánh sáng kém hoặc góc độ | Điều chỉnh `minNeighbors` nhỏ hơn |
| **Phát hiện sai** | Detector quá nhạy | Tăng `minNeighbors` lên 7-8 |
| **Chậm** | Xử lý nặng | Giảm độ phân giải camera |
| **Lỗi camera** | Webcam bị chiếm | Đóng chương trình khác |

## 📊 Luồng Xử Lý

```
Camera Input
    ↓
Read Frame (RGB)
    ↓
Convert to Grayscale
    ↓
Detect Faces (Haar Cascade)
    ├─→ For each Face:
    │       ├─→ Extract ROI (Region of Interest)
    │       ├─→ Detect Eyes (Haar Cascade)
    │       ├─→ For each Eye:
    │       │   ├─→ Draw Rectangle (Red)
    │       │   ├─→ Calculate Center Point
    │       │   └─→ Draw Circle at Center (Blue)
    │       └─→ Display Coordinates
    │
    ├─→ Draw Face Rectangle (Green)
    ├─→ Display Label "Face"
    └─→ Display Statistics
         ↓
Display Frame
    ↓
User Input (q or s)
    ↓
Exit or Save
```

## 🎯 Nâng Cao (Tùy Chọn)

### Thêm Dlib cho Nhận Dạng Chính Xác Hơn
```bash
pip install dlib
```

### Sử dụng MediaPipe (Mô Hình AI)
```bash
pip install mediapipe
```

---

**Chương trình sẵn sàng sử dụng! Chạy và thử ngay! 🎉**
