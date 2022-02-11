from __future__ import division # This is to return float results in division
from tkinter import *

window = Tk()
window.title("My calculator")
window.geometry("320x150")

#variable to contain unprocessed user input
userInput =''
displayText = StringVar()

#functions
def click(value):
    global userInput
    userInput = userInput + str(value)
    displayText.set(userInput)

def deleteLast():
    global userInput
    userInput = userInput[:-1]
    displayText.set(userInput)

def equals():
    global userInput
    #evaluate the userInput into a number then convert it to a string for further operations
    userInput = str(eval(userInput))
    displayText.set(userInput)

def clear():
    global userInput
    userInput = ''
    displayText.set(userInput)

# Frame to contain the input field
input_frame = Frame(window, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack()

# Input | display
display = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = displayText, width = 50, bg = "#eee", bd = 0, justify = RIGHT,state=DISABLED)
display.pack()

#buttons
buttons = Frame(window)
buttons.pack()
buttonWidth=4
buttonHeight=0

row =0
one = Button(buttons,text = '1', width=buttonWidth,height=buttonHeight,command= lambda : click(1)).grid(row = row)
two = Button(buttons,text = '2', width=buttonWidth,height=buttonHeight,command= lambda : click(2)).grid(row = row,column = 1)
three = Button(buttons,text = '3', width=buttonWidth,height=buttonHeight,command= lambda : click(3)).grid(row = row,column = 2)
delete =Button(buttons,text = 'DEL', width=buttonWidth,height=buttonHeight,command= lambda : deleteLast()).grid(row = row,column = 3)
clearDisplay = Button(buttons,text = 'C', width=buttonWidth,height=buttonHeight,command= lambda : clear()).grid(row = row,column = 4)

row = 1
four = Button(buttons,text = '4', width=buttonWidth,height=buttonHeight,command= lambda : click(4)).grid(row = row)
five = Button(buttons,text = '5', width=buttonWidth,height=buttonHeight,command= lambda : click(5)).grid(row = row,column = 1)
six = Button(buttons,text = '6', width=buttonWidth,height=buttonHeight,command= lambda : click(6)).grid(row = row,column = 2)
multiply = Button(buttons,text = '*', width=buttonWidth,height=buttonHeight,command= lambda : click('*')).grid(row = row,column = 3)
divide = Button(buttons,text = '/', width=buttonWidth,height=buttonHeight,command= lambda : click('/')).grid(row = row,column = 4)

row = 2
seven = Button(buttons,text = '7', width=buttonWidth,height=buttonHeight,command= lambda : click(7)).grid(row = row)
eight = Button(buttons,text = '8', width=buttonWidth,height=buttonHeight,command= lambda : click(8)).grid(row = row,column = 1)
nine = Button(buttons,text = '9', width=buttonWidth,height=buttonHeight,command= lambda : click(9)).grid(row = row,column=2)
plus = Button(buttons,text = '+', width=buttonWidth,height=buttonHeight,command= lambda : click('+')).grid(row = row,column = 3)
minus = Button(buttons,text = '-', width=buttonWidth,height=buttonHeight,command= lambda : click('-')).grid(row = row,column = 4)

row = 3
zero = Button(buttons,text = '0', width=buttonWidth,height=buttonHeight,command= lambda : click(0)).grid(row = row)
dot = Button(buttons,text = '.', width=buttonWidth,height=buttonHeight,command= lambda : click('.')).grid(row = row,column = 1)

equal = Button(buttons,text = '=', width=buttonWidth,height=buttonHeight,command= lambda : equals()).grid(row = row,column = 4)
  
window.mainloop()
