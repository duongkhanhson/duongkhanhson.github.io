# AI Hand Tracking & Finger Counting

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.x-orange.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Modern_UI-brightgreen.svg)

## 📌 Introduction
This is an automated **AI-powered Hand Tracking and Finger Counting** application built using Python. The application utilizes computer vision (OpenCV) and deep learning models (MediaPipe) to accurately detect hand landmarks, analyze gesture poses in real-time, and precisely count the number of fingers raised. All logic is integrated within a modern, user-friendly Dark Theme GUI crafted with CustomTkinter.

This project was developed for research and educational purposes to demonstrate the practical application of AI in automated tracking and HCI (Human-Computer Interaction).

## ✨ Features
- **Real-time AI Vision:** Detects up to 2 hands concurrently with high confidence thresholds.
- **Precise Finger Counting Logic:** Distinguishes between folded and raised fingers accurately based on the spatial relationships of phalangeal joints.
- **Modern User Interface:** Built with `customtkinter`, featuring smooth animations, "Dark Mode," status indicators, and one-click controls.
- **Hardware Agnostic:** Can seamlessly operate using any default webcam configuration.

## ⚙️ Installation

### 1. Requirements
Ensure you have Python 3.8 or above installed on your system.

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python main.py
```

## 🧠 Approach & Methodology
1. **Camera Feed Capture:** OpenCV reads frames from the active webcam.
2. **Image Processing:** Frames are resized, horizontally flipped for a mirror effect, and color-converted to conform with MediaPipe's expectations.
3. **Landmark Detection:** MediaPipe extracts 21 distinct 3D landmarks (x, y, z) per hand.
4. **Gesture Logic Calculation:** 
   - *Four fingers:* Tip node position (Y-axis) is compared against the lower interphalangeal joint.
   - *Thumb:* Vectorized comparison (X-axis) between the thumb tip and IP joint, conditioned by handedness classification (left vs. right).
5. **Visualization:** Hand connections and finger counting logic nodes are re-drawn over the OpenCV frame with status-indicator color overlays.

## 👨‍💻 Author
**Đường Khánh Sơn** - *Giảng Viên CTUT. Ngành Cơ điện tử.*
