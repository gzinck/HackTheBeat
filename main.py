# Python main file
from tkinter import *
from PIL import ImageTk,Image
from ui.launchscreen import LaunchScreen
from ui.matchscreen import MatchScreen
from ui.mainscreen import MainScreen

# Get the root
root = Tk()
root.geometry("400x500")
ms = MainScreen(root)
root.mainloop()

