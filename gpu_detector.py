import os
os.environ['YOLO_OFFLINE'] = 'True' 
os.environ['ULTRALYTICS_OFFLINE'] = 'True'

import cv2
import time
from ultralytics import YOLO

model = YOLO("best.onnx", task="detect")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("GPU for detection... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
    if not ret:
        break

    start_ms = time.time()

    results = model.predict(source=frame, verbose=False)

    end_ms = time.time()
    fps = 1 / (end_ms - start_ms)

    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Detecting Using GPU - Window", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()