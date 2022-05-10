# Splash screen
from tkinter import *
import os

def run():
    splashScreen.after(3000, os.system('python TicTacToe.py'))
    splashScreen.destroy()

splashScreen = Tk()
splashScreen.geometry("200x200")
#splashScreen.overrideredirect(True)

splashLabel = Label(splashScreen, text="Splash Screen", font=18)
splashLabel.pack()

splashScreen.eval('tk::PlaceWindow . center')
run()

splashScreen.mainloop()