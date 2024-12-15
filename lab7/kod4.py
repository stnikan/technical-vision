import cv2
import numpy
import math

def nothing(x):
    pass


pathImg1 = "./lab7/7_5_1.jpg"
pathImg2 = "./lab7/7_5_2.jpg"
pathImg3 = "./lab7/7_5_3.jpg"
pathImg4 = "./lab7/7_5_4.jpg"
pathImg5 = "./lab7/7_5_5.jpg"
pathImg6 = "./lab7/7_5_6.jpg"
winName = "Test Window"

# cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

path = [pathImg1,pathImg2,pathImg3,pathImg4,pathImg5,pathImg6]
images = list()
images_color = list()
for p in path:
    images_color.append(cv2.imread(p, flags=cv2.IMREAD_COLOR))
    images.append(cv2.cvtColor(images_color[-1], cv2.COLOR_BGR2GRAY))
img_filtr = list()
for img in images:
    img_filtr.append(cv2.medianBlur(img, 25))
circleInImg = list()
new_img = list()
for img in img_filtr:
    circleInImg.append(cv2.HoughCircles(img, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 100, param1 = 275, param2 = 400, minRadius = 0, maxRadius = 0))

for i in range(len(images)):
    new_img.append(cv2.cvtColor(images[i], cv2.COLOR_GRAY2RGB))
    if not (circleInImg[i] is None):
        for j in range(0,circleInImg[i].shape[1]):
            x = int(circleInImg[i][0][j][0])
            y = int(circleInImg[i][0][j][1])
            R = int(circleInImg[i][0][j][2])

            
            cv2.circle(new_img[i], center = (x, y), radius = R, color = (0, 0, 255), thickness = 5, lineType = cv2.LINE_8)

    

k = 0

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
while (1):
    cv2.imshow(winName, new_img[k])
    key = cv2.waitKey(100)
    if key == 27:break
    if key == 32: k = (k+1)%6


