

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import backend


class MainWindow(tk.Frame):
    def __init__(self, parent=None):
        frame = tk.Frame.__init__(self, parent)
        self.lmain = tk.Label(parent)
        self.lmain.grid(row=0,column=3)

        self.test_frame = None

        # Labels
        self.l1 = tk.Label(self.master, text="Choose Camera")
        self.l1.grid(row=0, column=0)

        # OptionMenus
        cams = ['0', '1', '2']
        self.vs = tk.StringVar()
        self.vs.set(cams[0])
        om1 = tk.OptionMenu(self.master, self.vs, *cams, command=self.camerachanged)
        om1.grid(row=0, column=1)
        self.camerachanged('0')

        # Buttons
        self.b1_text = tk.StringVar()
        self.b1_text.set("Start")
        self.b1 = tk.Button(self.master, textvariable=self.b1_text, command=self.start_pressed)
        self.b1.grid(row=1, column=0)


        # b = tk.Button(frame, text='open', command=self.load_window)
        # b.pack()

        width, height = 800, 600
        self.vidcap=backend.VideoCapture()





    def do_stuff(self):

        self.img = self.vidcap.get_frame()
        if self.test_frame != None:
            self.test_frame.show_frame()
        self.lmain.after(10, self.do_stuff)

    def load_window(self):
        if self.test_frame == None:
            self.test_frame = CamView(self)

    def start_pressed(self):
        if self.b1_text.get() == "Start":
            self.b1_text.set("Stop")
            self.vidcap.open_camera(self.cam)
            self.do_stuff()
            self.load_window()

        else:
            self.b1_text.set("Start")
            self.vidcap.close_camera()

    def camerachanged(self, nr):
        print('Camera was changed on UI to:' + self.vs.get())
        self.cam = (int(nr))



class CamView():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)

        self.lmain2 = tk.Label(self.window)
        self.lmain2.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.show_frame()

    def show_frame(self):
        imgtk = ImageTk.PhotoImage(image=self.parent.img)
        self.lmain2.imgtk = imgtk
        self.lmain2.configure(image=imgtk)

    def close(self):
        self.parent.test_frame = None
        self.window.destroy()





# root = tk.Tk()
# root.bind('<Escape>', lambda e: root.quit())
# control = Main(root)
# root.mainloop()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()