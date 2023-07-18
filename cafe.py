from tkinter import *
from tkinter import messagebox
import pymysql


def initialize():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8')
    if conn is None:
        print('mysql sakila db 연결실패')
        exit(0)
    else:
        print('mysql sakila 연결성공')
    lstMenu.delete(0, END)  # 기존에 있는걸 비우고 새로운 값을 추가
    # 리스트 채움
    cur = conn.cursor()
    cur.execute('select num,menuname,price from menu order by num')
    while True:
        row = cur.fetchone()  # fetch one record from cursor
        if row is None:
            break
        menustr = f'{row[0]:2d},{row[1]},{row[2]:4d}'
        lstMenu.insert(END, menustr)
    conn.close()


def doInsert():
    name = edtName.get()
    price = edtPrice.get()
    if name == '' or price == '':
        messagebox.showerror('NoData', '메뉴명/가격이 입력되지 않았습니다')
        return
    sql = "insert into menu (menuname,price) values ('" + name + "'," + price + ")"

    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8',
                           autocommit=True)
    if conn is None:
        print('mysql sakila db 연결실패')
        exit(0)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        initialize()
    except:
        conn.rollback()
        messagebox.showerror('Insert Error', '데이터 추가 실패')
    else:
        conn.close()


def doDelete():
    name = edtName.get()
    price = edtPrice.get()
    if name == '' or price == '':
        messagebox.showerror('NoData', '메뉴명/가격이 입력되지 않았습니다')
        return
    sql = "delete from menu where menuname = '" + name + "'and price=" + price

    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8',
                           autocommit=True)
    if conn is None:
        print('mysql sakila db 연결실패')
        exit(0)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        initialize()
        edtName.delete(0, END)
        edtPrice.delete(0, END)
    except:
        conn.rollback()
        messagebox.showerror('Insert Error', '데이터 추가 실패')
    else:
        conn.close()


def getMenu(event):
    menuitem = lstMenu.curselection()  # tuple
    menuitem = [lstMenu.get(i) for i in menuitem]
    print(menuitem, len(menuitem))
    menuitem = menuitem[0].split(',')
    edtPrice.delete(0, END)
    edtPrice.insert(0, menuitem[0].strip())
    menuitem = menuitem[0].split(' ')
    edtName.delete(0, END)
    edtName.insert(0, menuitem[1].strip())


w = Tk()
w.geometry('400x200')
w.title('카페주문관리')

lstFrame = Frame(w)
lstFrame.pack()
editFrame = Frame(w)
editFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

lstMenu = Listbox(lstFrame, bg='yellow', width=30, height=10, font='Aerial 12')
lstMenu.bind('<<ListboxSelect>>', getMenu)  # lstMenu를 클리했을 때, 호출되는 getMenu 함수를 결합.
# document.getElementById('lstMenu').addEventListner('click,function(){
# })
# lstOrder = Listbox(lstFrame, bg='aqua',width=30,height=10)
# lstSales = Listbox(lstFrame, bg='cyan',width=30,height=10)
lstMenu.pack(side=LEFT, fill=BOTH, expand=1)
# lstOrder.pack(side=LEFT,fill=BOTH,expand=1)
# lstSales.pack(side=LEFT,fill=BOTH,expand=1)

edtName = Entry(editFrame, width=10, font='Aerial 12')
edtPrice = Entry(editFrame, width=5, font='Aerial 12')
btninsert = Button(editFrame, text='추가', font='Aerial 12', command=doInsert)
btndelete = Button(editFrame, text='삭제', font='Aerial 12', command=doDelete)
edtName.pack(side=LEFT, padx=10)
edtPrice.pack(side=LEFT, padx=10)
btninsert.pack(side=LEFT, padx=10)
btndelete.pack(side=LEFT, padx=10)

initialize()

w.mainloop()
