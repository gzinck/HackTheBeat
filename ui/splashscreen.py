"""

Created on 15 Sept 2018.
This is the splashscreen which allows the user to start the application with
the analysis phase of the heartbeat recognition.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image
from ui.mainscreen import MainScreen

class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.resizedImage = Image.open("res/splashscreen.png")
        self.img = ImageTk.PhotoImage(self.resizedImage)
        self.working_widget = Label(root,
                    compound = CENTER,
                    image=self.img)
        self.label_widget = Button(root,
                    text="Click to begin analysis",
                    command=self.unpack)
        
    def pack(self):
        self.working_widget.pack()
        self.label_widget.place(x=100, y=500, width=200, height=50)

    def unpack(self):
        self.ms = MainScreen(self.root)
        self.label_widget.place_forget()
        self.working_widget.pack_forget()