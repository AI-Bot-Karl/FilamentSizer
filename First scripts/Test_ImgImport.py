import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import ntpath

root = tk.Tk()
root.withdraw()

file_valid = False
while not file_valid:
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)

    if img is not None:
        file_valid = True


cv2.imshow( ntpath.basename(file_path), img)
while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break