import cv2 
img_path  = "./emr_day_2/photos/sherlock_kid.png"
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_HSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# img_crop = img[0:,300:]
# h,w,c = img.shape
# img_cropped = img[0:, w//2:]
# print(img_slice)
# print(img.shape)
# cv2.imshow("Image",img_cropped)
# cv2.imshow("hsv",img_HSV)
# cv2.imshow("gray_img",img_gray)
# cv2.imwrite("./emr_day_2/photos/sherlock_kid_gray.png",img_gray)
# print(img.shape)
# print(img_gray.shape)
# img_resize = cv2.resize(img,(500,500))
# cv2.imshow("resize",img_resize) 

cv2.waitKey(0)