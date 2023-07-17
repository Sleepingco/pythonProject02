from tkinter import *
window = Tk()
window.title('윈도우 창 연습')
window.geometry('500x300')
lable1 = Label(window, text='this is Mysql을')
lable1.pack()
lable2 = Label(window, text='열심히', font=('궁서체',30),fg='blue')
lable2.pack()
lable3 = Label(window, text='공부중입니다',bg='magenta',width=20,height=4,anchor=SE)
lable1.pack()


window.resizable(width=FALSE, height=FALSE)
window.mainloop()