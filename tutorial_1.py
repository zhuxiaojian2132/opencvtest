import cv2 as cv
import numpy as np

def get_image_info(img):
    print(type(img))
    print(img.shape)
    print(img.size)  
    print(img.dtype)
    pixel_data=np.array(img) #转成np中数组形式
    print(pixel_data)  

def  video_demo():
    #打开对应视频文件
    capture=cv.VideoCapture("E:/Python_Code/VSC_Python/VID_20181226.mp4") # 0-3 代表摄像头，也可以加视频文件
    while(True):
        ret,frame=capture.read()
        frame=cv.flip(frame,-1) #水平镜像-1  上下镜像-0   对角镜像- -1 
        frame=np.rot90(frame)  #旋转90
        cv.imshow("video",frame)  
        c=cv.waitKey(50)  #50毫秒间隔的刷新图像
        if c==27:  #escp
            break
#加载图像
img=cv.imread("E:/Python_Code/VSC_Python/view.jpg")
#开启一个窗口
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#窗口中显示图像
cv.imshow("input image",img)
get_image_info(img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite("E:/Python_Code/VSC_Python/view2.png",gray)
video_demo()
cv.waitKey(0)
#关闭窗口
cv.destroyAllWindows()
