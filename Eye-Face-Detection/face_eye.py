import cv2

# 1. Tải bộ phân loại cho cả Khuôn mặt và Đôi mắt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 2. Khởi tạo Camera
cap = cv2.VideoCapture(0)

print("Đang nhận diện Khuôn mặt & Đôi mắt... Nhấn 'q' để thoát.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Phát hiện khuôn mặt trước
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Vẽ khung khuôn mặt (Màu xanh lá)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # 4. Xác định vùng khuôn mặt trong ảnh xám và ảnh màu để tìm mắt
        # Chúng ta chỉ tìm mắt TRONG phạm vi khuôn mặt đã tìm thấy
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # 5. Phát hiện đôi mắt trong vùng khuôn mặt (Region of Interest - ROI)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            # Vẽ khung đôi mắt (Màu xanh dương: 255, 0, 0)
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    # Hiển thị kết quả
    cv2.imshow('Nhan dang Khuon mat & Doi mat', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()