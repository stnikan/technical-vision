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

cv2.createTrackbar("size", winName, 0, 10, nothing)
# cv2.createTrackbar("iterations", winName, 0, 10, nothing)
morph_type = [cv2.MORPH_OPEN, cv2.MORPH_CLOSE,
              cv2.MORPH_GRADIENT, cv2.MORPH_TOPHAT, cv2.MORPH_BLACKHAT]

i = 0
while 1:
    
    
    # size = cv2.getTrackbarPos("size", winName)
    # img_new = cv2.medianBlur(img[i], size*2+1)  
    # edges = cv2.Canny(img_new,threshold1,threshold2)

    threshold1 = cv2.getTrackbarPos("threshold1", winName)
    threshold2 = cv2.getTrackbarPos("threshold2", winName)
    size = 4 #cv2.getTrackbarPos("size", winName)
    # if frame is read correctly ret is True
    size = cv2.getTrackbarPos("size", winName)+1
    iter_1 = 7 #cv2.getTrackbarPos("iterations", winName)+1
   
    # size = 3 #cv2.getTrackbarPos("size", winName)+1
    # iter = 0 #cv2.getTrackbarPos("iterations", winName)+1
    t = 0 #cv2.getTrackbarPos("type", winName)
    
    # img_new = cv2.cvtColor(img[i], cv2.COLOR_BGR2GRAY)
    img_new = cv2.medianBlur(img[i], size*2+1)
    # threshold_new, img_new = cv2.threshold(img_new, 120, 255, cv2.THRESH_BINARY)  
    
    
    # img_new = cv2.dilate(
    #                 img_new,
    #                 kernel=numpy.ones((size_1, size_1), dtype=int),
    #                 # kernel = ker,
    #                 anchor=(-1, -1),
    #                 iterations=iter_1,
    #                 borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    
    # img_new = cv2.morphologyEx(img_new, morph_type[t], kernel=numpy.ones((size, size), dtype=int),
    #                              anchor=(-1, -1),
    #                              iterations=iter,
    #                              borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255),
    #                              )
    
    img_new = cv2.Canny(img_new, threshold1, threshold2)

    cv2.imshow(winName, img_new)
    key = cv2.waitKey(10)
    if key==27:break
    if key == 32: i=(i+1)%2

cv2.destroyAllWindows()
