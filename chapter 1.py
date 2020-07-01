import cv2
import numpy as np

img=cv2.imread("Resources/lena.jpg")
kernel=np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny=cv2.Canny(imgGray,150,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("gray Image",imgGray)
cv2.imshow("blurry image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("dialted image",imgDialation)
cv2.imshow("erode image",imgEroded)
cv2.waitKey(0)