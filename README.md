# 🚗 AI Driver Drowsiness Detection System

An AI-based real-time driver drowsiness detection system using Computer Vision and Machine Learning.

This project detects if the driver's eyes are closed and triggers an alarm to prevent accidents.

Built using OpenCV + MediaPipe Face Mesh + Python.

---

# 📌 Features

• Real-time face & eye detection
• Detects eye closure using EAR (Eye Aspect Ratio)
• Smart alarm system
• Stops alarm when eyes open
• Works with webcam
• Two versions:

* Basic Haar Cascade model
* Advanced AI (MediaPipe) model

---

# 🧠 Tech Stack

Python
OpenCV
MediaPipe
NumPy
SciPy

---

# 📂 Project Structure

sleep.py → Basic Haar cascade version
advanced_sleep.py → AI powered MediaPipe version
alarm.mp3 → Custom alarm sound
requirements.txt → Dependencies

---

# ⚙️ Installation

Clone repo:

git clone [https://github.com/yourusername/Sleep_detector.git](https://github.com/yourusername/Sleep_detector.git)
cd Sleep_detector

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

# ▶️ Run Basic Version

python sleep.py

Uses Haar cascade for eye detection.

---

# ▶️ Run Advanced AI Version (Recommended)

python advanced_sleep.py

Uses MediaPipe FaceMesh + EAR (Eye Aspect Ratio).
Much more accurate and interview-level.

---

# 🔊 Custom Alarm Sound

Replace alarm.mp3 with your own sound file.
Keep same name: alarm.mp3

---

# 🎯 How it Works

1. Detect face using webcam
2. Detect eye landmarks
3. Calculate EAR (Eye Aspect Ratio)
4. If EAR < threshold → eyes closed
5. Alarm triggers
6. Alarm stops when eyes reopen

---

# 🧪 Future Improvements

Add yawning detection
Head pose detection
Mobile deployment
Car integration
Deep learning model

---

# 👨‍💻 Author

Naman
AI/ML Enthusiast | Computer Vision Developer
