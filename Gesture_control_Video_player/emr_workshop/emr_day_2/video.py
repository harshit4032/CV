import cv2
import numpy as np
video_reader = cv2.VideoCapture(0)

while True:
    success , frame = video_reader.read()
    if not success:
        break
    
    cv2.imshow("My video",frame)
    key = cv2.waitKey(5000)
    if key == ord(' '):
        break
print(success)
print(frame)
video_reader.release()
cv2.destroyAllWindows
