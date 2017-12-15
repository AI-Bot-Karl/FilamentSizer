import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Data/straight_Line_150.png',0)
edges = cv2.Canny(img,100,200)

cv2.imshow('image', img)
cv2.imshow('edges', edges)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()