import cv2 
img_path = "./emr_day_2/photos/book_page.jpg"
img =  cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('img',img) 
thresh_val,thresh_img = cv2.threshold(gray_scale_img,127,255,cv2.THRESH_OTSU)
print(thresh_val)
cv2.imshow('img2',thresh_img)
cv2.waitKey(0)