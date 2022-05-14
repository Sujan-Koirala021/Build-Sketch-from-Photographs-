
# Building sketches from photographs

This is a simple project that builds pencil sketch like images from photographs.

![img](https://user-images.githubusercontent.com/84112374/168413177-5b232b1c-6e94-4776-82fb-94ea807f8906.JPG)

![finalimage](https://user-images.githubusercontent.com/84112374/168413231-613355b9-d143-40fb-9c72-0c6010fe161e.jpg)

# About OpenCV
OpenCV stands for Open Source stands for Computer Vision, it is developed by Intel and Willow Garage, It is Officially launched in 1999 and later will Garage in 2000. OpenCV binds with Python to solve real-world problems. It supports languages like Python, Java, and MATLAB

The Opencv applications are as follows:
1. Object detection
2. Face Recognition
3. Identify the objects
4. Detecting Human activities
5. Stitching the images to produce the highest resolution
6. Recognize the scenery
7. Recognizing images stored in the Database
8. Remove Red Eye
9. Follow the eye movement and many other real-time applications

# Installation

## Install Opencv-python


```bash
  pip install opencv-python
```

# Usage

### Import opencv
```bash
  import cv2
```

###  Read image
```bash
  img = cv2.imread("img_name.jpg")
```
###  Convert to gray-scale image
```bash
   imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
###   Calculate per element bit-wise inversion of input 
Makes brighter region into lighter and lighter into brighter in order to find edges of the image very easily
```bash
    imgInvert = cv2.bitwise_not(imgGray)
```
###   Gaussian Blur
Reduces noise of images and blurs to smoothen image with the specified Gaussian kernel

```bash
    imgSmoothing = cv2.GaussianBlur(imgInvert, (21, 21), sigmaX=0, sigmaY=0 )
```
###   Divide the grayscale image by the inverse of the blurred images 
Remains the highlights of boldest edges

```bash
    def divideByInversion(x, y):
        return cv2.divide(x, 255 - y, scale = 256)

```

### Final image
```bash
    finalImage = divideByInversion(imgGray, imgSmoothing)
```
###  Save image in your local drive default : in same directory of python script 
```bash
    cv2.imwrite("finalimage.jpg", finalImage)
```

### Show final image

```bash
    cv2.imshow("Sketch", finalImage)
```

### Wait until any key is pressed

```bash
    cv2.waitKey()
```

### Destroy all windows of images after clicking any button

```bash
    cv2.destroyAllWindows()
```
## Documentation

- [Open-CV](https://pypi.org/project/opencv-python/)


## Authors

- [@sujankoirala](https://github.com/Sujan-Koirala021)
