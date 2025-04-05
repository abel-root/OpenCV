import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 

img[:,:,0]=0
cv.namedWindow("img")
cv.imshow("img",img)


cv.waitKey(0)
cv.destroyAllWindows()

