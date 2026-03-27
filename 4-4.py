import cv2 as cv

img = cv.imread('orange.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

oranges = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 100, param1=30, param2=30,
                          minRadius =10, maxRadius = 50)

for i in oranges[0]:
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]),(255, 0, 0), 2)

cv.imshow('Orange', img)

cv.waitKey()
cv.destroyAllWindows()