import cv2
import numpy as np
img = cv2.imread("images/img0.jpg")

## Convert img to gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## Blur image
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)

## Edge Detector
imgCanny = cv2.Canny(img,100,150)
kernel = np.ones((5,5),np.uint8)
    ## image dialation(making edge bigger)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
    ## Image eroded (making edge lighter)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Edge Detection",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Erosion image",imgEroded)

cv2.waitKey(0)