# Tic Tac Toe game
# @author Austine D. Odhiambo

from tkinter import *
from tkinter import messagebox

# Turn variable (Boolean): Used to determine player turns
isOTurn = False
# Game state variable (List): Used to store game state
gameState = [None] * 9

# Game I/O function
# Gets the buttons presses, checks the player who pressed, displays letter on the button
def gameInput(buttonPress):
    global isOTurn
    x = 'X'
    o = 'O'
    
    # Check for button presses
    if(buttonPress == 1):
        # check which player's turn it is (repeated for all buttons)
        if(not(isOTurn)):
            button1.config(text = x)
            button1.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button1.config(text = o)
            button1.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 2):
        if(not(isOTurn)):
            button2.config(text = x)
            button2.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button2.config(text = o)
            button2.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 3):
        if(not(isOTurn)):
            button3.config(text = x)
            button3.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button3.config(text = o)
            button3.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 4):
        if(not(isOTurn)):
            button4.config(text = x)
            button4.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button4.config(text = o)
            button4.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 5):
        if(not(isOTurn)):
            button5.config(text = x)
            button5.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button5.config(text = o)
            button5.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 6):
        if(not(isOTurn)):
            button6.config(text = x)
            button6.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button6.config(text = o)
            button6.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 7):
        if(not(isOTurn)):
            button7.config(text = x)
            button7.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button7.config(text = o)
            button7.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 8):
        if(not(isOTurn)):
            button8.config(text = x)
            button8.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button8.config(text = o)
            button8.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    elif(buttonPress == 9):
        if(not(isOTurn)):
            button9.config(text = x)
            button9.config(state = DISABLED)
            isOTurn = True
            checkWinState(x, buttonPress)
        elif(isOTurn):
            button9.config(text = o)
            button9.config(state = DISABLED)
            isOTurn = False
            checkWinState(o, buttonPress)

    else:
        print('error with input')

# Check win state function
# checks if x or o has met the win condition
def checkWinState(player, buttonId):
    global gameState
    global isOTurn
    gameState[buttonId - 1] = player

    if(gameState[0] == 'X' and gameState[1] == 'X'  and gameState[2] == 'X' or gameState[0] == 'O' and gameState[1] == 'O'  and gameState[2] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            print(isOTurn)
            print(gameState)
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            print(isOTurn)
            print(gameState)
            resetGame()

    if(gameState[0] == 'X' and gameState[3] == 'X'  and gameState[6] == 'X' or gameState[0] == 'O' and gameState[3] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()

    if(gameState[0] == 'X' and gameState[4] == 'X'  and gameState[8] == 'X' or gameState[0] == 'O' and gameState[4] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()

    if(gameState[1] == 'X' and gameState[4] == 'X'  and gameState[7] == 'X' or gameState[1] == 'O' and gameState[4] == 'O'  and gameState[7] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()

    if(gameState[2] == 'X' and gameState[4] == 'X'  and gameState[6] == 'X' or gameState[2] == 'O' and gameState[4] == 'O'  and gameState[6] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()

    if(gameState[2] == 'X' and gameState[5] == 'X'  and gameState[8] == 'X' or gameState[2] == 'O' and gameState[5] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
    
    if(gameState[3] == 'X' and gameState[4] == 'X'  and gameState[5] == 'X' or gameState[3] == 'O' and gameState[4] == 'O'  and gameState[5] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
    
    if(gameState[6] == 'X' and gameState[7] == 'X'  and gameState[8] == 'X' or gameState[6] == 'O' and gameState[7] == 'O'  and gameState[8] == 'O'):
        if(player == 'X'):
            messagebox.showinfo('Message', 'X Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()
        elif(player == 'O'):
            messagebox.showinfo('Message', 'O Wins!')
            isOTurn = False
            gameState = [None] * 9
            resetGame()

# Reset game function
# Resets game after player win or game over
def resetGame():
    button1.config(text = '')
    button1.config(state = NORMAL)

    button2.config(text = '')
    button2.config(state = NORMAL)

    button3.config(text = '')
    button3.config(state = NORMAL)

    button4.config(text = '')
    button4.config(state = NORMAL)

    button5.config(text = '')
    button5.config(state = NORMAL)

    button6.config(text = '')
    button6.config(state = NORMAL)

    button7.config(text = '')
    button7.config(state = NORMAL)

    button8.config(text = '')
    button8.config(state = NORMAL)

    button9.config(text = '')
    button9.config(state = NORMAL)

# Create gui
window = Tk()
button1 = Button(window, text='')
button1.config(command = lambda m = 1: gameInput(m))
button1.config(font = ('Ink Free', 50, 'bold'))
button1.config(height = 1, width = 2)
button1.grid(row = 1, column = 1)

button2 = Button(window, text='')
button2.config(command = lambda m = 2: gameInput(m))
button2.config(font = ('Ink Free', 50, 'bold'))
button2.config(height = 1, width = 2)
button2.grid(row = 1, column = 2)

button3 = Button(window, text='')
button3.config(command = lambda m = 3: gameInput(m))
button3.config(font = ('Ink Free', 50, 'bold'))
button3.config(height = 1, width = 2)
button3.grid(row = 1, column = 3)

button4 = Button(window, text='')
button4.config(command = lambda m = 4: gameInput(m))
button4.config(font = ('Ink Free', 50, 'bold'))
button4.config(height = 1, width = 2)
button4.grid(row = 2, column = 1)

button5 = Button(window, text='')
button5.config(command = lambda m = 5: gameInput(m))
button5.config(font = ('Ink Free', 50, 'bold'))
button5.config(height = 1, width = 2)
button5.grid(row = 2, column = 2)

button6 = Button(window, text='')
button6.config(command = lambda m = 6: gameInput(m))
button6.config(font = ('Ink Free', 50, 'bold'))
button6.config(height = 1, width = 2)
button6.grid(row = 2, column = 3)

button7 = Button(window, text='')
button7.config(command = lambda m = 7: gameInput(m))
button7.config(font = ('Ink Free', 50, 'bold'))
button7.config(height = 1, width = 2)
button7.grid(row = 3, column = 1)

button8 = Button(window, text='')
button8.config(command = lambda m = 8: gameInput(m))
button8.config(font = ('Ink Free', 50, 'bold'))
button8.config(height = 1, width = 2)
button8.grid(row = 3, column = 2)

button9 = Button(window, text='')
button9.config(command = lambda m = 9: gameInput(m))
button9.config(font = ('Ink Free', 50, 'bold'))
button9.config(height = 1, width = 2)
button9.grid(row = 3, column = 3)

window.mainloop() 