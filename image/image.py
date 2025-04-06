import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 

txt="KONAN Kouakou Abel"
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,txt,(200,100), font, 2,(0,0,255),2,cv.LINE_AA)

cv.imshow("Result",img)
cv.waitKey(0)
cv.destroyAllWindows()
