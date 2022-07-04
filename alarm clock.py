from tkinter import *
import tkinter as tk
from datetime import datetime
import time
import winsound

root = Tk()

def actual_time(hour_entry,minute_entry,second_entry):

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_hour = now.strftime("%H") 
        current_minute = now.strftime("%M")
        current_second = now.strftime("%S")

        if current_hour == hour_entry:
            if current_minute == minute_entry:
                if current_second == second_entry:      
                    print('Time for alarm')
                    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
#                    freq = 500
#                    dur = 100
#                    winsound.Beep(freq,dur)
                    break

canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

label = Label(frame, text='Alarm Clock', fg='red', bg='black', font='Arial')
label.grid(row=0, column=0)

button = Button(frame, text='Hour', fg='red', bg='black', font='Arial')
button.grid(row=1, column=0)

hour_entry = Entry(frame, bg='pink')
hour_entry.grid(row=2, column=0)

button = Button(frame, text='Minute', fg='red', bg='black', font='Arial')
button.grid(row=1, column=15)

minute_entry = Entry(frame, bg='pink')
minute_entry.grid(row=2, column=15)

button = Button(frame, text='Second', fg='red', bg='black', font='Arial')
button.grid(row=1, column=30)

second_entry = Entry(frame, bg='Pink')
second_entry.grid(row=2, column=30)

button = Button(frame, text='Play Alarm', command=lambda:actual_time(hour_entry.get(),minute_entry.get(),second_entry.get()))
button.grid(row=3, column=1)

root.mainloop()
