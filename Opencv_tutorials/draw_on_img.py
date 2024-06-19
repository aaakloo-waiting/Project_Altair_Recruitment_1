import cv2 as cv
import numpy as np

imgBlank=np.zeros((500, 500, 3), dtype='uint8') # creating a blank image size(500X500), 3 for number of color channels (in BGR)
# -> painting the blank image to a color
imgBlank[100:250, 150:200]=255,0,0
cv.rectangle(imgBlank, (100, 150), (250, 200), (255,0,255), thickness=-1) # Negative -1 thickness means filling the rectangle
cv.circle(imgBlank, (imgBlank.shape[1]//2, imgBlank.shape[0]//2), 50, (0, 255, 250), thickness=-1)
cv.line(imgBlank, (150, 100), (imgBlank.shape[1]//2, imgBlank.shape[0]//2), (0, 255, 0), thickness=2)
cv.putText(imgBlank, "aaakloo_waiting",(20, 75), cv.FONT_HERSHEY_DUPLEX, 1.10, (225, 200, 250), 4)
cv.imshow('Orange image', imgBlank) 

cv.waitKey(0) 
