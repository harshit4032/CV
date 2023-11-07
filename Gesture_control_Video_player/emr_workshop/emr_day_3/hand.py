from cv2 import cv2
def nothing(x):
    pass

def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("T","thresholding",0,255, nothing)

img_path = './emr_day_2/photos/hand.jpg'
img = cv2.imread(img_path)
cv2.imshow("orignal image",img)
gray_scale  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image", gray_scale)
 
createTrackbar()

while True:
    T = cv2.getTrackbarPos("T","thresholding")
    print(T)
    _,thresh_img  =cv2.threshold(gray_scale,T,255,cv2.THRESH_BINARY)
    cv2.imshow("thresh ig",thresh_img)
    key = cv2.waitKey(1)
    if (key == ord('q')):
        break


# cv2.waitKey(0)
# cv2.release()
cv2.destroyAllWindows()