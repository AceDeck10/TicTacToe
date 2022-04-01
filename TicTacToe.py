from tkinter import *

isOTurn = False

# game input function
def gameInput(buttonPress):
    global isOTurn
    x = 'X'
    o = 'O'
    
    # Check for button presses
    if(buttonPress == 'button1'):
        global isOTurn
        # check which player's turn it is (repeated fo all buttons)
        if(not(isOTurn)):
            button1.config(text = x)
            button1.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button1.config(text = o)
            button1.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button2'):
        if(not(isOTurn)):
            button2.config(text = x)
            button2.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button2.config(text = o)
            button2.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button3'):
        if(not(isOTurn)):
            button3.config(text = x)
            button3.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button3.config(text = o)
            button3.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button4'):
        if(not(isOTurn)):
            button4.config(text = x)
            button4.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button4.config(text = o)
            button4.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button5'):
        if(not(isOTurn)):
            button5.config(text = x)
            button5.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button5.config(text = o)
            button5.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button6'):
        if(not(isOTurn)):
            button6.config(text = x)
            button6.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button6.config(text = o)
            button6.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button7'):
        if(not(isOTurn)):
            button7.config(text = x)
            button7.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button7.config(text = o)
            button7.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button8'):
        if(not(isOTurn)):
            button8.config(text = x)
            button8.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button8.config(text = o)
            button8.config(state = DISABLED)
            isOTurn = False

    elif(buttonPress == 'button9'):
        if(not(isOTurn)):
            button9.config(text = x)
            button9.config(state = DISABLED)
            isOTurn = True
        elif(isOTurn):
            button9.config(text = o)
            button9.config(state = DISABLED)
            isOTurn = False

    else:
        print('error with input')

# create window
window = Tk()
button1 = Button(window, text='')
button1.config(command = lambda m='button1': gameInput(m))
button1.config(font = ('Ink Free', 50, 'bold'))
button1.config(height = 1, width = 2)
button1.grid(row=1, column=1)

button2 = Button(window, text='')
button2.config(command = lambda m='button2': gameInput(m))
button2.config(font = ('Ink Free', 50, 'bold'))
button2.config(height = 1, width = 2)
button2.grid(row=1, column=2)

button3 = Button(window, text='')
button3.config(command = lambda m='button3': gameInput(m))
button3.config(font = ('Ink Free', 50, 'bold'))
button3.config(height = 1, width = 2)
button3.grid(row=1, column=3)

button4 = Button(window, text='')
button4.config(command = lambda m='button4': gameInput(m))
button4.config(font = ('Ink Free', 50, 'bold'))
button4.config(height = 1, width = 2)
button4.grid(row=2, column=1)

button5 = Button(window, text='')
button5.config(command = lambda m='button5': gameInput(m))
button5.config(font = ('Ink Free', 50, 'bold'))
button5.config(height = 1, width = 2)
button5.grid(row=2, column=2)

button6 = Button(window, text='')
button6.config(command = lambda m='button6': gameInput(m))
button6.config(font = ('Ink Free', 50, 'bold'))
button6.config(height = 1, width = 2)
button6.grid(row=2, column=3)

button7 = Button(window, text='')
button7.config(command = lambda m='button7': gameInput(m))
button7.config(font = ('Ink Free', 50, 'bold'))
button7.config(height = 1, width = 2)
button7.grid(row=3, column=1)

button8 = Button(window, text='')
button8.config(command = lambda m='button8': gameInput(m))
button8.config(font = ('Ink Free', 50, 'bold'))
button8.config(height = 1, width = 2)
button8.grid(row=3, column=2)

button9 = Button(window, text='')
button9.config(command = lambda m='button9': gameInput(m))
button9.config(font = ('Ink Free', 50, 'bold'))
button9.config(height = 1, width = 2)
button9.grid(row=3, column=3)

window.mainloop() 