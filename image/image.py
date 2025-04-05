import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("spring.jpg") 
img_1 = cv.imread("lyon.jpeg")


rows,cols,channels = img_1.shape

roi = img[0:rows, 0:cols]

img2gray=cv.cvtColor(img_1,cv.COLOR_BGR2GRAY) # permet de convertir l'image rgb en image gray
ret, mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img_1,img_1,mask = mask)
# Put logo in ROI
dst = cv.add(img2_fg, img1_bg)
img[0:rows, 0:cols ] = dst

cv.imshow("Result",img)
cv.waitKey(0)
cv.destroyAllWindows()