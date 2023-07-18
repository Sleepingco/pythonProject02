import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root',password='himedia',db='sakila',charset='utf8')
if conn is None:
    print('mysql sakila db 연결실패')
    exit(0)
else:
    print('mysql sakila 연결성공')

cur = conn.cursor()
cur.execute('select num,menuname,price from menu order by num')
while True:
    row = cur.fetchone()  # fetch one record from cursor
    if row is None:
        break
    num = int(row[0]) # 데이터가 넘어올때 문자열로 넘어옴
    name = row[1]
    price = int(row[2])
    print(f'{num:2d} {name:12s} {price:4d}')
conn.close()
