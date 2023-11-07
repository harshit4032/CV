import cv2 
import numpy as np
img_path = "./emr_day_2/photos/sherlock_kid.png"
img = cv2.imread(img_path)
print(img.shape)
img_shape = img.shape
img_red = np.full(img_shape,[0,0,50],dtype=np.uint8)
cv2.imshow("image",img)
cv2.imshow("red_image",img_red)
# negative_img = img_white-img
mixed_img = np.add(img_red,img)
cv2.imshow('negative',mixed_img)
print(img_red)
cv2.waitKey(0)
cv2.destroyAllWindows()