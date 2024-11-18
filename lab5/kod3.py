import cv2
import numpy


def nothing(x):
    pass


pathVideo1 = "./lab5/stop_line_1.mp4"
pathVideo2 = "./lab5/stop_line_2.mp4"

cap = cv2.VideoCapture(pathVideo2)

winName = "test_window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

# cv2.createTrackbar("threshold1", winName, 0, 100, nothing)
# cv2.createTrackbar("threshold2", winName, 0, 200, nothing)
# cv2.createTrackbar("size", winName, 0, 100, nothing)

cv2.createTrackbar("size", winName, 0, 10, nothing)
cv2.createTrackbar("iterations", winName, 0, 10, nothing)
# cv2.createTrackbar("type", winName, 0, 4, nothing)
i = 1
my_type = ["OPEN", "CLOSE"]
morph_type = [cv2.MORPH_OPEN, cv2.MORPH_CLOSE,
              cv2.MORPH_GRADIENT, cv2.MORPH_TOPHAT, cv2.MORPH_BLACKHAT]
p = 1
while 1:
    if p == 1:
        ret, frame = cap.read()

    threshold1 = 120 #cv2.getTrackbarPos("threshold1", winName)
    threshold2 = 250 #cv2.getTrackbarPos("threshold2", winName)
    size = 4 #cv2.getTrackbarPos("size", winName)
    # if frame is read correctly ret is True
    size_1 = 2 #cv2.getTrackbarPos("size", winName)+1
    iter_1 = 7 #cv2.getTrackbarPos("iterations", winName)+1
   
    size = 3 #cv2.getTrackbarPos("size", winName)+1
    iter = 0 #cv2.getTrackbarPos("iterations", winName)+1
    t = 0 #cv2.getTrackbarPos("type", winName)
    
    img_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_new = cv2.medianBlur(img_new, size*2+1)
    threshold_new, img_new = cv2.threshold(img_new, 120, 255, cv2.THRESH_BINARY)  
    
    
    img_new = cv2.dilate(
                    img_new,
                    kernel=numpy.ones((size_1, size_1), dtype=int),
                    # kernel = ker,
                    anchor=(-1, -1),
                    iterations=iter_1,
                    borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    
    img_new = cv2.morphologyEx(img_new, morph_type[t], kernel=numpy.ones((size, size), dtype=int),
                                 anchor=(-1, -1),
                                 iterations=iter,
                                 borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255),
                                 )
    
    img_new = cv2.Canny(img_new, threshold1, threshold2)
    # img_new = cv2.Laplacian(img_new, cv2.CV_8U, ksize=5, scale=1,delta=0, borderType=cv2.BORDER_DEFAULT)
    # img_new = cv2.Sobel(img_new,  ddepth=0,dx=0, dy=1,ksize=3,scale=1, delta=0, borderType=cv2.BORDER_DEFAULT ) 


    cv2.imshow(winName, img_new)
    key = cv2.waitKey(100)
    if key == 32: p=1-p
    if key == 27:
        break
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

cap.release()
cv2.destroyAllWindows()
