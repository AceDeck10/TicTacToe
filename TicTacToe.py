from tkinter import *

# Turn variables. Used to determine turns
global turn
turn = 'X'

# game input function
def gameInput(buttonPress):
    if(buttonPress == 'button1'):
        button1.config(text = turn)
        button1.config(state = DISABLED)
    elif(buttonPress == 'button2'):
        button2.config(text = turn)
        button2.config(state = DISABLED)
    elif(buttonPress == 'button3'):
        button3.config(text = turn)
        button3.config(state = DISABLED)
    elif(buttonPress == 'button4'):
        button4.config(text = turn)
        button4.config(state = DISABLED)
    elif(buttonPress == 'button5'):
        button5.config(text = 'X')
        button5.config(state = DISABLED)
    elif(buttonPress == 'button6'):
        button6.config(text = turn)
        button6.config(state = DISABLED)
    elif(buttonPress == 'button7'):
        button7.config(text = turn)
        button7.config(state = DISABLED)
    elif(buttonPress == 'button8'):
        button8.config(text = turn)
        button8.config(state = DISABLED)
    elif(buttonPress == 'button9'):
        button9.config(text = turn)
        button9.config(state = DISABLED)
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