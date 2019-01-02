import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst=cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):
    dst=cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

def multi_demo(m1,m2):
    dst=cv.multiply(m1,m2)
    cv.imshow("multi_demo",dst)

def divide_demo(m1,m2):
    dst=cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)

def logic_demo(m1,m2):
    #dst=cv.bitwise_and(m1,m2)
    dst=cv.bitwise_or(m1,m2)
    cv.imshow("logic_demo",dst)

def contrast_brigthtness_demo(img,c,b):
    h,w,ch=img.shape
    blank=np.zeros([h,w,ch],img.dtype) #空白黑图
    dst=cv.addWeighted(img,c,blank,1-c,b)
    cv.imshow("con-bri-image",dst)

def others(m1,m2):
    M1=cv.mean(m1)
    M2,dev2=cv.meanStdDev(m2) #均值与标准方差
    h,w=m2.shape[:2]

    img=np.zeros([h,w],np.uint8)
    m,dev=cv.meanStdDev(img)
    print(m)
    print(dev)

img1=cv.imread("D:/Python_Code/VSC_Python/LinuxLogo.jpg")
img2=cv.imread("D:/Python_Code/VSC_Python/WindowsLogo.jpg")
cv.imshow("image1",img1)
cv.imshow("image2",img2)

#add_demo(img1,img2)
#subtract_demo(img1,img2)
#multi_demo(img1,img2)
#divide_demo(img1,img2)
#logic_demo(img1,img2)
others(img1,img2)

img=cv.imread("D:/Python_Code/VSC_Python/lena.jpg")
cv.imshow("orign image",img)
contrast_brigthtness_demo(img,1.5,10) #对比度1.5 亮度 10
cv.waitKey(0)