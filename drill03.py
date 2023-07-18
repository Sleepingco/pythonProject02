import pymysql
# 각 부서별 월급합계 (부서명, 월급합계)
conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='drill', charset='utf8')
if conn is None:
    print('mysql drill db 연결실패')
    exit(0)
else:
    print('mysql drill 연결성공')

cur = conn.cursor()
cur.execute("select a.department_name , ifnull(sum(b.salary),'0.0') sal from departments a left join employees b on a.department_id = b.department_id group by a.department_name")
while True:
    row = cur.fetchone()  # fetch one record from cursor
    if row is None:
        break
    dept = row[0]  # 데이터가 넘어올때 문자열로 넘어옴
    sal = float(row[1])
    print(f'{dept:7s}, {sal:7.2f}')

conn.close()