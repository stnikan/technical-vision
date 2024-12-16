import cv2

path = './Lab8/task.png'

img = cv2.imread(path, flags = cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

_, imgBin = cv2.threshold(img2, 250, 255, type = cv2.THRESH_BINARY)

contours, _ = cv2.findContours(imgBin, mode = cv2.RETR_CCOMP, method = cv2.CHAIN_APPROX_SIMPLE)


pattern = contours[1]
cv2.drawContours(img, contours, contourIdx = 1, color = [255, 255, 0], thickness = 3, lineType = cv2.LINE_8)

patternMoments = cv2.moments(contours[1], binaryImage = False)
patternHuMoments = cv2.HuMoments(patternMoments)
patternm00 = patternMoments['mu20']
patternnu = patternMoments['nu20']
patternnu2 = patternMoments['nu02']
patternm01 = patternMoments['mu02']
patternm10 = patternMoments['mu11']
diff = 1e-3
difference = []
print(patternMoments['mu20'])
for i in range(2, len(contours)):
    Moments = cv2.moments(contours[i], binaryImage = False)
    HuMoments = cv2.HuMoments(Moments)
    momentm00 = Moments['mu20']
    momentnu = Moments['nu20']
    momentnu2 = Moments['nu02']
    momentm01 = Moments['mu02']
    momentm10 = Moments['mu11']

    difference[:] = abs(patternHuMoments[:] - HuMoments[:])

    if (0.95*patternnu <= momentnu <= 1.05*patternnu) & (0.95*patternnu2 <= momentnu2 <= 1.05*patternnu2):
        if not((0.95*patternm00 <= momentm00 <= 1.05*patternm00)): 
            cv2.drawContours(img, contours, contourIdx = i, color = [255, 0, 139], thickness = 3, lineType = cv2.LINE_8)
            print(Moments['mu20'])

winName = "Test Window"

cv2.namedWindow(winName, flags = cv2.WINDOW_GUI_EXPANDED)

cv2.imshow(winName, img)
key = cv2.waitKey()
cv2.destroyAllWindows()