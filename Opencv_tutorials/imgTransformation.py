import cv2 as cv
import numpy as np
img = cv.imread('GOAT.jpg')

#Shifting image
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions=(img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x -->Left shift
# -y -->Up shift


# Roatating image
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension=(width, height)
    return cv.warpAffine(img, rotMat, dimension)

# Flipping image
flip = cv.flip(img, -1) # 0->x-axes, 1->y-axes, -1->both axes flip
rotated = rotate(img, 30)
translatedimg=translate(img, -300, 150)

cv.imshow('translatedimg', flip)
cv.waitKey(0)