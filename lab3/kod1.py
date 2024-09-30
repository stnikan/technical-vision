import cv2
import numpy


pathImg1 = "./lab3/3-1.PNG"
pathImg2 = "./lab3/3-2.PNG"
winName = "Test window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
img1 = cv2.imread(
    pathImg1, flags=cv2.IMREAD_COLOR)
img2 = cv2.imread(
    pathImg2, flags=cv2.IMREAD_GRAYSCALE)
img_new = cv2.blur(
    img1,
    (10,10),  # размер ядра
    anchor = (9,9),  # положение якорной точки
    borderType=cv2.BORDER_CONSTANT,  # тип рамки
)
cv2.imshow(winName, img_new)
key = cv2.waitKey()
"""
img_new = cv2.boxFilter(
    img,  # входное изображение
    ddepth,  # глубина изображения-результата
    ksize,  # размер ядра
    anchor,  # положение якорной точки
    normalize,  # нормирование (если True)
    bType  # тип рамки
)

img_new = cv2.medianBlur(
    img,  # входное изображение
    ksize  # размер ядра
)

img_new = cv2.GaussianBlur(
    img,  # входное изображение
    ksize,  # размер ядра
    sigmaX,  # сигма по оси X
    sigmaY,  # сигма по оси Y
    bType  # тип рамки
)

img_new = cv2. bilateralFilter(
    img,  # входное изображение
    d,  # размер окрестности пикселя
    sigmaColor,  # ширина второго компонента весовой функции
    sigmaSpace,  # ширина первого компонента весовой функции
    bType  # тип рамки
)
"""