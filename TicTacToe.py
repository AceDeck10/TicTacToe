#******************************************************************************
# Tic Tac Toe game
# 
# Python source code for a simple Tic Tac Toe game
# The purpose of this game is to test my python skills, GUI development skills
# as well as the Tkinter module
#   
# WARNING!: This program makes use of global variables 
# in a manner that is not best practice
#
# @author Austine D. Odhiambo AKA Ace Declan
#
#******************************************************************************

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

from PIL import ImageTk, Image

import sys, os

# Must include the following function for pyinstaller to build 
# the program correctlly
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Turn variable (Boolean): Used to determine player turns
isOTurn = False
# Game state variable (List): Used to store game state
gameState = [None] * 9

#Splash screen
splashScreen = Tk()
splashScreen.title("Splash")
splashScreen.geometry("300x200")
splashScreen.overrideredirect(True)

splashImageFrame = Frame(splashScreen, width=200, height=200)
splashImageFrame.pack()
splashImageFrame.place(anchor='center', relx=0.5, rely=0.5)

img = Image.open(resource_path("img\\tic-tac-toe.png"))
imgResized = img.resize((200, 200))
splashImage = ImageTk.PhotoImage(imgResized)

label = Label(splashImageFrame, image = splashImage)
label.pack()

splashScreen.eval('tk::PlaceWindow . center')

# Game I/O function
# Gets the buttons presses, checks the player who pressed, displays letter on the button
def gameInput(buttonPress):
    global isOTurn
    x = 'X'
    o = 'O'
    # Check for button presses

    for i in range(1, 10, 1):
        if(buttonPress == i):
            # check which player's turn it is (repeated for all buttons)
            if(not(isOTurn)):
                buttons[i - 1].config(text = x, state = DISABLED)
                isOTurn = True
                checkWinState(x, buttonPress)
            elif(isOTurn):
                buttons[i - 1].config(text = o, state = DISABLED)
                isOTurn = False
                checkWinState(o, buttonPress)

# Check win state function
# Checks if x or o has met the win condition
def checkWinState(player, buttonId):
    global gameState
    gameState[buttonId - 1] = player
    winState = False

    if(gameState[0] == 'X' and gameState[1] == 'X'  and gameState[2] == 'X' or gameState[0] == 'O' and gameState[1] == 'O'  and gameState[2] == 'O'):
        if(player == 'X'):
            buttons[0].config(bg = 'yellow')
            buttons[1].config(bg = 'yellow')
            buttons[2].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[0].config(bg = 'yellow')
            buttons[1].config(bg = 'yellow')
            buttons[2].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[0] == 'X' and gameState[3] == 'X'  and gameState[6] == 'X' or gameState[0] == 'O' and gameState[3] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            buttons[0].config(bg = 'yellow')
            buttons[3].config(bg = 'yellow')
            buttons[6].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[0].config(bg = 'yellow')
            buttons[3].config(bg = 'yellow')
            buttons[6].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[0] == 'X' and gameState[4] == 'X'  and gameState[8] == 'X' or gameState[0] == 'O' and gameState[4] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            buttons[0].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[0].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[1] == 'X' and gameState[4] == 'X'  and gameState[7] == 'X' or gameState[1] == 'O' and gameState[4] == 'O'  and gameState[7] == 'O'):
        if(player == 'X'):
            buttons[1].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[7].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[1].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[7].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[2] == 'X' and gameState[4] == 'X'  and gameState[6] == 'X' or gameState[2] == 'O' and gameState[4] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            buttons[2].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[6].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[2].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[6].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[2] == 'X' and gameState[5] == 'X'  and gameState[8] == 'X' or gameState[2] == 'O' and gameState[5] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            buttons[2].config(bg = 'yellow')
            buttons[5].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[2].config(bg = 'yellow')
            buttons[5].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()
    
    if(gameState[3] == 'X' and gameState[4] == 'X'  and gameState[5] == 'X' or gameState[3] == 'O' and gameState[4] == 'O'  and gameState[5] == 'O'):
        if(player == 'X'):
            buttons[3].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[5].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[3].config(bg = 'yellow')
            buttons[4].config(bg = 'yellow')
            buttons[5].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            resetGame()
    
    if(gameState[6] == 'X' and gameState[7] == 'X'  and gameState[8] == 'X' or gameState[6] == 'O' and gameState[7] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            buttons[6].config(bg = 'yellow')
            buttons[7].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            buttons[6].config(bg = 'yellow')
            buttons[7].config(bg = 'yellow')
            buttons[8].config(bg = 'yellow')
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(winState != True and any(elem is None for elem in gameState) == False):
        messagebox.showinfo('Message', 'Draw')
        resetGame()   


# Reset game function
# Resets game after player win or game over
def resetGame():
    global isOTurn
    global gameState
    
    isOTurn = False
    gameState = [None] * 9

    # For loop to reset buttons
    for i in range(len(buttons)):
        buttons[i].config(text = '', bg = origColor, state = NORMAL)


# Right click menu function
def showRightClickMenu(event):
    try:
        rightClickMenu.tk_popup(event.x_root, event.y_root)
    finally:
        rightClickMenu.grab_release()


#Main window
def mainWindow():
    # Destroy spash screen
    try:
        splashScreen
    except NameError:
        splashExists = False
    else:
        splashExists = True

    if(splashExists == True):
        splashScreen.destroy()

    # Declare globals
    global buttons
    global rightClickMenu
    global origColor

    # Create main window
    window = Tk()
    window.title("Tic Tac Toe")
    window.iconbitmap(resource_path("img\\tic-tac-toe.ico"))
    window.geometry('435x435')
    window.resizable(False, False)

    # Create list to store buttons
    buttons = list()

    # For loop to create buttons
    for i in range(3):
        for j in range(3):
            if(i == 0):
                k = i + j
            elif(i == 1):
                k = i + j + 2
            elif(i == 2):
                k = i + j + 4
            else:
                print('error while creating buttons')

            buttonFrame = Frame(width=145,height=145)

            buttons.append(Button(buttonFrame, text='', compound = CENTER))
               
            buttons[k].config(font = ('Ink Free', 75, 'bold'), command = lambda m = k + 1: gameInput(m))

            buttonFrame.rowconfigure(0, weight = 1)
            buttonFrame.columnconfigure(0, weight = 1)
            buttonFrame.grid_propagate(0)
            buttonFrame.grid(row = j + 1, column = i + 1)

            buttons[k].grid(sticky = "NWSE")

            origColor = buttons[k].cget("background")

    rightClickMenu = Menu(window, tearoff = 0)
    rightClickMenu.add_command(label ="Restart", command = resetGame)

    window.bind("<Button-3>", showRightClickMenu)
    window.eval('tk::PlaceWindow . center')

splashScreen.after(2000, mainWindow)
mainloop()