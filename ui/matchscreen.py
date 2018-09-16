"""

Created on 15 Sept 2018.
Creates a screen showing the closest matching heartbeat pattern for the
individual.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image
from ui.beattypes import BeatTypes
from ui.moreinfoscreen import MoreInfoScreen
import random

class MatchScreen:

    def __init__(self, root):
        self.isExpanded = FALSE
        self.root = root
        self.frame = Frame(root)
        self.label_percentMatch = Label(self.frame,
                    compound = CENTER)
        # self.canvas = Canvas(self.frame, width=200, height=100)
        self.canvas = Label(self.frame,
                compound = CENTER,
                width=400,
                height=200)
        self.label_beatType = Label(self.frame,
                    compound = CENTER)
        self.label_beatType.config(font=("TkDefaultFont", 30))
        
        # Make the extra info section
        self.info_section = MoreInfoScreen(root)

        # Get the down image assets
        self.resizedImage1 = Image.open("res/down_arrow.png").resize((30, 30))
        self.img1 = ImageTk.PhotoImage(self.resizedImage1)
        # Make the down image
        self.down_img = Button(root, image=self.img1, command=self.__pressExpandBtn)

        # Get the up image assets
        self.resizedImage2 = Image.open("res/up_arrow.png").resize((30, 30))
        self.img2 = ImageTk.PhotoImage(self.resizedImage2)

    def pack(self, graphImg = "", percentMatch = 70, beatType = -1):
        if(beatType == -1):
            self.beatType = random.randint(0, 5)
        else:
            self.beatType = beatType
        if(graphImg == ""):
             # Get the image assets
            self.resizedImage3 = Image.open("res/demo_graph.png").resize((400,200))
            self.graphImg = ImageTk.PhotoImage(self.resizedImage3)
        else:
            self.graphImg = graphImg
        # Make the graph image
        self.canvas.configure(image=self.graphImg)

        self.frame.pack(expand=True)
        self.label_percentMatch.configure(text=str(percentMatch) + "% match")
        self.label_percentMatch.pack()
        self.canvas.pack()

        self.label_beatType.configure(text=BeatTypes.BEATTYPE[self.beatType])
        self.label_beatType.pack()
        self.down_img.pack(ipadx=190)

    def unpack(self):
        self.frame.pack_forget()
        self.label_percentMatch.pack_forget()
        self.canvas.pack_forget()
        self.label_beatType.pack_forget()
        self.down_img.pack_forget()
        self.isExpanded = FALSE
        self.info_section.unpack()

    """
    When press the expand button, open up extra information
    (or if already open, close it)
    """
    def __pressExpandBtn(self):
        if(self.isExpanded):
            self.info_section.unpack()
            self.isExpanded = FALSE
            self.down_img.configure(image=self.img1)
        else:
            self.info_section.pack(self.beatType)
            self.isExpanded = TRUE
            self.down_img.configure(image=self.img2)