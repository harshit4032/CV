import cv2
import numpy as np
video_reader = cv2.VideoCapture(0)

while True:
    success , frame = video_reader.read()
    if not success:
        break
    vid_white = np.full(frame.shape,[250,250,250],dtype=np.uint8)
    neg_vid = np.subtract(vid_white,frame)
    cv2.imshow("My video",neg_vid)
    key = cv2.waitKey(10)
    if key == ord(' '):
        break

video_reader.release()
cv2.destroyAllWindows
