from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *


def func_open():
    # messagebox.showinfo("selectMenu", "open in menu selected")
    val = askinteger("확대배수", "주사위숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)
    label1.configure(text=str(val))


def func_exit():
    w.quit()
    w.destroy()


w = Tk()
w.geometry('500x300')

# Label build
label1 = Label(w, text='입력된값 ')
label1.pack()

# Menu Build
mainMenu = Menu(w)
w.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='file', menu=fileMenu)
fileMenu.add_command(label='open', command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='exit', command=func_exit)

# Two Frames build
upFrame = Frame(w)
upFrame.pack()
dnFrame = Frame(w)
dnFrame.pack()

# EditBox build
editBox = Entry(upFrame, width=10, bg='green')
editBox.pack(padx=20, pady=20)

# Listbox build
listbox = Listbox(dnFrame, bg='yellow')
listbox.pack()
listbox.insert(END, '하나')
listbox.insert(END, '둘')

w.mainloop()
# setting - projectname - + - pymysql package install
