import cv2
import numpy
import math 


def nothing(x):
    pass

morph_type = [cv2.MORPH_OPEN, cv2.MORPH_CLOSE,
              cv2.MORPH_GRADIENT, cv2.MORPH_TOPHAT, cv2.MORPH_BLACKHAT]


pathVideo1 = "./lab5/stop_line_1.mp4"
pathVideo2 = "./lab5/stop_line_2.mp4"

cap = cv2.VideoCapture(pathVideo1)

winName = "test_window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

p = 1
while 1:
    if p == 1:
        ret, frame = cap.read()
    else:
        lines = cv2.HoughLinesP(img_new, rho=1, theta=math.pi /360,
                            threshold=50, minLineLength=50, maxLineGap=6)
        img2=cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)
        
        for line in lines:
            cv2.line(img2, (line[0][0],line[0][1]), (line[0][2],line[0][3]), (255,5,2), 2, cv2.LINE_AA)
        cv2.imshow(winName, img2)
        cv2.waitKey()
        p=1-p
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