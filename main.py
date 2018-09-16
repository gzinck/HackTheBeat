"""

Created on 15 Sept 2018.
This starts the python application.

@author: Graeme Zinck

"""

# Python main file
from tkinter import *
from PIL import ImageTk,Image
from ui.launchscreen import LaunchScreen
from ui.matchscreen import MatchScreen
from ui.mainscreen import MainScreen
from ui.introscreen import IntroScreen

# Get the root
root = Tk()
root.title("Hack the Beat")
root.geometry("400x600")
isd = IntroScreen(root)
isd.pack()
# ms = MainScreen(root)
root.mainloop()