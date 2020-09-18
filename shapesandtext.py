import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
#img[:] = 255,0,0

cv2.line(img,(0,0),(100,100),(0,255,0),3)
###      img start_point end_point thikness

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
##                                         cv2.filled except 2
cv2.circle(img,(400,50),30,(255,255,0),2)

## Put text on images
cv2.putText(img,"OPEN CV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
##           image       text points   font         thikness    color   
cv2.imshow("Image",img)
cv2.waitKey(0)
