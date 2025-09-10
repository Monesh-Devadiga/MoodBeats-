# emotion_detector.py

import cv2
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)
    detected_emotion = None 

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            detected_emotion = result[0]['dominant_emotion']
            print(f"Detected Emotion: {detected_emotion}")
        except:
            continue

        cv2.putText(frame, "Press 'Q' to capture emotion", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return detected_emotion