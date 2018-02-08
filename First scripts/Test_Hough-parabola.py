import io
import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from copy import deepcopy


#loading image and converting to grayscale:
img = cv2.imread('Data/straight_Line_150.png',0)
im = Image.fromarray(img,'L')

print(img.size)

#edge detection and denoise
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper, cv2.CV_64F,5, True)

	return edged

edges = auto_canny(img)
#edges =  cv2.Canny(gray, 10, 20, cv2.CV_64F,5, True)

#deepcopy because of pointer/real copy problem
#img_det =deepcopy(img)
img_det = np.copy(img)

def HoughParabola(image, pmin, pmax):
    thres = 1
    lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
    while len(lines) > 2:
        thres += 1
        lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
        print(len(lines), end='', flush=True)
        print(thres)
    print(lines)
    if lines is not None:
        ii=0
        X0=[]
        Y0=[]
        for i in range(0, len(lines)):
            for rho, theta in lines[i]:
                a = np.cos(theta)
                b = np.sin(theta)
                print(a)
                print(b)
                x0 = a * rho
                y0 = b * rho
                X0.append(x0)
                Y0.append(y0)
                ii+=1


    vector_p = np.linspace(-pmax, pmax, 100, True)
    vector_phi = np.linspace(0 , 2*np.pi - (2*np.pi/100),100,True)
    Accumulator = np.zeros([len(vector_phi), len(vector_p)])
    [x,y]=np.where(img<255)

    #voting
    for k in range(0,ii):
        centery = Y0[k]
        centerx = X0[k]
        for i in range(0, len(x)):
            for j in range(0,len(vector_phi)):
                #print('.')
                Y= y[i] - centery
                X= x[i] - centerx
                angle=vector_phi[j]
                numerater = (Y*np.cos(angle)-X*np.sin(angle))**2
                denominater = 4*(X*np.cos(angle)+Y*np.sin(angle))
                #print(numerater,denominater)
                if denominater is not 0:
                    p=numerater/denominater

                    if np.abs(p)>pmin and np.abs(p)<pmax and p is not 0:
                        indice = np.where(vector_p >=p)
                        indice = indice[0]
                        Accumulator[j,indice]= Accumulator[j,indice]+1

    #finding local maxima in Accumulator
    max = np.max(Accumulator)
    [idx_phi, idx_p]=np.where(Accumulator == max)
    p=vector_p[idx_p]
    phi = vector_phi[idx_phi]
    return p,phi

width,height =  im.size


Parabolas = HoughParabola(img, (width + height) / 2 / 2, width + height)

print(Parabolas)