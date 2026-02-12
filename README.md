# 🛡️ AI-Powered Face Mask Detection: Real-Time Access Control System

## 🔍 Project Overview
AI-Powered Face Mask Detection is a real-time security system that monitors face mask compliance using Computer Vision and Machine Learning.

The system detects human faces, checks whether a mask is worn or not, and provides instant audio-visual feedback for access control.

This project is built using Python and OpenCV and can be used in schools, offices, hospitals, and secure facilities.



## ✨ Key Features

- Real-Time Face Detection using Haar Cascade Classifier
- Audio Alert System (1500Hz buzzer for "No Mask")
- Green Box → Mask OK (Access Granted)
- Red Box + Beep → No Mask (Access Denied)
- LBPH Face Recognition Algorithm
- Confidence Threshold System (Threshold: 185)
- Dataset Collection Module
- Full-Screen Display Support (1280x720)
- Histogram Equalization for better lighting handling
- Frame Stability Logic to prevent flickering



## 🛠️ Tech Stack

Language: Python 3.x  
Libraries: OpenCV, NumPy, OS, Winsound  
Algorithm: LBPH (Local Binary Patterns Histogram)  
Face Detection: Haar Cascade Classifier  



## 📁 Project Structure
```text
FACE_MASK_DETECTION/
│
├── dataset/
│   ├── with_mask/
│   └── without_mask/
│
├── capture_photos.py
├── train_ai.py
├── detect_mask.py
├── trained_model.xml
└── README.md



## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

Open terminal and run:

pip install opencv-contrib-python numpy



### 2️⃣ Data Collection

Collect around 100 images for each category (with mask & without mask).  
Move your head slightly while capturing images for better accuracy.

Run:

python capture_photos.py



### 3️⃣ Training

Train the AI model using your collected dataset.

Run:

python train_ai.py

This will generate:
trained_model.xml



### 4️⃣ Final Detection

Start the real-time mask detection system:

python detect_mask.py

Press 'Q' to exit the program.



## 📊 System Logic

Step 1: Face Detection  
The system detects faces using haarcascade_frontalface_default.xml.

Step 2: Recognition  
LBPH algorithm generates a texture map and compares it with trained data.

Step 3: Thresholding  
If confidence score is below 185 → Mask OK  
If confidence score is above 185 → PLEASE WEAR A MASK

Step 4: Feedback  
Green box = Access Granted  
Red box + Beep = Access Denied  



## 🤝 Acknowledgments

OpenCV – For providing an open-source Computer Vision library.  
LBPH Research – For texture-based recognition algorithm.  



## 📌 Future Improvements

- Deep Learning based CNN model integration  
- Cloud database integration  
- Mobile app support  
- Multi-user detection system  



 Developed By: Mira Ribadiya  


