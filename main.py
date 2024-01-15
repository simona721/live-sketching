import cv2
import numpy as np 

def liveSketch(image):
    #Cover the image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Blur the image
    img_blur=cv2.GaussianBlur(img_gray,(3,3),0)

    #Detect edges
    edges=cv2.Canny(img_blur,10,80)

    #Invert the threshold
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    return mask

#Capture video from webcam
capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    cv2.imshow("Live Capture", liveSketch(frame))
    if cv2.waitKey(1) == 13:
        break

capture.release()

cv2.destroyAllWindows()

