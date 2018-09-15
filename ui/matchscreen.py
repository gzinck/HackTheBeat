"""

Created on 15 Sept 2018.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image
from ui.beattypes import BeatTypes

class MatchScreen:

    def __init__(self, root, graphImg, percentMatch, beatType):
        self.root = root
        self.frame = Frame(root)
        self.label_percentMatch = Label(self.frame,
                    text=str(percentMatch) + "% match",
                    compound = CENTER)
        self.canvas = Canvas(self.frame, width=200, height=100)
        self.label_beatType = Label(self.frame,
                    text=BeatTypes.BEATTYPE[beatType],
                    compound = CENTER)
        
    def pack(self):
        self.frame.pack(expand=True)
        self.label_percentMatch.pack()
        self.canvas.pack()
        self.label_beatType.pack()

    def unpack(self):
        self.frame.pack_forget()
        self.label_percentMatch.pack_forget()
        self.canvas.pack_forget()
        self.label_beatType.pack_forget()