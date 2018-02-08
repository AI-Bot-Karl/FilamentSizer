import cv2
import sys


class VideoCapture:

    def __init__(self):
        pass

    def open_camera(self, cam_id):
        self.cam_id = cam_id
        self.device = cv2.VideoCapture(self.cam_id)

    def get_frame(self):
        ret, frame = self.device.read()
        if ret == False:
            print(sys.stderr, "Error capturing from video device.")
            return None
        self.frame = frame
        return frame

    def show_frame(self):
        cv2.imshow("Camera"+self.cam_id.__str__(),self.frame)

    def cleanup(self):
        self.device.release()
        cv2.destroyAllWindows

    def __del__(self):
        self.cleanup()

def video_loop(vidcap):
    while (True):
        vidcap.get_frame(vidcap)
        vidcap.show_frame(vidcap)
        if (cv2.waitKey(2) >= 0):  # If the user presses any key, exit the loop
            break


# vc = VideoCapture()
# vc.open_camera(0)
# while(True):
#     vc.get_frame()
#     vc.show_frame()
#     if (cv2.waitKey(2) >= 0):  # If the user presses any key, exit the loop
#         break
# vc.cleanup()


