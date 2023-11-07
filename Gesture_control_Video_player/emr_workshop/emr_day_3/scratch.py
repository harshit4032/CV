from cv2 import cv2 
import numpy

def nothing(x):
    print("yes")
    pass

def create_trackbar():
    cv2.namedWindow("win")
    cv2.createTrackbar("temp","win",0,255,nothing)
create_trackbar()
cv2.waitKey(0)
cv2.destroyAllWindows()
# -> onchange  -> null exception -> (nothing)ref problem