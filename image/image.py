import cv2 as cv 
import numpy as np

#load image 
img = cv.imread("Photo24.png",0) 

#show image 
cv.namedWindow("mage_1")
cv.imshow("image_3",img)

#update windows show 
key=cv.waitKey(0) 

if key==ord("s"):
    cv.imwrite("new_image.png",img)

#destroy all windows is openned 
cv.destroyAllWindows()