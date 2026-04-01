import cv2
import numpy as np
import serial
import serial.tools.list_ports
import time

# Kiểm tra COM port có sẵn không
available_ports = [port.device for port in serial.tools.list_ports.comports()]
print(f"COM ports có sẵn: {available_ports}")

# Kết nối Arduino
arduino = None
try:
    if 'COM4' in available_ports:
        arduino = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)  # Chờ Arduino khởi động
        print("✓ Kết nối Arduino COM4 thành công!")
    else:
        print(f"✗ COM4 không tìm thấy! Các port khả dụng: {available_ports}")
except PermissionError:
    print("✗ Lỗi: COM4 đang bị khóa!")
    print("  → Đóng Arduino IDE Serial Monitor")
    print("  → Hoặc đóng chương trình khác đang dùng COM4")
    arduino = None
except Exception as e:
    print(f"✗ Lỗi kết nối Arduino: {e}")
    arduino = None

# mở camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

last_led_state = None  # Biến lưu trạng thái LED trước (để không gửi liên tục)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # dải màu xanh
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    green_detected = False  # Biến theo dõi phát hiện xanh

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:
            green_detected = True  # Phát hiện måu xanh

            x, y, w, h = cv2.boundingRect(cnt)

            # tính tọa độ tâm
            cx = int(x + w/2)
            cy = int(y + h/2)

            # vẽ khung
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            # vẽ tâm
            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

            # hiển thị tọa độ
            text = f"X:{cx} Y:{cy}"
            cv2.putText(frame,text,(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,(0,255,0),2)

    # Điều khiển LED dựa vào phát hiện
    if arduino:
        current_state = 1 if green_detected else 0
        
        # Chỉ gửi lệnh khi trạng thái thay đổi
        if current_state != last_led_state:
            if green_detected:
                arduino.write(b'1\n')  # Bật LED
                print("✓ Phát hiện xanh → LED BẬT")
                cv2.putText(frame,"[LED ON]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                arduino.write(b'0\n')  # Tắt LED
                print("✗ Không phát hiện → LED TẮT")
            
            last_led_state = current_state
            time.sleep(0.2)  # Chờ 200ms để Arduino xử lý

    cv2.imshow("Camera", frame)
    cv2.imshow("Green Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if arduino:
    arduino.write(b'0\n')  # Tắt LED trước khi thoát
    arduino.close()

cap.release()
cv2.destroyAllWindows()