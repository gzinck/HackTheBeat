"""

Created on 15 Sept 2018.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image


class MatchScreen:

    def __init__(self, root, graphImg, percentMatch, beatType):
        self.root = root
        self.frame = Frame(root)
        self.label_percentMatch = Label(self.frame,
                    text=str(percentMatch) + "% match",
                    compound = CENTER)
        self.canvas = Canvas(self.frame, width=200, height=100)
        self.label_beatType = Label(self.frame,
                    text=beatType,
                    compound = CENTER)
        self.__makeBackButton()
        
    def pack(self):
        self.frame.pack(expand=True)
        self.label_percentMatch.pack()
        self.canvas.pack()
        self.label_beatType.pack()
        self.back_btn.place(x=0, y=0)

    def __del__(self):
        self.frame.pack_forget()
        self.label_percentMatch.pack_forget()
        self.canvas.pack_forget()
        self.label_beatType.pack_forget()

    def __makeBackButton(self):
        self.resizedImage = Image.open("res/reload_arrow.png").resize((30, 30))
        self.img = ImageTk.PhotoImage(self.resizedImage)
        self.back_btn = Button(self.root, image=self.img)
        