import pymysql
 # 매니저별 인원수,월급합계 (매니저명,인원수,월급합계)
conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='drill', charset='utf8')
if conn is None:
    print('mysql drill db 연결실패')
    exit(0)
else:
    print('mysql drill 연결성공')

cur = conn.cursor()
cur.execute("select ifnull(a.emp_name,'none') manager, count(*) howmany, sum(b.salary) sal from employees a inner join employees b on a.employee_id = b.manager_id group by b.manager_id")
while True:
    row = cur.fetchone()  # fetch one record from cursor
    if row is None:
        break
    for x in row:
        print(x,', ',end='')
    print('')

conn.close()