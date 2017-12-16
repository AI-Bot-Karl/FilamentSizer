import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL

img = cv2.imread('Data/straight_Line_150.png',0)
edges = cv2.Canny(img,100,200)


print(img.size)
print(edges.size)

cv2.
