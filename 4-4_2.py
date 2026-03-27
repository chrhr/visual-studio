import cv2 as cv
import numpy as np

img = cv.imread('road.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 50, 150) 

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

cv.imshow('Lane Detection', img)

cv.waitKey()
cv.destroyAllWindows()