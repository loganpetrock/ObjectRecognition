import cv2
import os
import time

folder_name = "camera_equipment_dataset"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
img_counter = 0

capture_interval = 3
last_capture_time = time.time()

print(f"Saving to: {folder_name}")
print("Automated: capturing an image every {capture_interval} seconds | ESC: Exit")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
    if not ret:
        break

    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        img_name = f"{folder_name}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Automated Capture: {img_name}")

        img_counter +=1
        last_capture_time = current_time

    cv2.imshow("Automated Data Collection - Window", frame)
    
    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Closing...")
        break

cap.release()
cv2.destroyAllWindows()