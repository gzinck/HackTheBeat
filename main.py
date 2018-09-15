# Python main file
from tkinter import *
from PIL import ImageTk,Image
from ui.launchscreen import LaunchScreen

root = Tk()
root.geometry("400x500")

ls = LaunchScreen(root)

root.mainloop()