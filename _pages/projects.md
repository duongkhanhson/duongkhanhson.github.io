---
title: "Projects"
permalink: /projects/
layout: single
---

<!-- Vietnamese -->
<h2>Tiếng Việt</h2>
Chào mừng đến với danh mục các dự án nghiên cứu và phát triển phần mềm của tôi tại Trường Đại học Kỹ thuật - Công nghệ Cần Thơ.

<!-- English -->
Welcome to the Projects section, showcasing my research and software development work at Can Tho University of Technology - Engineering.

## 1. AI Hand Tracking & Finger Counting
**Technologies:** Python, OpenCV, MediaPipe, CustomTkinter

Vietnamese: Dự án này là một ứng dụng tự động nhận diện bàn tay và đếm số ngón tay trực tiếp qua hình ảnh từ Webcam. Ứng dụng trí tuệ nhân tạo thông qua công nghệ Computer Vision (OpenCV) và deep learning (MediaPipe) để phát hiện đến 2 bàn tay đồng thời.

English: This project is an automatic hand detection and finger counting application using webcam images. It leverages AI via Computer Vision (OpenCV) and deep learning (MediaPipe) to detect up to two hands simultaneously.

- **Algorithm:** Counts fingers by extracting 3D coordinates of 21 landmarks in real‑time.
- **Interface:** Modern Dark‑Mode UI built with CustomTkinter.
- **Use case:** Foundation for remote SCARA robot control via hand gestures.

📄 *Source code & installation:* [AI‑Hand‑Tracking](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/AI-Hand-Tracking)

---

## 2. Game Rắn Săn Mồi – Luyện Phép Nhân
**Technologies:** HTML5 Canvas, CSS3, Vanilla JavaScript

Vietnamese: Trò chơi tương tác trên trình duyệt, giúp học sinh tiểu học luyện tập các phép nhân cửu chương. Kết hợp cơ chế Snake cổ điển với việc giải toán nhanh.

English: An interactive browser game that helps primary school students practice multiplication tables. It combines classic Snake mechanics with quick math problem solving.

- **Reflex Training:** The snake eats "correct answers" among random options, improving focus and reaction.
- **No external libraries:** Fully built with vanilla JavaScript.
- **Play instantly:** No installation required.

🎮 *Live demo:* [Snake‑Math‑Game](https://duongkhanhson.github.io/Snake-Math-Game/)
📄 *Source code:* [Snake‑Math‑Game repo](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Snake-Math-Game)

---

## 3. ESP32 Camera Network & Face Tracking
**Technologies:** Python, OpenCV, ESP32‑CAM, Tkinter

Vietnamese: Tích hợp ESP32‑CAM và máy trạm Python để nhận diện và theo dõi khuôn mặt không dây qua TCP/IP.

English: Integrates ESP32‑CAM hardware with a Python workstation to perform wireless face detection and tracking over TCP/IP.

- **Real‑time streaming:** Capture frames and analyze locally.
- **IoT integration:** Can trigger external commands on microcontrollers.

📄 *Details:* [ESP32‑Cam‑Face‑Tracking](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/ESP32-Cam-Face-Tracking)

---

## 4. PID Motor Serial Control Interface
**Technologies:** Python, Arduino C++, Control Theory

Vietnamese: Giao diện tinh chỉnh thuật toán PID qua cổng Serial cho Motor DC có Encoder, hỗ trợ nghiên cứu và giảng dạy.

English: A serial interface for fine‑tuning PID control algorithms for encoder‑equipped DC motors, supporting research and teaching.

- **Real‑time plotting:** Displays setpoint and process value instantly.

📄 *Details:* [PID‑Motor‑Control](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/PID-Motor-Control)

---

## 5. Servo Motor Array Controller
**Technologies:** Python, Arduino, Robotics Actuators

Vietnamese: Hệ thống điều khiển ma trận servo đa bậc tự do, giao tiếp Master‑Slave cho cánh tay robot.

English: Multi‑DOF servo array controller with Master‑Slave communication for complex robotic arm manipulation.

📄 *Details:* [Servo‑Motor‑Control](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Servo-Motor-Control)

---

## 6. Eye & Face Activity Detection System
**Technologies:** Python, OpenCV AI, Cascade Classifiers

Vietnamese: Phần mềm xử lý vị trí mắt và khuôn mặt, nền tảng cho hệ thống cảnh báo ngủ gật tài xế.

English: Software that detects eye and face positions, serving as a foundation for driver fatigue detection systems.

📄 *Details:* [Eye‑Face‑Detection](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Eye-Face-Detection)

---

*(More robotics, automation, and mechatronics projects will be continuously added.)*

Chào mừng đến với danh mục các dự án nghiên cứu và phát triển phần mềm của tôi tại Trường Đại học Kỹ thuật - Công nghệ Cần Thơ.

## [1. AI Hand Tracking & Finger Counting](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/AI-Hand-Tracking)
**Technologies:** Python, OpenCV, MediaPipe, CustomTkinter

Dự án này là một ứng dụng tự động nhận diện bàn tay và đếm số ngón tay trực tiếp qua hình ảnh từ Webcam. Ứng dụng ứng dụng trí tuệ nhân tạo thông qua công nghệ Computer Vision (OpenCV) và deep learning (MediaPipe) để phát hiện đến 2 bàn tay đồng thời.

- **Cơ chế Thuật toán:** Xây dựng logic đếm ngón tay dựa trên việc trích xuất và tính toán ma trận tọa độ không gian 3D của 21 khớp (Landmarks) trên thời gian thực.
- **Giao diện hiện đại (HCI):** Được tinh chỉnh với framework `CustomTkinter` cho trải nghiệm Dark Mode mượt mà, điều khiển thân thiện.
- **Tính ứng dụng:** Là nền tảng cốt lõi được tác giả nghiên cứu phục vụ điều khiển tay máy SCARA (Robotics) từ xa bằng cử chỉ.

📄 *Chi tiết mã nguồn và hướng dẫn cài đặt có thể xem tại:* [Thư mục Source Code AI-Hand-Tracking](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/AI-Hand-Tracking)

---

## [2. Game Rắn Săn Mồi - Luyện Phép Nhân](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Snake-Math-Game)
**Technologies:** HTML5 Canvas, CSS3, Vanilla JavaScript

Dự án này là một trò chơi tương tác ngay trên trình duyệt web, được thiết kế nhằm giúp học sinh tiểu học luyện tập các phép toán cửu chương một cách vui nhộn. Trò chơi kết hợp cơ chế Snake cổ điển với việc giải toán nhanh.

- **Kích thích Tư duy Phản xạ:** Thay vì thức ăn thông thường, rắn phải đi tìm và ăn "kết quả đúng" của phép nhân hiển thị ngẫu nhiên trên màn hình trong số 4 lựa chọn thức ăn. Sự xuất hiện của các "đáp án nhiễu" giúp tăng khả năng tập trung và phản xạ nhạy bén.
- **Không có Thư viện Ngoại:** Toàn bộ engine Game Loop và vẽ đồ họa Canvas (Graphic Rendering) được phát triển bằng cấu trúc thuần Vanilla JavaScript. Không sử dụng thư viện bên thứ 3.
- **Trải nghiệm ngay trên Web:** Bạn có thể chơi ngay lập tức mà không cần cài đặt phần mềm nào.

🎮 *CHƠI THỬ TRUY CẬP NGAY:* **[Live Web Demo Game](https://duongkhanhson.github.io/Snake-Math-Game/)**  
📄 *Chi tiết mã nguồn có thể xem tại:* [Thư mục Source Code Snake-Math-Game](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Snake-Math-Game)

---

## [3. ESP32 Camera Network & Face Tracking](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/ESP32-Cam-Face-Tracking)
**Technologies:** Python, OpenCV, ESP32-CAM, Tkinter

Dự án tích hợp module phần cứng ESP32-CAM và máy trạm Python để thực hiện nhận diện và theo dõi khuôn mặt hoàn toàn không dây qua TCP/IP Streaming.

- **Truyền Hình Ảnh Real-time:** Thu thập dữ liệu khung ảnh (frames) và phân tích trực tiếp trên máy tính thông qua mạng cục bộ.
- **Tích hợp IoT:** Vừa hiển thị Live Feed vừa có thể kích hoạt các lệnh điều khiển ngoại vi gửi ngược về vi điều khiển.

📄 *Chi tiết: [Thư mục ESP32-Cam-Face-Tracking](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/ESP32-Cam-Face-Tracking)*

---

## [4. PID Motor Serial Control Interface](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/PID-Motor-Control)
**Technologies:** Python, Arduino C++, Control Theory

Xây dựng hệ thống giao diện tinh chỉnh thuật toán điều khiển tự động PID qua cổng Serial, dùng cho Motor DC có Encoder. Phục vụ mạnh mẽ cho nghiên cứu và giảng dạy chuyên ngành Cơ điện tử.

- **Đồ thị thời gian thực (Plotting):** Hiển thị Setpoint và Process Value, cập nhật hệ thống vòng kín cực nhanh mà không cần biên dịch lại Code nhúng liên tục.

📄 *Chi tiết: [Thư mục PID-Motor-Control](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/PID-Motor-Control)*

---

## [5. Servo Motor Array Controller](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Servo-Motor-Control)
**Technologies:** Python, Arduino, Robotics Actuators

Hệ thống điều khiển ma trận động cơ Servo đa bậc tự do (Multi-DOF). Giao tiếp chuẩn Master-Slave cho phép điều khiển cánh tay Robot phức tạp thông qua các thành phần giao diện trên máy tính (Trượt Slider độ).

📄 *Chi tiết: [Thư mục Servo-Motor-Control](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Servo-Motor-Control)*

---

## [6. Eye & Face Activity Detection System](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Eye-Face-Detection)
**Technologies:** Python, OpenCV AI, Cascade Classifiers

Phần mềm khai thác thị giác máy tính nhằm xử lý định vị tọa độ mắt và khuôn mặt người dùng. Khác với nhận diện tổng quát, hệ thống chia nhỏ thành phần để tối ưu framerate. Đây là nền tảng khởi đầu cho việc nghiên cứu hệ thống Cảnh báo ngủ gật cho tài xế (Fatigue Detection).

📄 *Chi tiết: [Thư mục Eye-Face-Detection](https://github.com/duongkhanhson/duongkhanhson.github.io/tree/master/Eye-Face-Detection)*

---

*(Các dự án khác về Robotics, Tự động hóa - Điều khiển và Cơ điện tử sẽ liên tục được cập nhật).*
