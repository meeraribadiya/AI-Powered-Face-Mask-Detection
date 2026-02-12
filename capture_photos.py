import cv2
import os
import time

# List of both categories
categories = ["with_mask", "without_mask"]
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

for category in categories:
    path = os.path.join("dataset", category)
    if not os.path.exists(path):
        os.makedirs(path)

    print(f"\n[ACTION] Get ready for: {category.upper()}")
    print("[INFO] Starting in 3 seconds...")
    time.sleep(3)

    count = 0
    while count < 100:  # Collects 100 images for each
        ret, frame = cap.read()
        if not ret: break
        
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Save only the face area
            roi_resized = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
            cv2.imwrite(os.path.join(path, f"{count}.jpg"), roi_resized)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            count += 1

        cv2.putText(frame, f"Category: {category} | Progress: {count}%", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.imshow("Automated Data Collection", frame)

        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

print("\n[SUCCESS] All data collected for both categories!")
cap.release()
cv2.destroyAllWindows()