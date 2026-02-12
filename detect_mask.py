import cv2
import os
import winsound

# Load the face detection and recognition models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

if not os.path.exists("trained_model.xml"):
    print("[ERROR] 'trained_model.xml' not found. Please run train_ai.py first!")
else:
    recognizer.read("trained_model.xml")
    cap = cv2.VideoCapture(0)

    # --- SETUP LARGE WINDOW ---
    cv2.namedWindow('AI Face Mask Guard - Secure Access', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('AI Face Mask Guard - Secure Access', 1280, 720)

    mask_counter = 0
    no_mask_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Mirror the frame
        frame = cv2.flip(frame, 1)
        
        # --- 1. INSTRUCTION OVERLAY ---
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (frame.shape[1], 90), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        
        cv2.putText(frame, "TIP: Sit in a CLEAR BACKGROUND for better detection.", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, "TIP: Stay 2-3 feet away and ensure good lighting.", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        # Added exit instruction on screen
        cv2.putText(frame, "PRESS 'Q' ON KEYBOARD TO QUIT", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        # --- 2. IMAGE PRE-PROCESSING ---
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray) 

        # Face detection
        faces = face_cascade.detectMultiScale(gray, 1.1, 10, minSize=(100, 100))

        for (x, y, w, h) in faces:
            roi_gray = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
            label_id, confidence = recognizer.predict(roi_gray)

            # DETECTION LOGIC
            if label_id == 0 and confidence < 185:
                mask_counter += 1
                no_mask_counter = 0
            else:
                no_mask_counter += 1
                mask_counter = 0

            # STABILITY LOGIC
            if mask_counter >= 2:
                status, color = "MASK OK!", (0, 255, 0)
                msg = "ACCESS GRANTED"
            elif no_mask_counter >= 2:
                status, color = "PLEASE WEAR A MASK!", (0, 0, 255)
                msg = "WARNING: ACCESS DENIED"
                winsound.Beep(1500, 200) 
            else:
                continue 

            # --- 3. DRAWING UI ---
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 4)
            cv2.putText(frame, status, (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(frame, msg, (40, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 4)

        # Show final frame
        cv2.imshow('AI Face Mask Guard - Secure Access', frame)
        
        # --- 4. THE QUIT LOGIC ---
        # If 'q' is pressed, it breaks the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Closing System...")
            break

    cap.release()

    cv2.destroyAllWindows()

