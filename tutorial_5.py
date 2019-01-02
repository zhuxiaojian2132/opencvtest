import cv2 as cv
import numpy as np

def fill_color_demo(img):
    copyImg=img.copy()
    h,w=img.shape[:2]
    mask=np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(50,50),(0,255,255),(30,30,30),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color",copyImg)

def fill_binary_demo(img):
    img=np.zeros([400,400,3],np.uint8)
    img[100:300,100:300,:]=255
    cv.imshow("fill_binary",img)

    mask=np.ones([402,402,1],np.uint8)
    mask[101:301,101:301]=0
    cv.floodFill(img,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("mask_filled_binary",img)

img=cv.imread("D:/Python_Code/VSC_Python/girl.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
# face=img[20:260,250:435]
# gray=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
# backface=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# img[20:260,250:435]=backface
# #cv.imshow("face",face)
# cv.imshow("face",img)
#fill_color_demo(img)
fill_binary_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()