#******************************************************************************
# Tic Tac Toe game
# 
# Python source code for a simple Tic Tac Toe game
# The purpose of this game is to test my python skills, GUI development skills
# as well as the Tkinter module
#
# Splash screen
#
# @author Austine D. Odhiambo
#
#******************************************************************************
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