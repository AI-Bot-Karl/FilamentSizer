import cv2
import sys
from PIL import Image
import glob

class VideoCapture:

    def __init__(self):
        pass

    def open_camera(self, cam_id):
        self.cam_id = cam_id
        self.device = cv2.VideoCapture(self.cam_id)

    def close_camera(self):
        self.device.release()

    def get_frame(self):
        ret, frame = self.device.read()
        if ret == False:
            print(sys.stderr, "Error capturing from video device.")
            return None
        self.frame = frame
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        return Image.fromarray(cv2image)

    def show_frame(self):
        cv2.imshow("Camera"+self.cam_id.__str__(),self.frame)

    def cleanup(self):
        try:
            self.device.release()
            cv2.destroyAllWindows
        except:
            pass

    def __del__(self):
        self.cleanup()



class Detector:

    def __init__(self):
        self.find_scripts()


    def find_scripts(self):
        self.scripts=glob.glob('Detector Scripts/*.py')
        self.scriptiterator =glob.iglob('Detector Scripts/*.py')

    def run_scripts(self):
        pass


    def __del__(self):
        pass



class Datahandler:

    def __init__(self):
        pass

    def saveto(self):
        pass

    def startsaving(self):
        pass

    def stopsaving(self):
        pass

    def __del__(self):
        pass