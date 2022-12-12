#******************************************************************************
# Tic Tac Toe game
# 
# Python source code for a simple Tic Tac Toe game
# The purpose of this game is to test my python skills, GUI development skills
# as well as the Tkinter module
#
# @author Austine D. Odhiambo AKA Ace Declan
#
#******************************************************************************

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

# Turn variable (Boolean): Used to determine player turns
isOTurn = False
# Game state variable (List): Used to store game state
gameState = [None] * 9

#Splash screen
splashScreen = Tk()
splashScreen.title("Splash")
splashScreen.geometry("300x200")
splashScreen.overrideredirect(True)
splashLabel = Label(splashScreen, text="Tic Tac Toe\n An Ace Declan game", font=('Montserat', 12))
splashLabel.pack(pady=20)
splashScreen.eval('tk::PlaceWindow . center')

# Game I/O function
# Gets the buttons presses, checks the player who pressed, displays letter on the button
def gameInput(buttonPress):
    global isOTurn
    x = 'X'
    o = 'O'
    # Check for button presses
    # TODO: if possible, use 1 if statment to check for all the buttons
    if(buttonPress == 1):
        # check which player's turn it is (repeated for all buttons)
        if(not(isOTurn)):
            buttons[0].config(text = x)
            buttons[0].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[0].config(text = o)
            buttons[0].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 2):
        if(not(isOTurn)):
            buttons[1].config(text = x)
            buttons[1].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[1].config(text = o)
            buttons[1].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 3):
        if(not(isOTurn)):
            buttons[2].config(text = x)
            buttons[2].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[2].config(text = o)
            buttons[2].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 4):
        if(not(isOTurn)):
            buttons[3].config(text = x)
            buttons[3].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[3].config(text = o)
            buttons[3].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 5):
        if(not(isOTurn)):
            buttons[4].config(text = x)
            buttons[4].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[4].config(text = o)
            buttons[4].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 6):
        if(not(isOTurn)):
            buttons[5].config(text = x)
            buttons[5].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[5].config(text = o)
            buttons[5].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 7):
        if(not(isOTurn)):
            buttons[6].config(text = x)
            buttons[6].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[6].config(text = o)
            buttons[6].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 8):
        if(not(isOTurn)):
            buttons[7].config(text = x)
            buttons[7].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[7].config(text = o)
            buttons[7].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 9):
        if(not(isOTurn)):
            buttons[8].config(text = x)
            buttons[8].config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            buttons[8].config(text = o)
            buttons[8].config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    else:
        print('error with input')

# Check win state function
# Checks if x or o has met the win condition
def checkWinState(player, buttonId):
    global gameState
    gameState[buttonId - 1] = player
    winState = False

    if(gameState[0] == 'X' and gameState[1] == 'X'  and gameState[2] == 'X' or gameState[0] == 'O' and gameState[1] == 'O'  and gameState[2] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[0] == 'X' and gameState[3] == 'X'  and gameState[6] == 'X' or gameState[0] == 'O' and gameState[3] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[0] == 'X' and gameState[4] == 'X'  and gameState[8] == 'X' or gameState[0] == 'O' and gameState[4] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[1] == 'X' and gameState[4] == 'X'  and gameState[7] == 'X' or gameState[1] == 'O' and gameState[4] == 'O'  and gameState[7] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[2] == 'X' and gameState[4] == 'X'  and gameState[6] == 'X' or gameState[2] == 'O' and gameState[4] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()

    if(gameState[2] == 'X' and gameState[5] == 'X'  and gameState[8] == 'X' or gameState[2] == 'O' and gameState[5] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            winState = True
            resetGame()
    
    if(gameState[3] == 'X' and gameState[4] == 'X'  and gameState[5] == 'X' or gameState[3] == 'O' and gameState[4] == 'O'  and gameState[5] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            resetGame()
    
    if(gameState[6] == 'X' and gameState[7] == 'X'  and gameState[8] == 'X' or gameState[6] == 'O' and gameState[7] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            winState = True
            resetGame()
        elif(player == 'O'):
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

    buttons[0].config(text = '')
    buttons[0].config(state = NORMAL)

    buttons[1].config(text = '')
    buttons[1].config(state = NORMAL)

    buttons[2].config(text = '')
    buttons[2].config(state = NORMAL)

    buttons[3].config(text = '')
    buttons[3].config(state = NORMAL)

    buttons[4].config(text = '')
    buttons[4].config(state = NORMAL)

    buttons[5].config(text = '')
    buttons[5].config(state = NORMAL)

    buttons[6].config(text = '')
    buttons[6].config(state = NORMAL)

    buttons[7].config(text = '')
    buttons[7].config(state = NORMAL)

    buttons[8].config(text = '')
    buttons[8].config(state = NORMAL)

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

    global buttons
    global rightClickMenu

    window = Tk()
    window.title("Tic Tac Toe")
    window.geometry('435x435')
    window.resizable(False, False)

    buttons = list()

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
               
            buttons[k].config(command = lambda m = k + 1: gameInput(m))
            buttons[k].config(font = ('Ink Free', 75, 'bold'))

            buttonFrame.rowconfigure(0, weight = 1)
            buttonFrame.columnconfigure(0, weight = 1)
            buttonFrame.grid_propagate(0)
            buttonFrame.grid(row = j + 1, column = i + 1)

            buttons[k].grid(sticky = "NWSE")

    rightClickMenu = Menu(window, tearoff = 0)
    rightClickMenu.add_command(label ="Restart", command = resetGame)

    window.bind("<Button-3>", showRightClickMenu)
    window.eval('tk::PlaceWindow . center')

splashScreen.after(2000, mainWindow)
mainloop()