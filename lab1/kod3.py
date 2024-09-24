import cv2
import numpy as np

weight,height = 150,400
a = 10
winName = "test_window"
cv2.namedWindow(winName)



res = np.full((weight, height,3),(255,255,255),dtype=np.uint8,order='C',) 

for i in range(0,15):
    for j in range(0,40):
        if (j%2 + i%2)%2 == 0:
            cv2.rectangle(res,(j*a,i*a),(j*a+a,i*a+a),(128,0,128),thickness=-1)
        


cv2.imshow(winName, res) 
key = cv2.waitKey() 