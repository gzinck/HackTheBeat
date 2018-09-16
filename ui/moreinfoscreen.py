from tkinter import *
class MoreInfoScreen:
    def __init__(self, parent):
        self.container = Frame(parent)
        self.info = Message(self.container,
                    text="Hecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifyingHecking terrifying")

    def pack(self):
        self.container.place(rely=0.65, relheight=0.35, relwidth=1)
        self.info.pack()

    def unpack(self):
        self.info.pack_forget()
        self.container.place_forget()