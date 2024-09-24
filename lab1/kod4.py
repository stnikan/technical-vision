import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
my_data = datetime.datetime.now().strftime('%d-%m-%Y')
print("Для завершения работы программы нажмите Esc")
print("Для сохранения текущего кадра нажмите z")
frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
height, weight= frame.shape[0:2]
while 1:
    frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    cv2.putText(frame, my_data, (weight-240,height-20), cv2.FONT_ITALIC, fontScale=1 , color = (255,255,255))
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key==122:
        res = cv2.imwrite("my_screen.jpg",frame)
    
    if key == 27:
        break