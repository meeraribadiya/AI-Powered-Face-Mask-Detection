import cv2
import os
import numpy as np

data = []
labels = []
categories = ["with_mask", "without_mask"]

print("[INFO] AI Training started. Please wait...")

for category in categories:
    path = os.path.join("dataset", category)
    label = categories.index(category) # 0 for mask, 1 for no mask
    
    if not os.path.exists(path):
        print(f"[ERROR] Path not found: {path}")
        continue

    print(f"[INFO] Training on category: {category}")
    for img in os.listdir(path):
        try:
            img_path = os.path.join(path, img)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            # Enhance contrast so the AI sees mask edges better
            image = cv2.equalizeHist(image)
            image = cv2.resize(image, (100, 100))
            
            data.append(image)
            labels.append(label)
        except:
            continue

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(data, np.array(labels))

recognizer.save("trained_model.xml")
print(f"[SUCCESS] Model ready! Trained on {len(data)} images.")