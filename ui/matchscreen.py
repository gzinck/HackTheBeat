"""

Created on 15 Sept 2018.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image
from ui.beattypes import BeatTypes
from ui.moreinfoscreen import MoreInfoScreen

class MatchScreen:

    def __init__(self, root, graphImg, percentMatch, beatType):
        self.isExpanded = FALSE
        self.root = root
        self.frame = Frame(root)
        self.label_percentMatch = Label(self.frame,
                    text=str(percentMatch) + "% match",
                    compound = CENTER)
        self.canvas = Canvas(self.frame, width=200, height=100)
        self.label_beatType = Label(self.frame,
                    text=BeatTypes.BEATTYPE[beatType],
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

    def pack(self):
        self.frame.pack(expand=True)
        self.label_percentMatch.pack()
        self.canvas.pack()
        self.label_beatType.pack()
        self.down_img.pack(ipadx=20, ipady=5)

    def unpack(self):
        self.frame.pack_forget()
        self.label_percentMatch.pack_forget()
        self.canvas.pack_forget()
        self.label_beatType.pack_forget()
        self.down_img.pack_forget()

    def __pressExpandBtn(self):
        if(self.isExpanded):
            self.info_section.unpack()
            self.isExpanded = FALSE
            self.down_img.configure(image=self.img1)
        else:
            self.info_section.pack()
            self.isExpanded = TRUE
            self.down_img.configure(image=self.img2)