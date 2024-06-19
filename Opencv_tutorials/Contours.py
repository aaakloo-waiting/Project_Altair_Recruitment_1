import cv2 as cv
import numpy as np

img = cv.imread('GOAT.jpg') # Reads image, fn parameter takes img location
canny = cv.Canny(img, 125, 175)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # RETR_LIST returns all contours
print(f'{len(contours)} contours found')
cv.imshow('Ankara Messi', canny) # Displays the read img in new window; fn param title in window & matrix of pixel to display

cv.waitKey(0) # waits for infinite(0) time for a key to be pressed

