import cv2
import numpy
import math

def nothing(x):
    pass


pathImg = "./lab7/7_1.jpg"
winName = "Test Window"

cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
img = cv2.imread(pathImg, flags=cv2.IMREAD_GRAYSCALE)
img_c = cv2.imread(pathImg, flags=cv2.IMREAD_COLOR)
height, weight = img.shape[0:2]
img = cv2.resize(img, (int(height*0.5), int(weight*0.5)))
img_c = cv2.resize(img_c, (int(height*0.5), int(weight*0.5)))


grad_x = cv2.Sobel(img,  ddepth=0, dx=1, dy=0, ksize=3, scale=1, delta=0)
grad_y = cv2.Sobel(img,  ddepth=0, dx=0, dy=1, ksize=3, scale=1, delta=0)
new_img = grad_x+grad_y


new_img = cv2.morphologyEx(new_img, cv2.MORPH_CLOSE, kernel=numpy.ones((1, 1), dtype=int),
                           anchor=(-1, -1),
                           iterations=1,
                           borderType=cv2.BORDER_CONSTANT, borderValue=(
                               255, 255, 255),
                           )

cv2.createTrackbar("rho_res", winName, 7, 20, nothing)
cv2.createTrackbar("theta_res", winName, 0, 358, nothing)
cv2.createTrackbar("threshold", winName, 6, 20, nothing)
while (1):
    rho_res = 0.1+cv2.getTrackbarPos("rho_res", winName)/10
    theta_res = math.pi/(2+cv2.getTrackbarPos("theta_res", winName))
    threshold = (1+cv2.getTrackbarPos("threshold", winName))*50

    lines = cv2.HoughLines(
        new_img,  # входное изображение
        rho_res,  # разрешение по расстоянию
        theta_res,  # разрешение по углу
        threshold,  # значение аккумулятора
        min_theta=None,  # ограничение угла
        max_theta=None  # ограничение угла
    )
    img_c_n = img_c.copy()
    for line in lines:
        rho = line[0][0]
        theta = line[0][1]
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        x0 = cos_t * rho
        y0 = sin_t * rho
        pt1 = int(x0 - 1000*sin_t), int(y0 - 1000*cos_t)
        pt2 = int(x0 + 1000*sin_t), int(y0 + 1000*cos_t)
        cv2.line(img_c_n, pt1, pt2, (255,255,255), 10, cv2.LINE_AA)


    cv2.imshow(winName, img_c_n)
    key = cv2.waitKey(100)
    if key == 27:break
