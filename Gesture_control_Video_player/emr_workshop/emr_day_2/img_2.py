import cv2 
import numpy as np
img_path = "./emr_day_2/photos/sherlock_kid.png"
img = cv2.imread(img_path)
print(img.shape)
img_shape = img.shape
img_white = np.full(img_shape,255,dtype=np.uint8)
cv2.imshow("image",img)
cv2.imshow("white_image",img_white)
# negative_img = img_white-img
negative_img = np.subtract(img_white,img)
cv2.imshow('negative',negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()