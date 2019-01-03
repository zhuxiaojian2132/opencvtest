import cv2 as cv
import numpy as np
#利用opencv中harr级联器来检测人脸
def face_detect_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detector=cv.CascadeClassifier("E:/github_repository/VSC_Python/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces=face_detector.detectMultiScale(gray,1.02,3)
    print(faces)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",img)

# img=cv.imread("E:/github_repository/VSC_Python/lena.jpg")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",img)
# face_detect_demo(img)

#视频检测人脸
capture=cv.VideoCapture("E:/github_repository/VSC_Python/VID_20190103.mp4") 
cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
while(True):
    ret,frame=capture.read()
    frame=cv.flip(frame,1) #水平镜像-1  上下镜像-0   对角镜像- -1 
    face_detect_demo(frame) 
    c=cv.waitKey(10)  #50毫秒间隔的刷新图像
    if c==27:  #escp
        break
cv.waitKey(0)
cv.destroyAllWindows()