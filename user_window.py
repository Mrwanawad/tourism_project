from tkinter import *


window = Tk()
window.geometry('800x400')

title_1 = Label(window, text = 'enter the country you\n want to travel to', fg = 'red',
                font = ('times new roman', 25))
title_1.place( x = 10, y = 100 )

user_entry = Entry(window, fg = 'black', bg = 'yellow',
                font = ('times new roman', 25) )
user_entry.place( x = 300, y = 100 )

check_button = Button( window, text='click me to\n check the country', bg = 'yellow',
                font = ('times new roman', 25) )
check_button.place(x = 200, y = 250)



window.mainloop()