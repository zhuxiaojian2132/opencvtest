import cv2 as cv
import numpy as np
#颜色空间
def color_space_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv=cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)

#截取视频中单色区块
def extrace_object_demo():
    capture=cv.VideoCapture("D:/Python_Code/VSC_Python/vtest.avi")
    while(True):
        ret,frame=capture.read()
        if ret==False:
            break
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([0,0,0])
        upper_hsv=np.array([180,255,46])
        mask=cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv) #截取特定区域
        #dst=cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        #cv.imshow("mask",dst)
        c=cv.waitKey(40)
        if c==27:
            break

img=cv.imread("D:/Python_Code/VSC_Python/view.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#color_space_demo(img)
extrace_object_demo() 
#通道分离与合并
# b,g,r=cv.split(img)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# chg_img=cv.merge([b,g,r])
# chg_img[:,:,0]=0
# cv.imshow("changed image",chg_img)
cv.waitKey(0)
cv.destroyAllWindows()