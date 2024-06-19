import cv2 as cv
import numpy as np


def detect_red_and_white_regions(messi):
    messiHSV = cv.cvtColor(messi, cv.COLOR_BGR2HSV)

    redLower = np.array([150, 100, 100], dtype=np.uint8)
    redUpper = np.array([180, 255, 255], dtype=np.uint8)
    whiteLower = np.array([75, 0, 99], dtype=np.uint8)
    whiteUpper = np.array([179, 62, 255], dtype=np.uint8)

    redMask = cv.inRange(messiHSV, redLower, redUpper)
    whiteMask = cv.inRange(messiHSV, whiteLower, whiteUpper)
    comboRedWhite = cv.bitwise_or(redMask, whiteMask)
    finalMessi = cv.bitwise_and(messi, messi, mask=comboRedWhite)

    cv.imshow("Red-White regions detected!", finalMessi)
    cv.waitKey(0)


def analyze_goat(image_array):
    pvMin = np.min(image_array)
    pvMax = np.max(image_array)
    pvAvg = np.mean(image_array)
    pcNonzero = np.count_nonzero(image_array)
    pcZero = image_array.size - pcNonzero

    print("The minimum and maximum pixel values in the image: ", pvMin, pvMax)
    print("The average pixel value in the image: ", pvAvg)
    print("The total number of non-zero (foreground) pixels in the image: ", pcNonzero)
    print("The total number of zero (background) pixels in the image: ", pcZero)


img = cv.imread('GOAT.jpg')  # Reads image, fn parameter takes img location
imgGrayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
detect_red_and_white_regions(img)
analyze_goat(imgGrayscale)
