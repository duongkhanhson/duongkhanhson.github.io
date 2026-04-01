# ESP32 Camera Network & Face Tracking

![Microcontroller](https://img.shields.io/badge/Microcontroller-ESP32-red.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green.svg)

## 📌 Introduction
This project integrates an ESP32-CAM module with a Python client to perform real-time wireless Face Tracking and Recognition. The hardware streams HTTP/MJPEG video directly to a desktop GUI developed in Python, bypassing the need for physical wires while maintaining high inference speeds.

## ✨ Features
- **Wireless Streaming:** Extracts continuous frame data over the local network via ESP32 WiFi infrastructure.
- **Hardware Integration:** Communicates serial/HTTP commands to the microcontroller for IoT integrations.
- **Face Localization:** Utilizes OpenCV's pre-trained Cascade Classifiers to detect human faces from the raw MJPEG stream dynamically.
- **Client GUI:** A robust `tkinter` / `customtkinter` interface allowing start, stop, and snapshot functionalities.

## 👨‍💻 Author
**Đường Khánh Sơn** - *Giảng Viên CTUT. Ngành Cơ điện tử.*
