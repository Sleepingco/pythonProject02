import pymysql
# Python/MySQL연동과제 : student테이블 출력
conn = pymysql.connect(host='127.0.0.1', user='root',password='himedia',db='sakila',charset='utf8')
if conn is None:
    print('mysql sakila db 연결실패')
    exit(0)
else:
    print('mysql sakila 연결성공')

cur = conn.cursor()
cur.execute("select ifnull(num,'-')num,ifnull(name,'-')name,ifnull(gender,'-')gender,ifnull(mobile,'-')mobile,"
            "ifnull(birthday,'-')birthday,ifnull(school,'-')school from student order by num")
while True:
    row = cur.fetchone()  # fetch one record from cursor
    if row is None:
        break
    num = int(row[0]) # 데이터가 넘어올때 문자열로 넘어옴
    name = row[1]
    gender = row[2]
    mobile = row[3]
    birthday = row[4]
    school = row[5]
    print(f'{num:3d} {name:12s} {gender:1s}{mobile:20s}{birthday:8s}{school:32s}')
conn.close()
