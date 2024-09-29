import cv2
import numpy


def nothing(x):
    pass


pathBerd = "./lab2/2-0.jpg"
pathHuman = "./lab2/2-1.jpg"
pathZebra = "./lab2/2-2.jpg"
pathText = "./lab2/2-3.PNG"
pathMoumt = "./lab2/2-4.png"

winNameHand = "Hand"
winNameAdaptive = "Adaptive"
winNameAuto = "Auto"
winName = "Test Window"

cv2.namedWindow(winName, cv2.WINDOW_GUI_NORMAL)

imgBerd = cv2.imread(pathBerd, flags=cv2.IMREAD_GRAYSCALE)
imgHuman = cv2.imread(pathHuman, flags=cv2.IMREAD_GRAYSCALE)
imgZebra = cv2.imread(pathZebra, flags=cv2.IMREAD_GRAYSCALE)
imgText = cv2.imread(pathText, flags=cv2.IMREAD_GRAYSCALE)
imgMount = cv2.imread(pathMoumt, flags=cv2.IMREAD_GRAYSCALE)

cap = cv2.VideoCapture(0)

#height, weight = img.shape[0:2] буду определеять по мере надобности???


###################################################################

###################################################################
# блок ручного пооиска
"""threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY) #ручной поиск птиц
cv2.imshow(winName, new_img) 
key = cv2.waitKey() 

threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY_INV) #ручной поиск фона
cv2.imshow(winName, new_img) 
key = cv2.waitKey() """
# конец ручного поиска
###################################################################

###################################################################
# адаптивный поиск
# cv2.createTrackbar("polzunok", winName, 60, 200, nothing)
# cv2.createTrackbar("polzunok2", winName, 90, 100, nothing)
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
# конец адаптивного поиска
###################################################################

###################################################################
# автоматический поиск
ThresholdType = ["Ручной","Адаптивный", "Авто"]
method = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TOZERO,
          cv2.THRESH_TOZERO_INV, cv2.THRESH_TRUNC, cv2.THRESH_OTSU, cv2.THRESH_TRIANGLE]
methodName = ["cv2.THRESH_BINARY", "cv2.THRESH_BINARY_INV", "cv2.THRESH_TOZERO",
              "cv2.THRESH_TOZERO_INV", "cv2.THRESH_TRUNC", "cv2.THRESH_OTSU", "cv2.THRESH_TRIANGLE"]

'''
cv2.createTrackbar("type of conversion", winName, 0, 3, nothing)
cv2.createTrackbar("polzunok", winName, 0, 6, nothing)
cv2.createTrackbar("polzunok", winName, 0, 6, nothing)
cv2.createTrackbar("polzunok2", winName, 0, 255, nothing)

while (1):
    par = cv2.getTrackbarPos('polzunok', winName)
    par2 = cv2.getTrackbarPos('polzunok2', winName)
    threshold_new, new_img = cv2.threshold(img,  par2, 255,  method[par])

    new_img = cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)

    cv2.putText(new_img, methodName[par], (weight-1040, height-200),
                cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(126, 0, 255), thickness=5)
    cv2.putText(new_img, str(threshold_new), (weight-240, height-100),
                cv2.FONT_HERSHEY_DUPLEX, fontScale=2, color=(126, 0, 255), thickness=5)

    cv2.imshow(winName, new_img)
    key = cv2.waitKey(10)
    if key == 27:
        break

# threshold_new, new_img = cv2.threshold(img,  255,  cv2.THRESH_BINARY_INV)
# cv2.imshow(winName, new_img)
# key = cv2.waitKey()
# конец автоматического поиска'''
###################################################################


cv2.createTrackbar("img", winName, 0, 5, nothing)
cv2.createTrackbar("conversion", winName, 0, 3, nothing)
cv2.createTrackbar("porog", winName, 0, 255, nothing)

while(1):
    index_img = cv2.getTrackbarPos('img', winName)
    type_Conversion = cv2.getTrackbarPos("conversion", winName)
    if index_img == 0:
        new_img = imgBerd
    elif index_img == 1:
        new_img = imgHuman
    elif index_img == 2:
        new_img = imgZebra
    elif index_img == 3:
        new_img = imgText
    elif index_img == 4:
        new_img = imgMount
    else:
        new_img = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

    if type_Conversion == 0:
        threshold_new, new_img = cv2.threshold(new_img, 19, 255,  cv2.THRESH_BINARY)
    elif type_Conversion == 1:
        new_img = cv2.adaptiveThreshold(new_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 60*2+1 , 90)
    else:
        threshold_new, new_img = cv2.threshold(new_img, 19, 255, cv2.THRESH_OTSU)

    cv2.imshow(winName, new_img)
    key = cv2.waitKey(100)
    if key == 32:break
