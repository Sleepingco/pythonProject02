from tkinter import *
from tkinter import messagebox


def clickbutton():
    messagebox.showinfo('Press the Button', 'Button Pressed')


window = Tk()
window.geometry('200x200')

button1 = Button(window, text='요기요', fg='red', bg='yellow', command=clickbutton)
button1.pack(expand=1)
window.mainloop()
# wxformbuilder 윈도우 디자인 가능
