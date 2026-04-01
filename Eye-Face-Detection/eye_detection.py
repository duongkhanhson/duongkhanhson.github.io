import cv2
import numpy as np

# Load Haar Cascade classifiers (có sẵn trong OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Mở camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Thiết lập độ phân giải camera (tùy chọn)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

print("════════════════════════════════════════")
print("   CHƯƠNG TRÌNH NHẬN DẠNG MẮT & MẶT")
print("════════════════════════════════════════")
print("Nhấn 'q' để thoát")
print("Nhấn 's' để chụp ảnh kết quả")
print("════════════════════════════════════════\n")

frame_count = 0
face_count = 0
eyes_total = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("✗ Lỗi: Không thể đọc frame từ camera!")
        break
    
    frame_count += 1
    
    # Chuyển sang grayscale để phát hiện tốt hơn
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Phát hiện mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        face_count = len(faces)
        eyes_total = 0
    
    # Vẽ khung và phát hiện mắt cho từng mặt
    for (x, y, w, h) in faces:
        # Vẽ khung mặt (xanh)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Nhãn "FACE"
        cv2.putText(frame, "Face", (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Vùng ROI (Region Of Interest) của mặt
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Phát hiện mắt trong vùng mặt
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=5, minSize=(15, 15))
        
        eyes_total = len(eyes)
        
        # Vẽ khung và tâm cho từng mắt (đỏ)
        for (ex, ey, ew, eh) in eyes:
            # Tọa độ tuyệt đối
            eye_x = x + ex
            eye_y = y + ey
            
            # Vẽ khung mắt
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
            
            # Tính tâm mắt
            eye_center_x = eye_x + ew // 2
            eye_center_y = eye_y + eh // 2
            
            # Vẽ tâm mắt (tròn nhỏ)
            cv2.circle(frame, (eye_center_x, eye_center_y), 4, (255, 0, 0), -1)
            
            # Hiển thị tọa độ tâm mắt
            cv2.putText(frame, f"({eye_center_x},{eye_center_y})", 
                       (eye_center_x + 10, eye_center_y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
    
    # Hiển thị thông tin trên màn hình
    info_text = f"Mặt: {face_count} | Mắt: {eyes_total}"
    cv2.putText(frame, info_text, (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    
    # Hiển thị frame count
    cv2.putText(frame, f"Frame: {frame_count}", (10, 70), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
    
    # Hiển thị hướng dẫn
    cv2.putText(frame, "Press 'q' to exit | 's' to save", (10, frame.shape[0] - 20),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
    
    # Hiển thị kết quả
    cv2.imshow("Eye & Face Detection", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        print("\n✓ Thoát chương trình")
        break
    elif key == ord('s'):
        # Lưu ảnh kết quả
        filename = f"eye_detection_{frame_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"✓ Đã lưu ảnh: {filename}")

# Thống kê
print("\n════════════════════════════════════════")
print(f"Tổng frame xử lý: {frame_count}")
print("════════════════════════════════════════")

cap.release()
cv2.destroyAllWindows()
