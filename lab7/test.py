import cv2
import numpy as np

# Шаг 1: Загрузите изображение
image = cv2.imread('./lab7/7_5_1.jpg')

# Шаг 2: Преобразуйте изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Шаг 3: Примените размытие, чтобы уменьшить шум
gray = cv2.medianBlur(gray, 5)

# Шаг 4: Примените метод HoughCircles для поиска кругов
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=5,
    maxRadius=100
)

# Шаг 5: Если круги найдены, нарисуйте их на исходном изображении
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Рисуем внешний круг
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Рисуем центр круга
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

# Шаг 6: Покажите изображение с обнаруженными кругами
cv2.imshow('Detected Circles', image)
cv2.waitKey()
cv2.destroyAllWindows()