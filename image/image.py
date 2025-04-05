import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png",1) 

# shape 

print(img.shape)

#show image 
plt.imshow(img)
plt.show()