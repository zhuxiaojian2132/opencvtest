import cv2 as cv
import numpy as np
#图像的梯度： 一阶导数与sobel算子；二阶导数与laplacian算子
def sobel_demo(img):
    grad_x=cv.Sobel(img,cv.CV_32F,1,0) #cv.Scharr()  对sobel算子的一个增强版本，强化边缘
    grad_y=cv.Sobel(img,cv.CV_32F,0,1)
    gradx=cv.convertScaleAbs(grad_x)
    grady=cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x",gradx)
    cv.imshow("gradient_y",grady)
    gradxy=cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient_xy",gradxy)

def lapalcian_demo(img):
    # dst=cv.Laplacian(img,cv.CV_32F)
    kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]]) #4邻域的laplacian; [[1,1,1],[1,-8,1],[1,1,1]  8邻域则增强边缘
    dst=cv.filter2D(img,cv.CV_32F,kernel=kernel)
    lpls=cv.convertScaleAbs(dst)
    cv.imshow("laplacian_demo",lpls)

img=cv.imread("E:/Python_Code/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
sobel_demo(img)
lapalcian_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()