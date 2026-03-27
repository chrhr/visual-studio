import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('sign.png', cv.IMREAD_UNCHANGED)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
t, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.imshow(bin_img, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b=bin_img[bin_img.shape[0]//2:bin_img.shape[0], 0:bin_img.shape[0]//2+1]
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

se = np.uint8([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
])

# 팽창
b_dilation=cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 침식
b_erosion=cv.erode(b, se, iterations=1)
plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 열림
b_opening = cv.dilate(b_erosion, se, iterations=1)
plt.imshow(b_opening, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 닫기
b_closing=cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)
plt.imshow(b_closing, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()