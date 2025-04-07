import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt


# mouse callback function
def drawfunction(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),20,(0,0,255),-1)
#load image 

img = cv.imread("Photo24.png") 

cv.setMouseCallback('image',drawfunction)

while(1):
    cv.imshow("Result",img)
    key=cv.waitKey(1)
    if key==27:
        break
cv.destroyAllWindows()
