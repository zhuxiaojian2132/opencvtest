import cv2 as cv
import numpy as np  

def access_pixels(img):
    print(img.shape)
    height=img.shape[0]
    width =img.shape[1]
    channels=img.shape[2]
    print("width:%s,height: %s channels：%s"%(width,height,channels))
    # for row in range(height):
    #     for col in range(width):
    #         for c in range(channels):
    #             pv=img[row,col,c]
    #             img[row,col,c]=255-pv

    #img=255-img
    img=cv.bitwise_not(img) #调用内置的c代码
    cv.imshow("pixels_demo",img)

def create_img():
    img=np.zeros([200,200,3],np.uint8) #指定类型创建三通道的图像数据
    img[:,:,1]=np.ones([200,200])*255
    cv.imshow("new image",img)

    img2=img.reshape([40,1000,3])
    cv.imshow("reshape image",img2)

img=cv.imread("D:/Python_Code/VSC_Python/view.jpg")
cv.imshow("input image",img)
t1=cv.getTickCount()
#access_pixels(img)
create_img()
t2=cv.getTickCount()
print("time:%s ms"%((t2-t1)/cv.getTickFrequency()*1000))
cv.waitKey(0)