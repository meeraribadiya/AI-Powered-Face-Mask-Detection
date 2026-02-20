# 🛡️ AI-Powered Face Mask Detection  
### Real-Time Access Control System

📄 Project Report: [Click Here to View](https://drive.google.com/file/d/1WbBibllIR1VuuwdJrDRzXzUaU7qevoAc/view?usp=drive_link)

## 🔍 Overview

AI-Powered Face Mask Detection is a real-time security system built using **Python** and **OpenCV**.  
It detects human faces, verifies mask compliance, and provides instant **audio-visual feedback** for access control.

This system can be deployed in:
- Schools  
- Offices  
- Hospitals  
- Secure Facilities  



## ✨ Key Features

- Real-Time Face Detection (Haar Cascade)
- Mask / No-Mask Classification using LBPH
- Green Box → Access Granted
- Red Box + 1500Hz Beep → Access Denied
- Confidence Threshold System (Threshold: 185)
- Dataset Collection Module
- Histogram Equalization (Better Lighting Handling)
- Full Screen Display (1280x720)



## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:** OpenCV, NumPy, OS, Winsound  
- **Algorithm:** LBPH (Local Binary Patterns Histogram)  
- **Face Detection:** Haar Cascade Classifier  


## 📁 Project Structure

```
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
```



## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install opencv-contrib-python numpy
```

### 2️⃣ Collect Dataset

Capture ~100 images for:
- With Mask  
- Without Mask  

```bash
python capture_photos.py
```



### 3️⃣ Train Model

```bash
python train_ai.py
```

This generates:

```
trained_model.xml
```



### 4️⃣ Start Real-Time Detection

```bash
python detect_mask.py
```

Press **Q** to exit.



## ⚙️ System Logic

1. Face detected using Haar Cascade  
2. LBPH extracts facial texture features  
3. Confidence score evaluated  
   - < 185 → Mask OK  
   - > 185 → Wear a Mask  
4. System gives visual + audio feedback  



## 📌 Future Improvements

- CNN-based Deep Learning Model  
- Cloud Database Integration  
- Mobile Application Support  



## 👩‍💻 Developed By

**Mira Ribadiya**

