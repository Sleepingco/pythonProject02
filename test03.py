from tkinter import *
window = Tk()

# button1  = Button(window,text='버튼1')
# button2  = Button(window,text='버튼2')
# button3  = Button(window,text='버튼3')
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)

btnList =[]  # [None,None,None]
for i in range(0, 15):
    btnList.append(Button(window, text='button'+str(i+1)))
for btn in btnList:
    btn.pack(side=RIGHT)
window.mainloop()
