import cv2
import numpy

path = "./lab1/im_1.jpg"
winName = "test_window"
cv2.namedWindow(winName)
img = cv2.imread(path, # путь до изображения
    flags=cv2.IMREAD_COLOR) # параметр(ы) чтения

height, weight= img.shape[0:2]

while (1):
    img1 = img

    cv2.imshow(winName, img1) 
    key = cv2.waitKey(5000) 
    if key==27:break

    img2=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow(winName, img2) 
    key = cv2.waitKey(7000) 
    if key==27:break
    

    img3 = cv2.resize(img, (height//2,weight//2))
    cv2.imshow(winName, img3) 
    key = cv2.waitKey(9000) 
    if key==27:break

    img4 = cv2.cvtColor(cv2.resize(img, (height//4,weight//4)),cv2.COLOR_RGB2GRAY)
    cv2.imshow(winName, img4) 
    key = cv2.waitKey(11000) 
    if key==27:break

    b, g, r = cv2.split(img)
    img5 = cv2.merge([b, r, g])
    cv2.imshow(winName, img5) 
    key = cv2.waitKey(4000) 
    if key==27:break