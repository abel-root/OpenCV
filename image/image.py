import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png",0) 

#show image 
plt.imshow(img)
plt.show()