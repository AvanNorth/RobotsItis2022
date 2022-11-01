import os
import cv2 as cv
import numpy as np

# url to image
url = "default.jpg"
path = ''

image = cv.imread(url)

cv.imshow("Original", image)

# downscale to 300x200
downWidth = 300
downHeight = 200
downPoints = (downWidth, downHeight)
resizedDownImage = cv.resize(image, downPoints, interpolation=cv.INTER_LINEAR)

cv.imshow("Resized down", resizedDownImage)
cv.waitKey()

cv.destroyAllWindows()

# downscaling with different inter
scale_down = 0.7

resInterNear = cv.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv.INTER_NEAREST)
resInterLinear = cv.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv.INTER_LINEAR)
resInterArea = cv.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv.INTER_AREA)

cv.imshow("Near", resInterNear)
cv.imshow("Linear", resInterLinear)
cv.imshow("Area", resInterArea)
cv.waitKey()

imgHeight = resizedDownImage.shape[0]
imgWidth = resizedDownImage.shape[1]
imgCopy = resizedDownImage.copy()

M = 50
N = 100
x1 = 0
y1 = 0

for y in range(0, imgHeight, M):
    for x in range(0, imgWidth, N):
        if (imgHeight - y) < M or (imgWidth - x) < N:
            break

        y1 = y + M
        x1 = x + N

        if x1 >= imgWidth or y1 >= imgHeight:
            print('1st if')
            x1 = imgWidth - 1
            y1 = imgHeight - 1
            tiles = imgCopy[y: y + M, x: x + N]
            if not cv.imwrite(os.path.join(path, 'title' + str(x) + '_' + str(y) + '.jpg'), tiles):
                print("error")
            cv.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 < imgHeight:
            print('elif')
            y1 = imgHeight - 1
            tiles = imgCopy[y: y + M, x: x + N]
            if not cv.imwrite(os.path.join(path, 'title' + str(x) + '_' + str(y) + '.jpg'), tiles):
                print("error")
            cv.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
