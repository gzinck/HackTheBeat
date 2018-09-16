"""

Created on 15 Sept 2018.
Creates a loading screen while the analysis occurs.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image


class LoadingScreen:
    def __init__(self, root):
        self.img = PhotoImage(file = "res/analysing_bg.gif", format="gif -index 3")
        self.image_widget = Label(root,
                    compound = CENTER,
                    image=self.img)
        
    def pack(self):
        self.image_widget.pack()

    def unpack(self):
        self.image_widget.pack_forget()