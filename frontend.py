
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import backend
import ttkwidgets



class MainWindow(tk.Frame):
    def __init__(self, parent=None):
        frame = tk.Frame.__init__(self, parent)
        self.lmain = tk.Label(parent)
        self.lmain.grid(row=0 ,column=3)

        self.test_frame = None

        self.build_UI()

        self.vidcap =backend.VideoCapture()

        self.do_stuff()



    def build_UI(self):
        # Labels
        self.l1 = tk.Label(self.master, text="Choose Camera")
        self.l1.grid(row=0, column=0)


        # OptionMenus
        self.cams = ['0', '1', '2']
        self.camselection = self.cams
        self.vs = tk.StringVar()
        self.vs.set(self.cams[0])
        self.om1 = tk.OptionMenu(self.master, self.vs, *self.camselection, command=self.camerachanged, )
        self.om1.grid(row=0, column=1)
        self.camerachanged('0')

        # Buttons
        self.b1_text = tk.StringVar()
        self.b1_text.set("Start")
        self.b1 = tk.Button(self.master, textvariable=self.b1_text, command=self.start_pressed)
        self.b1.grid(row=1, column=0)

        #Listbox
        # self.list1 = tk.Listbox(self.master)
        # self.list1.grid(row=3,column=0)



    def do_stuff(self):
        #print("do stuff")
        if self.test_frame is not None:
            #print("testframe not none")
            self.img = self.vidcap.get_frame()
            self.test_frame.show_frame()
        self.lmain.after(10, self.do_stuff)

    def load_window(self):
        if self.test_frame is None:
            self.test_frame = CamView(self)

    def close_window(self):
        self.test_frame.close()
        self.test_frame = None

    def start_pressed(self):
        if self.b1_text.get() == "Start":
            self.b1_text.set("Stop")
            self.vidcap.open_camera(self.cam)
            self.load_window()
            self.camselection = self.cam.__str__()

        else:
            self.b1_text.set("Start")
            self.vidcap.close_camera()
            self.close_window()
            self.camselection = self.cams

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
        try:
            imgtk = ImageTk.PhotoImage(image=self.parent.img)
            self.lmain2.imgtk = imgtk
            self.lmain2.configure(image=imgtk)
        except:
            pass

    def close(self):
        self.parent.test_frame = None
        self.window.destroy()



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
