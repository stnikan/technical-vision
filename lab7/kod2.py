import cv2
import numpy
import math


def nothing(x):
    pass





pathImg1 = "./lab4/4-1.jpg"
winName = "test_window"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img = cv2.imread(pathImg1, flags=cv2.IMREAD_GRAYSCALE)

cv2.createTrackbar("size", winName, 1, 10, nothing)
cv2.createTrackbar("iterations", winName, 1, 10, nothing)
cv2.createTrackbar("type", winName, 1, 4, nothing)


morph_type = [cv2.MORPH_OPEN, cv2.MORPH_CLOSE,
              cv2.MORPH_GRADIENT, cv2.MORPH_TOPHAT, cv2.MORPH_BLACKHAT]
while 1:
    # ker = numpy.full((7,7), 1)
    size = cv2.getTrackbarPos("size", winName)+1
    iter = cv2.getTrackbarPos("iterations", winName)+1
    t = cv2.getTrackbarPos("type", winName)

    img_new = cv2.morphologyEx(img, morph_type[t], kernel=numpy.ones((size, size), dtype=int),
                               anchor=(-1, -1),
                               iterations=iter,
                               borderType=cv2.BORDER_CONSTANT, borderValue=(
                                   255, 255, 255),
                               )

    # cv2.imshow(winName, img_new)
    # key = cv2.waitKey(100)
    break
    if key == 27:
        break

cv2.destroyWindow(winName)
cv2.namedWindow(winName)
img = img_new.copy()

_, new_img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)

lines = cv2.HoughLinesP(new_img, rho=1, theta=math.pi /180,
                            threshold=50, minLineLength=50, maxLineGap=3)
img2=cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)
# for line in lines:
#     cv2.line(img2, (line[0][0],line[0][1]), (line[0][2],line[0][3]), (255,5,2), 2, cv2.LINE_AA)
# cv2.imshow(winName, img2)
# key = cv2.waitKey(10000)

circles = cv2.HoughCircles(new_img, method=cv2.HOUGH_GRADIENT, dp=2,
                            minDist=20, param1=80, param2=100, minRadius=0, maxRadius=0)
max_R = circles[0][0][2]
max_circle = circles[0][0]
for c in circles[0]:
    if c[2]>max_R:
      max_R = c[2]
      max_circle = c  
x,y,R = int(max_circle[0]),int(max_circle[1]),int(max_circle[2])
cv2.circle(img2, center = (x, y), radius = R, color = (255, 0, 0), thickness = 3, lineType = cv2.LINE_8)

# img2=cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)
max_line = lines[0]
line_len = 0
for line in lines:
    l = ((line[0][0]-line[0][2])**2+(line[0][1]-line[0][3])**2)**0.5
    if line_len <= l:
        max_line = line
        line_len = l
cv2.line(img2, (max_line[0][0],max_line[0][1]), (max_line[0][2],max_line[0][3]), (0,0,255), 5, cv2.LINE_AA)

cv2.imshow(winName, img2)
key = cv2.waitKey(10000)
# print(circles)
# # print(len(circles))
