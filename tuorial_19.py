import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as  tess

def recognize_text(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(1,4))
    open_out=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    open_out=cv.morphologyEx(open_out,cv.MORPH_OPEN,kernel,iterations=2)
    # kernel=cv.getStructuringElement(cv.MORPH_RECT,(2,2))
    # open_out=cv.dilate(open_out,kernel)
    cv.imshow("binary_img",open_out)

    cv.bitwise_not(open_out,open_out)
    textImage=Image.fromarray(open_out)
    text=tess.image_to_string(textImage)
    print("验证码为：%s"%text)


img=cv.imread("E:/github_repository/VSC_Python/validate1.JPG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
recognize_text(img)

cv.waitKey(0)
cv.destroyAllWindows()