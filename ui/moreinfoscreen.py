"""

Created on 15 Sept 2018.

@author: Graeme Zinck

"""

from tkinter import *
from ui.beattypes import BeatTypes
class MoreInfoScreen:
    def __init__(self, parent):
        self.container = Frame(parent)
        self.info = Message(self.container)
        self.info.configure(pady=20)

    def pack(self, beatType):
        self.info.configure(text=BeatTypes.BEATINFO[beatType])
        self.container.pack()
        # self.container.place(rely=0.65, relheight=0.35, relwidth=1)
        self.info.pack()

    def unpack(self):
        self.info.pack_forget()
        self.container.pack_forget()