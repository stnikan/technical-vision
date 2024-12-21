
import cv2
import numpy


def nothing(x):
    pass


pathImg1 = "./lab3/3-4.jpg"

winName = "Border"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

img1 = cv2.imread(pathImg1, flags=cv2.IMREAD_COLOR)

height, weight = img1.shape[0:2]

All_border = [cv2.BORDER_CONSTANT, cv2.BORDER_DEFAULT, cv2.BORDER_ISOLATED, cv2.BORDER_REFLECT,
              cv2.BORDER_REFLECT101, cv2.BORDER_REFLECT_101, cv2.BORDER_REPLICATE,  cv2.BORDER_WRAP]
All_border_name = ["cv2.BORDER_CONSTANT", "cv2.BORDER_DEFAULT", "cv2.BORDER_ISOLATED", "cv2.BORDER_REFLECT",
              "cv2.BORDER_REFLECT101", "cv2.BORDER_REFLECT_101", "cv2.BORDER_REPLICATE",  "cv2.BORDER_WRAP"]

cv2.createTrackbar("border", winName, 0, len(All_border)-1, nothing)
cv2.createTrackbar("top", winName, 0, 200, nothing)
cv2.createTrackbar("bot", winName, 0, 200, nothing)
cv2.createTrackbar("left", winName, 0, 200, nothing)
cv2.createTrackbar("right", winName, 0, 200, nothing)

while (1):
    top = cv2.getTrackbarPos("top", winName)
    bottom = cv2.getTrackbarPos("bot", winName)
    left = cv2.getTrackbarPos("left", winName)
    right = cv2.getTrackbarPos("right", winName)
    border = cv2.getTrackbarPos("border", winName)
    img_new = cv2.copyMakeBorder(
        img1,  # входное изображение
        top,  # пиксели сверху
        bottom,  # пиксели снизу
        left,  # пиксели слева
        right,  # пиксели справа
        borderType=All_border[border] # тип рамки
        

    )
    color_text = (0,0,255)
    cv2.putText(img_new, "top "+str(top) + "  bottom " + str(bottom), (weight-1500, height-800),
                cv2.FONT_HERSHEY_DUPLEX, fontScale=5, color=color_text, thickness=10)
    cv2.putText(img_new, "left "+str(left) + "  right " + str(right), (weight-1500, height-600),
                cv2.FONT_HERSHEY_DUPLEX, fontScale=5, color=color_text, thickness=10)
    cv2.putText(img_new, All_border_name[border], (weight-1500, height-400),
                cv2.FONT_HERSHEY_DUPLEX, fontScale=4, color=color_text, thickness=10)
    cv2.imshow(winName, img_new)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyWindow(winName)
