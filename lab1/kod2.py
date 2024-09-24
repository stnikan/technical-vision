import cv2
import numpy as np

weight,height = 405,720
winName = "test_window"
cv2.namedWindow(winName)



res = np.full(
(weight, height,3), # размер массива
(255,255,255), # значение для заполнения
dtype=np.uint8, # тип данных
order='C', # тип хранения многомерных данных
) 

cv2.circle(res, (200,100), 90, (0,0,255))
cv2.putText(res, "Circle", (110,210), cv2.FONT_ITALIC, fontScale=1 , color = (0,0,0))

cv2.rectangle(res,(50,50),(300,300),(128,0,128)) #BGR
cv2.putText(res, "Rectangle", (50,310), cv2.FONT_HERSHEY_PLAIN, fontScale=0.5 , color = (0,0,0))

h, w = res.shape[0:2]
cv2.line(res,(w,0),(0,h),(255, 191, 0))
cv2.putText(res, "line", (w//2, h//2+20), cv2.FONT_HERSHEY_PLAIN, fontScale=2 , color = (0,0,0))

cv2.imshow(winName, res) 
key = cv2.waitKey() 
