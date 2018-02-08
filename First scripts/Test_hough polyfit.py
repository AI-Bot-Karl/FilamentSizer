import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from copy import deepcopy

# loading image and converting to grayscale:
img = cv2.imread('Data/straight_Line_150.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# alternatively:
# img = cv2.imread('Data/straight_Line_150.png',0)
im = Image.fromarray(img)

print(img.size)


# edge detection and denoise
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper, cv2.CV_64F, 5, True)

    # return the edged image
    return edged


edges = auto_canny(img)
# edges =  cv2.Canny(gray, 10, 20, cv2.CV_64F,5, True)

# deepcopy because of pointer/real copy problem
# img_det =deepcopy(img)
img_det = np.copy(img)

print('im')
print(im)
print('img')
print(img)
print('gray')
print(gray)
print('edge')
print(edges)
plt.subplot(2, 2, 1), plt.imshow(img), plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(gray, cmap='gray'), plt.title('gray')
plt.subplot(2, 2, 3), plt.imshow(edges, cmap='gray'), plt.title('Edges')
plt.subplot(2, 2, 4), plt.imshow(im), plt.title('im')
plt.show()

# search biggest accumulation of 1's in horiz. slices of the binary image and definae a window.
Hist = cv2.calcHist([edges], channels=[0], mask=None, histSize=256, ranges=[0, 255])
print(Hist)

# identify the nonzero pixels in x and y within the window and fit a second order polynomial to each line
