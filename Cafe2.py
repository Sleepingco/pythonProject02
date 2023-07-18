from tkinter import *
from tkinter import messagebox
import pymysql


def initialize():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8',
                           autocommit=True)
    if conn is None:
        print('MySQL Sakila DB 연결 실패')
        exit(0)

    lstMenu.delete(0, END)
    lstData = []
    cur = conn.cursor()
    cur.execute("select ifnull(num,0),ifnull(menuname,'-'),ifnull(price,0) from menu order by num")
    while True:
        row = cur.fetchone()  # fetch one record from cursor
        if row is None:
            break
        menustr = f'{row[0]:2d} {row[1]:10s}, {row[2]:4d}'
        lstMenu.insert(END, menustr)
    conn.close()


def doInsert():
    name = edtName.get()
    price = edtPrice.get()
    if name == '' or price == '':
        messagebox.showerror('No data', '메뉴명/가격이 입력되지 않았습니다')
        return
    sql = "insert into menu (menuname,price) values ('" + name + "'," + price + ")"
    print(sql)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8',
                           autocommit=True)
    if conn is None:
        print('MySQL Sakila DB 연결 실패')
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


def doDelete():
    name = edtName.get()
    price = edtPrice.get()
    if name == '' or price == '':
        messagebox.showerror('No data', '메뉴명/가격이 입력되지 않았습니다')
        return
    sql = "delete from menu where menuname='" + name + "' and price=" + price
    print(sql)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='sakila', charset='utf8',
                           autocommit=True)
    if conn is None:
        print('MySQL Sakila DB 연결 실패')
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
    menuitem = [lstMenu.get(i).strip() for i in menuitem]
    print(menuitem, len(menuitem))
    menuitem = menuitem[0].split(',')
    edtPrice.delete(0, END)
    edtPrice.insert(0, menuitem[1].strip())
    menuitem = menuitem[0].split(' ')
    edtName.delete(0, END)
    edtName.insert(0, menuitem[1].strip())


w = Tk()
w.geometry('500x300')
w.title('메뉴관리')

lstFrame = Frame(w)
lstFrame.pack()
edtFrame = Frame(w)
edtFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

lstMenu = Listbox(lstFrame, bg='yellow', width=40, font=('맑은고딕 18'))
lstMenu.bind('<<ListboxSelect>>', getMenu)  # lstMenu를 클릭했을 때, 호출되는 getMenu 함수를 결합.

# lstOrder = Listbox(lstFrame, bg='aqua', width=40)
# lstSales = Listbox(lstFrame, bg='cyan', width=40)
lstMenu.pack(side=LEFT, fill=BOTH, expand=1)
# lstOrder.pack(side=LEFT, fill=BOTH, expand=1)
# lstSales.pack(side=LEFT, fill=BOTH, expand=1)

edtName = Entry(edtFrame, width=10, font=('맑은고딕 18'))
edtPrice = Entry(edtFrame, width=5, font=('맑은고딕 18'))
btnInsert = Button(edtFrame, text='추가', font=('맑은고딕 18'), command=doInsert)
btnDelete = Button(edtFrame, text='삭제', font=('맑은고딕 18'), command=doDelete)

edtName.pack(side=LEFT, padx=10)
edtPrice.pack(side=LEFT, padx=10)
btnInsert.pack(side=LEFT, padx=10)
btnDelete.pack(side=LEFT, padx=10)

initialize()

w.mainloop()
