import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 

cv.line(img,(20,1000),(1000,20),(255,0,0),3) # color is BGR

cv.circle(img,(200,200), 100, (255,255,0), -1)

cv.rectangle(img,(500,200),(800,500),(0,255,0),5)

cv.ellipse(img, (300,425), (80, 20), 5, 0, 360, (0,0,255), -1)

cv.imshow("Result",img)
cv.waitKey(0)
cv.destroyAllWindows()
