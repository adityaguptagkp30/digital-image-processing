import cv2

img=cv2.imread("Resources/lena.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny=cv2.Canny(img,150,200)


cv2.imshow("gray Image",imgGray)
cv2.imshow("blurry image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.waitKey(0)