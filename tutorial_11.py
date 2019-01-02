import cv2 as cv
import numpy as np
#高斯金字塔
def pyramid_demo(img):
    level=3
    temp=img.copy()
    pyramid_imgs=[]
    for i in range(level):
        dst=cv.pyrDown(temp)
        pyramid_imgs.append(dst)
        cv.imshow("pyramid_down"+str(i),dst)
        temp=dst.copy()
    return  pyramid_imgs

#拉普拉斯金字塔
def lapalian_demo(img):
    pyramid_imgs=pyramid_demo(img)
    level=len(pyramid_imgs)
    for i in range(level-1,-1,-1):
        if i-1<0:
            expand=cv.pyrUp(pyramid_imgs[i],dstsize=img.shape[:2])
            lapls=cv.subtract(img,expand)
            cv.imshow("lapalian_demo"+str(i),lapls)
        else:
            expand=cv.pyrUp(pyramid_imgs[i],dstsize=pyramid_imgs[i-1].shape[:2])
            lapls=cv.subtract(pyramid_imgs[i-1],expand)
            cv.imshow("lapalian_demo"+str(i),lapls)

img=cv.imread("E:/Python_Code/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
pyramid_demo(img)
lapalian_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()