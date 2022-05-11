# Splash screen
from tkinter import *
import os

def run():
    os.system('python TicTacToe.py')

splashScreen = Tk()
splashScreen.geometry("200x200")
#splashScreen.overrideredirect(True)

splashLabel = Label(splashScreen, text="Splash Screen", font=18)
splashLabel.pack()

splashScreen.eval('tk::PlaceWindow . center')

splashScreen.after(3000, run)
splashScreen.mainloop()