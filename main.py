# Python main file
from tkinter import *
from PIL import ImageTk,Image
from ui.launchscreen import LaunchScreen
from ui.matchscreen import MatchScreen

root = Tk()
root.geometry("400x500")

ls = LaunchScreen(root)
ms = MatchScreen(root, "", 70, 1)
ls.pack()
root.after(1000, ms.pack)
root.after(1000, ls.__del__)

root.mainloop()