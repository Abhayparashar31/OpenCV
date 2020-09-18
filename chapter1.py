import cv2
print("Package Imported")

## Reading Images
'''
img = cv1.imread("images/img0.jpg")
cv1.imshow("Output",img)
cv1.waitKey(0)
'''

## Reading video
'''
cap = cv2.VideoCapture("video/video.mp4")
while True:
    success , img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
'''


## Using Webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)  ## width
cap.set(4,480)  ## Height
cap.set(10,100) ## Britness
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
