import cv2 as cv
import numpy as np


img=cv.imread("D:/Python_Code/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)

cv.waitKey(0)
cv.destroyAllWindows()