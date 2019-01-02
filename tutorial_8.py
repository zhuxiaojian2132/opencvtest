import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#2D的直方图+matplotlib来显示
def hist2d_demo(img):
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hist=cv.calcHist([img],[0,1],None,[180,256],[0,180,0,256])  #HSV的2维直方图计算
    #cv.imshow("hist2d",hist)  #原始显示
    plt.imshow(hist,interpolation="nearest")
    plt.title("2D Histogram")
    plt.show()

#直方图反向投影
# https://www.sohu.com/a/148538953_823210
# https://blog.csdn.net/zzq060143/article/details/73176699
def backProjection_demo():
    pattern=cv.imread("E:/Python_Code/VSC_Python/pattern.png")
    target=cv.imread("E:/Python_Code/VSC_Python/backpojection.png")
    patt_hsv=cv.cvtColor(pattern,cv.COLOR_BGR2HSV)
    target_hsv=cv.cvtColor(target,cv.COLOR_BGR2HSV)
    #show image
    cv.imshow("target",target)
    cv.imshow("pattern",pattern)
    #BackProject
    pattHist=cv.calcHist([patt_hsv],[0,1],None,[36,48],[0,180,0,256]) #bins的个数可以来调整其筛选效果
    cv.normalize(pattHist,pattHist,0,255,cv.NORM_MINMAX)
    dst=cv.calcBackProject([target_hsv],[0,1],pattHist,[0,180,0,256],1) 
    cv.imshow("bakproject_img",dst)


img=cv.imread("E:/Python_Code/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)

hist2d_demo(img)

backProjection_demo()
cv.waitKey(0)
cv.destroyAllWindows()