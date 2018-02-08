from tkinter import *


class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Filamentsizer")

        # Labels
        l1 = Label(window, text="Choose Camera")
        l1.grid(row=0, column=0)

        # OptionMenus
        cams = ['0', '1', '2']
        self.vs = StringVar()
        self.vs.set(cams[0])
        om1 = OptionMenu(window, self.vs, *cams, command=self.camerachanged)
        om1.grid(row=0, column=1)
        self.camerachanged('0')

        # Buttons
        self.b1_text = StringVar()
        self.b1_text.set("Start")
        self.b1 = Button(textvariable=self.b1_text, command=self.start_pressed)
        self.b1.grid(row=1, column=0)

    def start_pressed(self):
        if self.b1_text.get() == "Start":
            self.b1_text.set("Stop")
        else:
            self.b1_text.set("Start")

    def camerachanged(self, nr):
        print('Camera was changed on UI to:' + self.vs.get())
        self.choose_Cam(int(nr))

    def choose_Cam(self, number):
        self.cam = number


root = Tk()
gui = Window(root)
root.mainloop()
