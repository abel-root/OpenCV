import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 
img_1 = cv.imread("new_image.png")


dist1 = cv.bitwise_and(img,img_1, mask=None)
dist2 = cv.bitwise_or(img,img_1,mask=None)
dist3=cv.bitwise_xor(img,img_1, mask=None)

cv.imshow("img",img)
cv.imshow("img_1",img_1)
cv.imshow("AND ",dist1)
cv.imshow("OR", dist2)
cv.imshow("XOR",dist3)

cv.imshow("Not img ", cv.bitwise_not(img, mask=None))
cv.imshow("Not img_1", cv.bitwise_not(img_1,mask=None))

if cv.waitKey(0) & 0xff =="q":
    cv.destroyAllWindows()