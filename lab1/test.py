f = open('text.py', 'w')
a = 10
f.write("import cv2"+ '\n')
f.write("import numpy as np"+ '\n')
f.write("weight,height = 150,400"+ '\n')
f.write("a = 10"+ '\n')
f.write('winName = "test_window"'+ '\n')
f.write("cv2.namedWindow(winName)"+ '\n')
f.write("res = np.full((weight, height,3),(255,255,255),dtype=np.uint8,order='C',)" + '\n')

for i in range(0,15):
    for j in range(0,40):
        if (j%2 + i%2)%2 == 0:
            st = "cv2.rectangle(res,("+str(j*a)+","+str(i*a)+"),("+str(j*a+a)+","+str(i*a+a)+"),(128,0,128),thickness=-1)"
            #print(st)
            f.write(st + '\n')
f.write("cv2.imshow(winName, res)"+ '\n'+"key = cv2.waitKey(5000)"+ '\n')
f.close()
