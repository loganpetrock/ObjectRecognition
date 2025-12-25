import cv2
import os

folder_name = "camera_equipment_dataset"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
img_counter = 0

print(f"Saving to: {folder_name}")
print("SPACE: Capture Image | ESC: Exit")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
    if not ret:
        break

    cv2.imshow("Manual Data Collection - Window", frame)
    
    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Closing...")
        break
    elif k % 256 == 32:
        img_name = f"{folder_name}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Captured: {img_name}")
        img_counter += 1

cap.release()
cv2.destroyAllWindows()