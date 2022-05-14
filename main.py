#   Building Sketches from Photographs using OpenCV

#   Importing Open CV Library
import cv2

imgName = "img.jpg"
#   Reading image
img = cv2.imread(imgName )

#   Converting image into grayscale to have black and white image of output
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#   Calculate per element bit-wise imversion of input in order to make brighter region into lighter and lighter into brighter
#   In order to find edges of the image very easily
imgInvert = cv2.bitwise_not(imgGray)

#   Reduce noise of images and blurring to smoothen image with the specified Gaussian kernel
imgSmoothing = cv2.GaussianBlur(imgInvert, (21, 21), sigmaX=0, sigmaY=0 )

#   Divide the grayscale image by the inverse of the blurred images, remains the highlights of boldest edges

def divideByInversion(x, y):
    return cv2.divide(x, 255 - y, scale = 256)

#   Final Image
finalImage = divideByInversion(imgGray, imgSmoothing)

#   Save image in your local drive in same directory of python script 
cv2.imwrite("finalimage.jpg", finalImage)

#   Showing final image
cv2.imshow("Sketch", finalImage)

#   Waits until any key is pressed
cv2.waitKey()

#   Destroy all windows of images after clicking any button
cv2.destroyAllWindows()