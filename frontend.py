from tkinter import *
from PIL import Image, ImageTk
import backend


class MainWindow(Frame):

    def __init__(self,title="Filamentsizer", master=None):
        frame =Frame.__init__(self, master)
        self.master.title(title)

        # Labels
        self.l1 = Label(self.master, text="Choose Camera")
        self.l1.grid(row=0, column=0)

        # OptionMenus
        cams = ['0', '1', '2']
        self.vs = StringVar()
        self.vs.set(cams[0])
        om1 = OptionMenu(self.master, self.vs, *cams, command=self.camerachanged)
        om1.grid(row=0, column=1)
        self.camerachanged('0')

        # Buttons
        self.b1_text = StringVar()
        self.b1_text.set("Start")
        self.b1 = Button(self.master, textvariable=self.b1_text, command=self.start_pressed)
        self.b1.grid(row=1, column=0)

        self.start_backend()

    def start_pressed(self):
        if self.b1_text.get() == "Start":
            self.b1_text.set("Stop")

            # self.vc.open_camera(self.vc,0)
            # backend.video_loop(self.vc)
        else:
            self.b1_text.set("Start")

    def camerachanged(self, nr):
        print('Camera was changed on UI to:' + self.vs.get())
        self.choose_Cam(int(nr))

    def choose_Cam(self, number):
        self.cam = number

    def start_backend(self):
        # self.vc = backend.VideoCapture
        pass

    def __del__(self):
        try:
            self.vc.cleanup()
        except:
            pass


class CamView():
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(parent)

        self.lmain2 = Label(self.window)
        self.lmain2.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.show_frame()

    def show_frame(self):
        imgtk = ImageTk.PhotoImage(image =None)
        self.lmain2.imgtk = imgtk
        self.lmain2.configure(image=imgtk)

    def close(self):
        self.parent.test_frame = None
        self.window.destroy()







if __name__=='__main__':
    app = MainWindow()
    app.mainloop()