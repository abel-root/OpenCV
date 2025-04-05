# OpenCV With pytthon and C/C++

## Description 

    This tutoral are the rule to learn the library OpenCV with pytthon and C/C++.
    The main goal of the tutoral is to be able to use the OpenCV library in python and c/c++ project for create the computer vision. 

## OpenCV with python 

### Loard image 
>For loarding image with the OpenCV, it must use the function :
1. imread()

```
    import cv2 as cv 
    img = cv.imread(filname, flags)
```
  - flags : 
     - ``` 1 ``` Loads a color image
     - ``` 0 ```  Loads image in grayscale mode
     - ``` -1 ``` Loads image as such including alpha channel

>It is posible to use without the flags. The image will be generate is color image 

    ```
    import cv2 as cv 
    img = cv.imread(filname, flags)

    ```
2. imshow()

    Use to show image on windows 
    
    ```
        cv.namedWindow("window_name") # rename windows 
        cv.imshow(windows_name, img)
    ```

3.  WaitKey() 

>Use to update the curent windows and can allows to ouside the windows with keyboard 
   
 ``` cv.Waitekey(0)```

### Resume loading image 

```
 import cv2 as cv 

 img = cv.imread(filename)
 cv.nameWindows(windows_name)
 cv.imshow(windows_name,img)

 cv.waitkety(0)
 cv.destroyAllWindows()

```
### Saves image 
    
For save image you can use the function ``` imwrite() ```, the image is saved in the current folder. 

>example :
     
 ```
 cv.imwrite(new_filename,img)
 ```

>Resume load and save image 
```
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
```
### Show image with the library matplotlib

>It's posible to show the image with the `matplotlib` library.

example : 
  
  ```
    import cv2 as cv 
    import matplotlib.pyplot as plt

    img = cv.imread(filename)  # load image 

    plt.imshow(img) # draw image 

    plt.show() # show image 

  ```
 
 ### Get image shape 

>The shape() method is used to get contours from the image. It allows to have : 
   - Width 
   - Height 
   - RGB chanal 

example : 

```
   print(img.shape) # to show ```img.shape``` data 
```

### Get image size 

>This function is use to get image size 

example : 

```
 print (img.size) # to show ```img.size``` data 
```

### Split the image chanal 

>This function is able to split chanal and retturned RGB chanal.

example :

```
import cv2 as cv 

img=cv.imread(filename)
 b,g,r = img.split()

```
Each element is ndarray. You can check to print data 

.eig : 
```
import cv2 as cv 

img=cv.imread(filename)
r,b,g = img.split()
print(f"r : {r}\n\n")
print(f"b : {b}\n\n")
print(f"g : {g}")
```

### Merge chanal 

This function is used to merge all chanal in one.

example : 
```
import cv2 as cv 

img=cv.imread(filename)
r,b,g = img.split()

```

### Bitwise Operations 

```Bitwise``` operations are used in image manipulation and for ```extracting``` the essential parts in the image.

Following operators are implemented in OpenCV:

  - ```bitwise_and```
  - ```bitwise_or```
  - ```bitwise_xor```
  - ```bitwise_not```

example : 

```
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

```
### cvtColor 

This function is used to convert image in a type in other type. For example in RGB en Gray 

- BRG to Gray :

```
import cv2 as cv

imgBRG=cv.imread(filename)
imgray=cv.cvtColor(imgBRG, cv.COLOR_BGR2GRAY)
```

- BRG to HSV : 

```
import cv2 as cv

imgBRG=cv.imread(filename)
imghsv=cv.cvtColor(imgBRG, cv.COLOR_BGR2HSV)
```

- BRG to RGB :

```
import cv2 as cv

imgBRG=cv.imread(filename)
imghsv=cv.cvtColor(imgBRG, cv.COLOR_BGR2RGB)
```

### threshold

This function is used to convert the ```gray image``` to the ```binary image```

```
    retval, dst = cv.threshold(src, thresh, maxval, type)

```
example : 

```
import cv2 as cv

imgBRG=cv.imread(filename)
imgray=cv.cvtColor(imgBRG, cv.COLOR_BGR2GRAY)
ret,binaryImage =cv.threshold(imgray,10,255,cv.THRESH_BINARY)

```
if pixel <10 then pixel=0
if pixel >= 10 then pixel=255
if pixel >255 then pixel = 255

- type : 

   - ```cv.THRESH_BINARY```
   - ```cv.THRESH_BINARY_INV```
   - ```cv.THRESH_TRUNC```
   - ```cv.THRESH_TOZERO```
   - ```cv.THRESH_TOZERO_INV```


