#   Building Sketches from Photographs using OpenCV

#   Importing Open CV Library
import cv2

#   Reading image
img = cv2.imread("butterfly.jpg", )

#   Converting image into grayscale to have black and white image of output
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#   Calculate per element bit-wise imversion of input in order to make brighter region into lighter and lighter into brighter
#   In order to find edges of the image very easily
imgInvert = cv2.bitwise_not(imgGray)


cv2.imshow("Buttefly", imgInvert)
cv2.waitKey()