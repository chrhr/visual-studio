import cv2 as cv
import numpy as np
import sys

img = cv.imread('dd.jpg')


img = cv.resize(img, dsize=(0,0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

BrushSiz = 12

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN or (event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON):
        
        y1, y2 = y - BrushSiz, y + BrushSiz
        x1, x2 = x - BrushSiz, x + BrushSiz

        gray[y1:y2, x1:x2] = cv.GaussianBlur(gray[y1:y2, x1:x2], (15, 15), 0.0)

        cv.imshow('Painting', gray)

cv.namedWindow('Painting')
cv.imshow('Painting', gray)
cv.setMouseCallback('Painting', painting)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break