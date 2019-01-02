import cv2 as cv
import numpy as np

#均值模糊：去随机噪声 
def blur_mean_demo(img):
     dst=cv.blur(img,(1,5))
     cv.imshow("blur_demo",dst)

#均值模糊：去椒盐噪声 
def blue_median_demo(img):
    dst=cv.medianBlur(img,5)
    cv.imshow("median_blur_demo",dst)


#自定义模糊： 
def custom_blur_demo(img):
    #kernel=np.ones([5,5],np.float32)/25 #自定义5*5的均值模糊
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)/9  #锐化算子
    dst=cv.filter2D(img,-1,kernel=kernel)
    cv.imshow("custom_blur_demo",dst)

#截断范围
def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    return pv 

#加高斯噪声
def gaussian_noise(img):
    h,w,c=img.shape
    for row in range(h):
        for col in range(w):
            s=np.random.normal(0,20,3)
            b=img[row,col,0] #blue
            g=img[row,col,1] #green
            r=img[row,col,2] #red
            img[row,col,0]=clamp(b+s[0])
            img[row,col,1]=clamp(g+s[1])
            img[row,col,2]=clamp(r+s[2])
    cv.imshow("noise img",img)
    cv.imwrite("E:/Python_Code/VSC_Python/soldier2.png",img)

#双边模糊（滤波） 
def bi_fliter_demo(img):
    dst=cv.bilateralFilter(img,0,100,15)
    cv.imshow("bi_filiter_demo1",dst)
    dst2=cv.pyrMeanShiftFiltering(img,10,50)
    cv.imshow("bi_filiter_demo2",dst2)

img=cv.imread("E:/Python_Code/VSC_Python/soldier.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
#blur_mean_demo(img)
#blue_median_demo(img)
#custom_blur_demo(img)
gaussian_noise(img)

#dst=cv.GaussianBlur(img,(5,5),0)  #高斯平滑滤波器 降低(高斯)噪
#cv.imshow("Gaussian_filter_img",dst)
bi_fliter_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()