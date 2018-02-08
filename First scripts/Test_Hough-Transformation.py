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

# linesp = cv2.HoughLinesP(edges, 1, np.pi/180, 200)
# print(linesp)
# if linesp is not None:
#     for i in range(0, len(linesp)):
#         l = linesp[i][0]
#         cv2.line(img_det, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)

thres = 1
lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
while len(lines) > 2:
    thres += 1
    lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
    print(len(lines), end='', flush=True)
    print(thres)
print(lines)
if lines is not None:
    for i in range(0, len(lines)):
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            print(a)
            print(b)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 2000 * (-b))
            y1 = int(y0 + 2000 * (a))
            x2 = int(x0 - 2000 * (-b))
            y2 = int(y0 - 2000 * (a))

            cv2.line(img_det, (x1, y1), (x2, y2), (255, 0, 0), 2)

# print images to screen
plt.subplot(2, 2, 1), plt.imshow(img), plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(edges, cmap='Greys'), plt.title('Edges')
plt.subplot(2, 2, 3), plt.imshow(img_det), plt.title('Detected lines')
plt.show()

cv2.imwrite('houghlines3.jpg', img)
