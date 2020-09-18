import cv2


def getContours(img):
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.)

path = 'images/shapes.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

## Edge detection
imgCanny = cv2.Canny(imgGray,50,50)
## Contors detection






cv2.imshow("Gray",imgGray)
cv2.imshow("Edge",imgCanny)
cv2.waitKey(0)