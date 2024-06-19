import cv2 as cv

# ->Rescaling images, videos, live videos fn
def rescaleFrame(frame, scale=0.35):
    width = int(frame.shape[1]*scale) # shape[1] for width
    height = int(frame.shape[0]*scale) # shape[0] for height
    dimensions= (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#->Reading images
img = cv.imread('GOAT.jpg') # Reads image, fn parameter takes img location
resizedImg=rescaleFrame(img)
cv.imshow('Ankara Messi', resizedImg) # Displays the read img in new window; fn param title in window & matrix of pixel to display

cv.waitKey(0) # waits for infinite(0) time for a key to be pressed


# -> Reading videos
# capture = cv.VideoCapture('color.mp4') # int argument(0 or more) for multiple webcams, video path for existing videos
# while True :
#     isTrue, frame = capture.read() # capture is part of VideoCapture class which is being read grame by frame using capture.read()
#     resizedFrame = rescaleFrame(frame)
#     cv.imshow('My first Downloaded Video (Resized)', resizedFrame) # showing frame

#     if cv.waitKey(20) & 0xFF==ord('d'): # waits for 20 seconds and until 'd' key-pressing, when pressed it stops showing frame
#         break

# capture.release() # release all read frame
# cv.destroyAllWindows() # once done destroy all window










