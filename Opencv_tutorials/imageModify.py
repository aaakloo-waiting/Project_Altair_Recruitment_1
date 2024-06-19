import cv2 as cv

img = cv.imread('GOAT.jpg') # Reads image, fn parameter takes img location

# Converting to grayscale image
grayGoat=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blur image
blurGoat=cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

# Edge Cascade
cany = cv.Canny(img, 125, 175)

# Dilating image
dilated = cv.dilate(cany, (3,3), iterations=1)

# Eroding image
eroded = cv.erode(dilated, (3,3), iterations=1)

# Resizing image
resize=cv.resize(img, (400, 400)) # resize image ignoring aspect ration

# Cropping
cropped = img[5:200, 5:150]
cv.imshow('Ankara Blurry Messi', cropped) # Displays the read img in new window; fn param title in window & matrix of pixel to display
cv.waitKey(0) # waits for infinite(0) time for a key to be pressed
