import cv2
import numpy as np

img = cv2.imread('images/img0.jpg')

hor = np.hstack((img,img))

cv2.imshow("Horizontal",hor)

cv2.waitKey(0)