import cv2 as cv
import numpy as np

#轮廓发现
def contours_demo(img):
    dst=cv.GaussianBlur(img,(3,3),0)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary_img",binary)

    #cloneImage,contours,heriachy=cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cloneImage,contours,heriachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(img,contours,i,(0,0,255),2)#-1 填充
        print(i)
    cv.imshow("detect_contours",img)

#多边形拟合
def measure_object(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    print("threshold value:%s"%ret)
    cv.imshow("binary img",binary)
    outimg,contours,hireachy=cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area=cv.contourArea(contour)
        x,y,w,h=cv.boundingRect(contour)
        mm=cv.moments(contour)
        #print(type(mm))
        cx=mm['m10']/mm['m00']
        cy=mm['m01']/mm['m00']
        cv.circle(img,(np.int(cx),np.int(cy)),2,(255,255,0),-1)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        print("contour area %s"%area)
        approxCur=cv.approxPolyDP(contour,4,True)
        print(approxCur.shape)
    cv.imshow("measure_contours",img)
#img=cv.imread("E:/github_repository/VSC_Python/coins2.jpg")
img=cv.imread("E:/github_repository/VSC_Python/digits.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#contours_demo(img)
measure_object(img)
cv.waitKey(0)
cv.destroyAllWindows()