# OpenCV With pytthon and C/C++

## Description 

    This tutoral are the rule to learn the library OpenCV with pytthon and C/C++.
    The main goal of the tutoral is to be able to use the OpenCV library in python and c/c++ project for create the computer vision. 

## OpenCV with python 

### Loard image 
  For loarding image with the OpenCV, it must use the function :
1. imread()

```
    import cv2 as cv 
    img = cv.imread(filname, flags)
```
  - flags : 
     - ``` 1 ``` Loads a color image
     - ``` 0 ```  Loads image in grayscale mode
     - ``` -1 ``` Loads image as such including alpha channel

    It is posible to use without the flags. The image will be generate is color image 

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

    Use to update the curent windows and can allows to ouside the windows with keyboard 
   
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

example :
     
 ```
 cv.imwrite(new_filename,img)
 ```

Resume load and save image 
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

It's posible to show the image with the `matplotlib` library.

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