import cv2
import numpy


def nothing(x):
    pass


path = "./2-0.jpg"
winName = "test_window"
cv2.namedWindow(winName, cv2.WINDOW_GUI_EXPANDED)

img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)

height, weight = img.shape[0:2]

cv2.imshow(winName, img)
key = cv2.waitKey()

'''threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY) #ручной поиск птиц
cv2.imshow(winName, new_img) 
key = cv2.waitKey() 

threshold_new, new_img = cv2.threshold(img, 19, 255,  cv2.THRESH_BINARY_INV) #ручной поиск фона
cv2.imshow(winName, new_img) 
key = cv2.waitKey() '''

# адаптивный поиск
cv2.createTrackbar("polzunok", winName, 60, 200, nothing)
cv2.createTrackbar("polzunok2", winName, 90, 100, nothing)
while (1):
    par = cv2.getTrackbarPos('polzunok', winName)
    par2 = cv2.getTrackbarPos('polzunok2', winName)
    adaptive_img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, par2*2+1 , par)
    cv2.imshow(winName, adaptive_img)
    key = cv2.waitKey(100)
    if key == 32:
        break

"""new_img = img.copy()
for i in range(len(new_img)):
    for j in range(len(new_img[0])):
        if adaptive_img[i][j] == 255:
            new_img[i][j] = new_img[i][j]
        else:
            new_img[i][j] = 255


cv2.imshow(winName, img)
key = cv2.waitKey()
new_win = "new_window"
cv2.namedWindow(new_win, cv2.WINDOW_GUI_EXPANDED)
cv2.imshow(new_win, new_img)
key = cv2.waitKey()"""

img1 = img
img2 = adaptive_img

brows, bcols = img1.shape[:2]
rows,cols = img2.shape
# Ниже я изменил roi, чтобы картинка выводилась посередине, а не в левом верхнем углу
roi = img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
int(cols/2):int(bcols/2)+int(cols/2) ]

img2gray = img2
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
int(cols/2):int(bcols/2)+int(cols/2) ] = dst
cv2.imwrite('res.jpg',img1)