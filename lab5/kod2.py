import cv2
import numpy


def nothing(x):
    pass

pathImg1 = "./lab5/5-4.PNG"
pathImg2 = "./lab5/5-5.jpg"


winName = "test_window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img = [cv2.imread(pathImg1, flags=cv2.IMREAD_GRAYSCALE),cv2.imread(pathImg2, flags=cv2.IMREAD_GRAYSCALE)]
ddepth = [cv2.CV_64F,cv2.CV_32F, cv2.CV_16F,cv2.CV_16S,cv2.CV_8U]

cv2.createTrackbar("threshold1", winName, 0, 100, nothing)
cv2.createTrackbar("threshold2", winName, 0, 200, nothing)
i = 0
while 1:
    
    threshold1 = cv2.getTrackbarPos("threshold1", winName)
    threshold2 = cv2.getTrackbarPos("threshold2", winName)

    edges = cv2.Canny(img[i],threshold1,threshold2)

    cv2.imshow(winName, edges)
    key = cv2.waitKey(10)
    if key==27:break
    if key == 32: i=(i+1)%2

cv2.destroyAllWindows()
