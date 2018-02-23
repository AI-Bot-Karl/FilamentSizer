import numpy as np

class Hough_Transform:

    def detect(self,frame ):
        lines = self.find_two_lines(self.auto_canny(frame))
        return lines





    def auto_canny(self,image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper, cv2.CV_64F, 5, True)

        # return the edged image
        return edged

    def find_two_lines(self,edges):
        thres = 1
        lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
        while len(lines) > 2:
            thres += 1
            lines = cv2.HoughLines(edges, 1, np.pi / 180, thres)
        return lines