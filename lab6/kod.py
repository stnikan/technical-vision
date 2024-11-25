import cv2
import numpy


def nothing(x):
    pass


pathImg = "./lab6/6-1.PNG"
winName = "Test Window"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)
img = cv2.resize(cv2.imread(pathImg, flags=cv2.IMREAD_GRAYSCALE), (1920, 1080))
threshold_new, new_img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
new_img = cv2.morphologyEx(new_img, cv2.MORPH_BLACKHAT, kernel=numpy.ones((10, 10), dtype=int),
                           anchor=(-1, -1),
                           iterations=6,
                           borderType=cv2.BORDER_CONSTANT, borderValue=(
                               255, 255, 255),
                           )

contours, hierarchy = cv2.findContours(
    new_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)
img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

for i in range(0, len(contours)):
    area = cv2.contourArea(contours[i])
    c, r = cv2.minEnclosingCircle(contours[i])
    s = 3.14*r**2
    if area < s*1.05 and area > s*0.95:
        cv2.drawContours(
            img2,  # исходное изображение
            contours,  # список контуров
            i,  # индекс контура для рисования
            (255, 0, 0),  # цвет для рисования
            5,  # толщина линии для рисования
            cv2.LINE_4  # тип линии для рисования
        )
    s = 2*r**2
    if area < s*1.05 and area > s*0.95:
        cv2.drawContours(
            img2,  # исходное изображение
            contours,  # список контуров
            i,  # индекс контура для рисования
            (0, 255, 0),  # цвет для рисования
            5,  # толщина линии для рисования
            cv2.LINE_4  # тип линии для рисования
        )
    x,y = c
    # cv2.circle(img2, (int(x),int(y)), int(r), (1,255,255))
    len = cv2. arcLength(
        contours[i],  # контур
        closed=False  # замкнутый или нет
    )
    s = (3*(3**0.5)*r**2)/4
    if area < s*1.05 and area > s*0.95:
        cv2.drawContours(
            img2,  # исходное изображение
            contours,  # список контуров
            i,  # индекс контура для рисования
            (0, 0, 255),  # цвет для рисования
            5,  # толщина линии для рисования
            cv2.LINE_4  # тип линии для рисования
        )


# cv2.drawContours(
#     img2,  # исходное изображение
#     contours,  # список контуров
#     -1,  # индекс контура для рисования
#     (255, 0, 0),  # цвет для рисования
#     1,  # толщина линии для рисования
#     cv2.LINE_4  # тип линии для рисования
# )
cv2.imshow(winName, img2)
key = cv2.waitKey()
