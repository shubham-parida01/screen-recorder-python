import cv2
import pyautogui
import numpy as np

resolution = (1920,1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = 'ScreenRecording.avi'
output = cv2.VideoWriter(filename , codec , 60 , resolution)

cv2.namedWindow('Live Recording' , cv2.WINDOW_NORMAL)

cv2.resizeWindow('Live Recording' , 480 , 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)

    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow('Live Recording' , frame)

    if cv2.waitKey(1) == ord('q'):    # press 'q' to stop
        break

output.release()
cv2.destroyAllWindows()
