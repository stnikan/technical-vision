import cv2
import numpy


def nothing(x):
    pass


path = "./lab2/2-0.jpg"
winName = "test_window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_EXPANDED)

img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)

height, weight = img.shape[0:2]

cv2.imshow(winName, img)
key = cv2.waitKey()
###################################################################
#блок ручного пооиска
"""threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY) #ручной поиск птиц
cv2.imshow(winName, new_img) 
key = cv2.waitKey() 

threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY_INV) #ручной поиск фона
cv2.imshow(winName, new_img) 
key = cv2.waitKey() """
#конец ручного поиска
###################################################################

###################################################################
# адаптивный поиск
cv2.createTrackbar("polzunok", winName, 60, 200, nothing)
cv2.createTrackbar("polzunok2", winName, 90, 100, nothing)
""""
while (1):
    par = cv2.getTrackbarPos('polzunok', winName)
    par2 = cv2.getTrackbarPos('polzunok2', winName)
    adaptive_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, par2*2+1 , par)
    cv2.imshow(winName, adaptive_img)
    key = cv2.waitKey(100)
    if key == 32:
        break

dst = cv2.add(img,adaptive_img)
cv2.imshow(winName, dst)
key = cv2.waitKey()"""
#конец адаптивного поиска
###################################################################

###################################################################
#автоматический поиск


#конец автоматического поиска
###################################################################