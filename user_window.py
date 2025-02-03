from tkinter import *

def check() : # normalization 
    user_country = user_entry.get().capitalize() 
    
    with open('C:\\Users\\KimoStore\\Desktop\\Countries.txt') as file :
        # file >>> represents the whole countries file
        content = file.read()
        
        if user_country in content :
            title_1['text'] = 'Book now !'
            title_1['fg'] = 'green'
            
        else :
            title_1['text'] = 'the country is not available !'
            title_1['fg'] = 'red'                
            
            
        
        
        
        
    
    


window = Tk()
window.geometry('800x400')

title_1 = Label(window, text = 'enter the country you\n want to travel to', fg = 'red',
                font = ('times new roman', 25))
title_1.place( x = 10, y = 100 )

user_entry = Entry(window, fg = 'black', bg = 'yellow',
                font = ('times new roman', 25) )
user_entry.place( x = 300, y = 100 )

check_button = Button( window, text='click me to\n check the country', bg = 'yellow',
                font = ('times new roman', 25), command= check )
check_button.place(x = 200, y = 250)



window.mainloop()