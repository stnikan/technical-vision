import cv2
import numpy


def nothing(x):
    pass

pathImg1 = "./lab5/5-1.jpg"
pathImg2 = "./lab5/5-2.jpg"
pathImg3 = "./lab5/5-3.jpg"

winName = "Sobel"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img = [cv2.imread(pathImg1, flags=cv2.IMREAD_COLOR),cv2.imread(pathImg2, flags=cv2.IMREAD_COLOR),cv2.imread(pathImg3, flags=cv2.IMREAD_COLOR)]
ddepth = [cv2.CV_64F,cv2.CV_32F, cv2.CV_16F,cv2.CV_16S,cv2.CV_8U]

cv2.createTrackbar("xorder", winName, 0, 2, nothing)
cv2.createTrackbar("yorder", winName, 0, 2, nothing)
i = 0
while 1:
    
    xorder = cv2.getTrackbarPos("xorder", winName)
    yorder = cv2.getTrackbarPos("yorder", winName)
    if xorder+yorder==0:xorder=1
    grad_x = cv2.Sobel(img[i],  ddepth=0,dx=xorder, dy=yorder,ksize=3,scale=1, delta=0, borderType=cv2.BORDER_DEFAULT )
    cv2.imshow(winName, grad_x)
    key = cv2.waitKey(100)
    if key==27:break
    if key == 32: i=(i+1)%3

cv2.destroyAllWindows()
winName = "Laplacian"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
while 1:

    dst = cv2.Laplacian(img[i], cv2.CV_8U, ksize=5, scale=1,delta=0, borderType=cv2.BORDER_DEFAULT) 
    cv2.imshow(winName, dst)
    key = cv2.waitKey(100)
    if key==27:break
    if key == 32: i=(i+1)%3
