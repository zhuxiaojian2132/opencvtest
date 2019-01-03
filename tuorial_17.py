#基于距离变换的分水岭算法
import cv2 as cv
import numpy as np
def watershed_demo(img):
    blurred=cv.pyrMeanShiftFiltering(img,10,100)
    #gray\binary image
    gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    ret,binary= cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    cv.imshow("binary-image",binary)
    # morphology operation
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb=cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sur_bg=cv.dilate(mb,kernel,iterations=3)
    cv.imshow("morph-opt",sur_bg)
    #distance transform
    dist=cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_out=cv.normalize(dist,0,10,cv.NORM_MINMAX)
    cv.imshow("distance-out",dist_out*50)

    ret,surface=cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface-bin",surface)
    surface_fg=np.uint8(surface)
    unknown =cv.subtract(sur_bg,surface_fg)
    ret,markers=cv.connectedComponents(surface_fg)

    #watershed transform
    markers=markers+1
    markers[unknown==255]=0
    markers=cv.watershed(img,markers=markers)
    img[markers==-1]=[0,0,255]
    cv.imshow("result",img)

img=cv.imread("E:/github_repository/VSC_Python/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",img)
watershed_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()