import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def image_hist_demo(img):
    color =("blue","green","red")
    for i,c in enumerate(color):
        hist=cv.calcHist([img],[i],None,[256],[0,256])#每一维的hist
        plt.plot(hist,color=c)
        plt.xlim([0,256])
    plt.show("3通道的直方图")

#直方图均衡化，对比度增强
def equalHist_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    dst=cv.equalizeHist(gray)
    cv.imshow("equal_demo",dst)
#直方图均衡化(自适应)
def clahe_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst=clahe.apply(gray)
    cv.imshow("clahe_demo",dst)

#创建一个rgb三通道构成的直方图
def create_rgb_hist(img):
    h,w,c=img.shape
    rgbHist =np.zeros([16*16*16,1],np.float32)#bins=16*16*16
    bsize=256/16
    for row in range(h):
        for col in range(w):
            b=img[row,col,0]
            g=img[row,col,1]
            r=img[row,col,2]
            index =np.int((b/bsize))*16*16+np.int((g/bsize))*16+np.int(r/bsize)#b,g,r都在同一个bins内，则落到一个index下
            rgbHist[np.int(index),0]=rgbHist[np.int(index),0]+1
    return rgbHist

#直方图相似度比较
def hist_compare(img1,img2):
    hist1=create_rgb_hist(img1)
    hist2=create_rgb_hist(img2)
    match1=cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)#巴氏距离
    match2=cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)#卡方距离
    match3=cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)#相关性
    print("巴氏距离：%s, 卡方距离:%s ,相关性 %s"%(match1,match2,match3))

img=cv.imread("E:/Python_Code/VSC_Python/hist1.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#image_hist_demo(img)
#equalHist_demo(img)
#clahe_demo(img)

img1=cv.imread("E:/Python_Code/VSC_Python/soldier.jpg")
img2=cv.imread("E:/Python_Code/VSC_Python/soldier2.jpg")
hist_compare(img1,img2)
cv.waitKey(0)
cv.destroyAllWindows()