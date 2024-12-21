import cv2
import numpy


def nothing(x):
    pass


def my_func(type, img, size, iterations):
    if type == "OPEN":
        img_new = cv2.dilate(
            cv2.erode(
                img,
                kernel=numpy.ones((size, size), dtype=int),
                # kernel = ker,
                anchor=(-1, -1),
                iterations=iterations,
                borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)),
            kernel=numpy.ones((size, size), dtype=int),
            # kernel = ker,
            anchor=(-1, -1),
            iterations=iterations,
            borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    elif type == "CLOSE":
        img_new = cv2.erode(
                cv2.dilate(
                    img,
                    kernel=numpy.ones((size, size), dtype=int),
                    # kernel = ker,
                    anchor=(-1, -1),
                    iterations=iterations,
                    borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)),
            kernel=numpy.ones((size, size), dtype=int),
            # kernel = ker,
            anchor=(-1, -1),
            iterations=iterations,
            borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    else:
        img_new = img
        print("error")
    return img_new


pathImg1 = "./lab4/4-1.jpg"
pathImg2 = "./lab4/4-2.jpg"
# pathTestImg = "./lab4/test2.jpeg"
winName = "test_window"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img = cv2.imread(pathImg1, flags=cv2.IMREAD_COLOR)

cv2.createTrackbar("size", winName, 0, 10, nothing)
cv2.createTrackbar("iterations", winName, 0, 10, nothing)
cv2.createTrackbar("type", winName, 0, 1, nothing)
i = 1
my_type = ["OPEN", "CLOSE"]
morph_type = [cv2.MORPH_OPEN, cv2.MORPH_CLOSE,
              cv2.MORPH_GRADIENT, cv2.MORPH_TOPHAT, cv2.MORPH_BLACKHAT]
while 1:
    # ker = numpy.full((7,7), 1)
    size = cv2.getTrackbarPos("size", winName)+1
    iter = cv2.getTrackbarPos("iterations", winName)+1
    t = cv2.getTrackbarPos("type", winName)
    img_new = my_func(my_type[t], img, size, iter)
    img_new_2 = cv2.morphologyEx(img, morph_type[t], kernel=numpy.ones((size, size), dtype=int),
                                 anchor=(-1, -1),
                                 iterations=iter,
                                 borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255),
                                 )
    img_new -=img_new_2
    cv2.imshow(winName, img_new)
    key = cv2.waitKey(100)
    if key == 27:
        break
