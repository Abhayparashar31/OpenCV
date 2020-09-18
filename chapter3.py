import cv2

img = cv2.imread("images/img0.jpg")
print(img.shape)

## shift + alt + A
""" imgResize = cv2.resize(img,(224,224))
imgResize2 = cv2.resize(img,(1024,1024))
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Increase size",imgResize2)
print(imgResize.shape) """

imgCropped = img[0:200,200:400]
##              height,width
cv2.imshow("Image cropped",imgCropped)
cv2.imshow("Image",img)
cv2.waitKey(0)