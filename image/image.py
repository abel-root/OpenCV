import cv2 as cv 
import numpy as np

#load image 
img = cv.imread("Photo24.png") 

#show image 
cv.namedWindow("mage_1")
cv.imshow("image_3",img)

#update windows show 
cv.waitKey(0) 

#destroy all windows is openned 
cv.destroyAllWindows()