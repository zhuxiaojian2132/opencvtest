import cv2 as cv
import numpy as np

#canny算法 边缘提取
def canny_edge_demo(img):
    blurred=cv.GaussianBlur(img,(3,3),0)#降低噪声
    gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    grad_x=cv.Sobel(img,cv.CV_16SC1,1,0) 
    grad_y=cv.Sobel(img,cv.CV_16SC1,0,1)
    canny_edge=cv.Canny(grad_x,grad_y,50,150)
    #canny_edge=cv.Canny(blurred,50,150)  #也可以直接计算blurred
    cv.imshow("canny_edge",canny_edge)
    dst=cv.bitwise_and(img,img,mask=canny_edge)
    cv.imshow("colored_edge",dst)

#直线检测 hough line transform
# https://blog.csdn.net/u010429424/article/details/77822783
def line_detection(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSize=3)
    lines=cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta=line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("images_lines",img)   

def line_detection_possible_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges=cv.Canny(gray,50,150,apertureSize=3)
    lines=cv.HoughLinesP(edges,1,np.pi/180,200,minLineLength=50,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("images_lines_possible",img)  


#圆检测 
def detect_circles_demo(img):
    dst=cv.pyrMeanShiftFiltering(img,10,100)#对噪声敏感，降噪
    gray=cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=40,param2=50,minRadius=0,maxRadius=0)
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(img,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(img,(i[0],i[1]),2,(255,0,0),2)
    cv.imshow("detected_circles",img)
# img=cv.imread("E:/Python_Code/VSC_Python/lena.jpg")    
# img=cv.imread("E:/Python_Code/VSC_Python/sudoku.png")    
img=cv.imread("E:/github_repository/VSC_Python/coins1.jpg")    
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#canny_edge_demo(img)
#line_detection(img)
#line_detection_possible_demo(img)
detect_circles_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()