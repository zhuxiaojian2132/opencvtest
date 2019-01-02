import cv2 as cv
import numpy as np

#图像二值化(全局)
def threshold_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    # ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_TRIANGLE)
    # ret,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY|cv.THRESH_TRUNC)
    print("threshold value %s:"%ret)
    cv.imshow("binary",binary)

#图像二值化(局部)
def local_threshold_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #binary=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,25,10)
    binary=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)#blocksize=25
    cv.imshow("local_binary",binary)

#超大图像二值化（分块）
def big_img_binary(img):
    print(img.shape)
    cw=256
    ch=256
    h,w=img.shape[:2]
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi=gray[row:row+ch,col:col+cw]
            #ret,dst=cv.threshold(roi,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU) 
            dst=cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,10)
            gray[row:row+ch,col:col+cw]=dst
            #print(np.std(dst),np.mean(dst))
    cv.imwrite("E:/Python_Code/VSC_Python/bigpicture_binary.jpg",gray)

img=cv.imread("E:/Python_Code/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
threshold_demo(img)
local_threshold_demo(img)

img2=cv.imread("E:/Python_Code/VSC_Python/bigpicture.jpg")
big_img_binary(img2)

cv.waitKey(0)
cv.destroyAllWindows()