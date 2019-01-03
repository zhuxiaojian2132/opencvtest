import cv2 as cv
import numpy as np

def top_hat_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst=cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)  #cv.MORPH_BLACKHAT
    deltaimg=np.array(gray.shape,np.uint8)
    deltaimg=100
    dst=cv.add(dst,deltaimg)
    cv.imshow("top_hat_demo",dst)

def hat_binary_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst=cv.morphologyEx(binary,cv.MORPH_BLACKHAT,kernel)  
    cv.imshow("binary_black_hat_demo",dst)



img=cv.imread("E:/github_repository/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
top_hat_demo(img)
hat_binary_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()