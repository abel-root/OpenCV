import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

#load image 
img = cv.imread("Photo24.png") 

b,g,r=cv.split(img)

