from tkinter import *
from PIL import ImageTk,Image
from ui.launchscreen import LaunchScreen
from ui.matchscreen import MatchScreen

class MainScreen:
    def __init__(self, root):
        self.root = root
        # Add the screens
        self.ls = LaunchScreen(root)
        self.ms = MatchScreen(root, "", 70, 1)

        # Get the back image assets
        self.resizedImage = Image.open("res/reload_arrow.png").resize((30, 30))
        self.img = ImageTk.PhotoImage(self.resizedImage)
        # Make the back image
        self.back_btn = Button(root, image=self.img, command=self.refresh)
        self.back_btn.config(padx=5, pady=5)

        self.ls.pack()
        root.after(1000, self.ms.pack)
        root.after(1000, self.ls.unpack)
        self.back_btn.place(x=0, y=0)

    def refresh(self):
        self.ms.unpack()
        self.ls.pack()
        self.root.after(1000, self.ms.pack)
        self.root.after(1000, self.ls.unpack)
    
