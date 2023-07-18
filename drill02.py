import pymysql

# Python/MySQL연동과제 : student테이블 출력
conn = pymysql.connect(host='127.0.0.1', user='root', password='himedia', db='drill', charset='utf8')
if conn is None:
    print('mysql sakila db 연결실패')
    exit(0)
else:
    print('mysql sakila 연결성공')

cur = conn.cursor()
cur.execute("select a.employee_id,a.emp_name,ifnull(b.emp_name,'-') Manager_name,ifnull(c.department_name,'-') "
            "from employees a left join employees b on a.manager_id = b.employee_id"
            " left join departments c on a.department_id = c.department_id")
while True:
    row = cur.fetchone()  # fetch one record from cursor
    if row is None:
        break
    # num = int(row[0])  # 데이터가 넘어올때 문자열로 넘어옴
    # name = row[1]
    # manager = row[2]
    # dept = row[3]
    # print(f'{num:3d} {name:20s} {manager:20s} {dept:20s}')
    for x in row:
        print(x,',',end='')
    print('')
conn.close()
# count와 같이 함수 이름이 컬럼으로 들어 갈떄는 컬럼에 이름을 붙혀주는게 좋다
