from tkinter import *
import tkinter as tk
import random

root = Tk()

def display_selection(result):
    listbox = Listbox(frame, width=50, height=1)
    listbox.grid(row=4, column=0)
    listbox.insert(END, result)
    print('display_selection')
    
def calculate_result(user_choice):
    result = StringVar()
    list = ['Rock', 'Paper', 'Scissors']
    cchoice = random.choice(list)
    print(cchoice)
    answer = ('Computer choice is ' + str(cchoice))
    print(answer)
    print(user_choice)
    pchoice = user_choice
    print(pchoice)

    if (pchoice == cchoice):
        result = ('Computer choice is ' + str(cchoice) + 'Its a draw')
    elif (pchoice == 'Rock' and cchoice == 'Paper'):
        result = ('Computer choice is ' + str(cchoice) + 'Paper covers Rock,\n Computer Wins')

    elif (pchoice == 'Rock' and cchoice == 'Scissors'):
        result = ('Computer choice is ' + str(cchoice) + 'Rock smashes Scissors,\n Player Wins')

    elif (pchoice == 'Paper' and cchoice == 'Rock'):
        result = ('Computer choice is ' + str(cchoice) + 'Paper covers Rock,\n Player Wins')

    elif (pchoice == 'Paper' and cchoice == 'Scissors'):
        result = ('Computer choice is ' + str(cchoice) + 'Scissors cuts Paper,\n Computer Wins')

    elif (pchoice == 'Scissors' and cchoice == 'Paper'):
        result = ('Computer choice is ' + str(cchoice) + 'Scissors cuts Paper,\n Player Wins')

    elif (pchoice == 'Scissors' and cchoice == 'Rock'):
        result = ('Computer choice is ' + str(cchoice) + 'Rock smashes Scissors,\n Player Wins')

    display_selection(result)

canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

label = Label(frame, text='Rock-Paper-Scissors \n Player Vs Computer')
label.grid(row=0, column=0)

label = Label(frame, text='Player, please enter anyone of the choices') 
label.grid(row=1, column=0)

user_choice = Entry(frame)
user_choice.grid(row=1,column=1)

button = Button(frame, text='Result', command=lambda:calculate_result(user_choice.get()))
button.grid(row=2, column=1)

root.mainloop()
