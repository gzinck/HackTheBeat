"""

Created on 15 Sept 2018.
Initiates the main screen for the application, succeeding the loading screen.

@author: Graeme Zinck

"""

from tkinter import *
from PIL import ImageTk,Image
from ui.loadingscreen import LoadingScreen
from ui.matchscreen import MatchScreen

class MainScreen:
    def __init__(self, root):
        self.root = root
        # Add the screens
        self.ls = LoadingScreen(root)
        self.ms = MatchScreen(root)

        # Get the back image assets
        self.resizedImage = Image.open("res/reload_arrow.png").resize((30, 30))
        self.img = ImageTk.PhotoImage(self.resizedImage)
        # Make the back image
        self.back_btn = Button(root, image=self.img, command=self.refresh)
        self.back_btn.config(padx=5, pady=5)

        # Pack the match screen and plop the back button there
        self.ms.pack()
        self.back_btn.place(x=0, y=0)
        self.refresh()

    """
    Refreshes the data by performing the analysis all over again and
    recalculating the information for the GUI.
    """
    def refresh(self):
        self.ms.unpack()
        self.ls.pack()
        self.root.after(1000, self.ms.pack)
        self.root.after(1000, self.ls.unpack)