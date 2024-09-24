import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
print
while 1:
    frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    #cv2.putText(frame, datetime.datetime.now().strftime('%d-%m-%Y'), (0,0), cv2.FONT_ITALIC, fontScale=1 , color = (0,0,255))
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key==122:
        res = cv2.imwrite("my_screen.jpg",frame)

    if key == 27:
        break