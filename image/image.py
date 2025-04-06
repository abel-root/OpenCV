import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 

cv.line(img,(20,1000),(1000,20),(255,0,0),3) # color is BGR

cv.imshow("Result",img)
cv.waitKey(0)
cv.destroyAllWindows()
