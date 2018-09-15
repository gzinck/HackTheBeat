"""

Created on 15 Sept 2018.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image


class LaunchScreen:
    def __init__(self, root):
        self.resizedImage = Image.open("res/gears.png").resize((60, 60))
        self.img = ImageTk.PhotoImage(self.resizedImage)
        self.frame = Frame(root)
        self.label_widget = Label(self.frame,
                    text="Analysing...",
                    compound = CENTER)
        self.working_widget = Label(self.frame,
                    compound = CENTER,
                    image=self.img)
        
    def pack(self):
        self.frame.pack(expand=True)
        self.label_widget.pack()
        self.working_widget.pack()
        
    def __del__(self):
        self.frame.pack_forget()
        self.label_widget.pack_forget()
        self.working_widget.pack_forget()