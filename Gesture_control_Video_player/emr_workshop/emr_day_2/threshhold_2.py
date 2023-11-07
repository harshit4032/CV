import cv2 
img_path = "./emr_day_2/photos/gray_scale.png"
img =  cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('img',img)
h,w = gray_scale_img .shape
for i in range(0,h):
    for j in range(0,w):
        if j <= w//2:
            gray_scale_img[i,j] = 255
            print(gray_scale_img)
        else:
            gray_scale_img[i,j] = 0
            print(gray_scale_img[i,j])

cv2.imshow('img',gray_scale_img)

cv2.waitKey(0)