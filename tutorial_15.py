import cv2 as cv
import numpy as np

#腐蚀
def erode_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst=cv.erode(binary,kernel)
    cv.imshow("erode_demo",dst)
#膨胀
def dilate_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst=cv.dilate(binary,kernel)
    cv.imshow("dilate_demo",dst)

#开操作 
def open_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,1))
    dst=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open_demo",dst)

#闭操作 
def close_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(10,10))  #取大一点，将填充大的闭合区域
    dst=cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("close_demo",dst)

#img=cv.imread("E:/github_repository/VSC_Python/bin.JPG") #闭操作
img=cv.imread("E:/github_repository/VSC_Python/bin2.JPG") #开操作 
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#erode_demo(img)
#dilate_demo(img)
open_demo(img)
#close_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()