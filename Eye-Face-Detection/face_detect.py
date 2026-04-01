import cv2

# 1. Tải bộ phân loại khuôn mặt đã được huấn luyện sẵn của OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Khởi tạo Camera
cap = cv2.VideoCapture(0)

print("Đang khởi động bộ nhận diện... Nhấn 'q' để thoát.")

while True:
    # Đọc khung hình
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Chuyển sang ảnh xám (Haar Cascade hoạt động tốt nhất trên ảnh xám)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. Phát hiện khuôn mặt
    # scaleFactor: Độ thu nhỏ hình ảnh để tìm khuôn mặt (1.1 là 10%)
    # minNeighbors: Số lượng các hình chữ nhật lân cận để xác nhận là khuôn mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # 5. Vẽ hình chữ nhật quanh khuôn mặt phát hiện được
    for (x, y, w, h) in faces:
        # Vẽ khung màu xanh lá (BGR: 0, 255, 0), độ dày nét vẽ là 2
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Thêm dòng chữ "Face" phía trên khung
        cv2.putText(frame, 'Khuon mat', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Hiển thị kết quả
    cv2.imshow('Nhan dang khuon mat', frame)

    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()