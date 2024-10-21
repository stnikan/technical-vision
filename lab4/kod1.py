import cv2
import numpy

pathImg1 = "./lab4/4-1.jpg"
pathImg2 = "./lab4/4-2.jpg"
winName = "test_window"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img = cv2.imread(    pathImg1, flags=cv2.IMREAD_COLOR)
# ker = numpy.full((7,7), 1)
img_new = cv2.dilate(
    img,
    kernel = numpy.ndarray((5, 5), dtype=int),
    # kernel = ker,
    anchor= (-1, -1),
    iterations=1,
    borderType=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
cv2.imshow(winName, img_new)
key = cv2.waitKey(5000)
