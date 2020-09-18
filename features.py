import numpy as np
import cv2

img = cv2.imread("images/test.jpg")
width,height = 250,350
pts1 = np.float32([[26,53],[191,53],[26,286],[191,286]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("King Image",imgOutput)
cv2.waitKey(0)