import sqlite3

# DB에 연결 - connect(db경로)
conn = sqlite3.connect("c:/pydb/mydb.db")
print(conn, "데이터베이스 연결 성공!")

# 필수 요소
# 1. connect() 2. cursor() 3. excute()
# 자료 검색(sql 언어 사용)
def select():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        # 데이터 가져옴
        rows = cursor.fetchall() # 리스트로 반환
        # print(rows) 
        for row in rows:
            print(row)

#  자료 삽입
def insert():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor()
        sql = "INSERT INTO emp(id, name, salary) VALUES ('e201', '김대리', 4000000)"
        cursor.execute(sql)
        conn.commit() # 작업 완료
        print("직원 추가 완료!")

# 특정한 자료 검색
def select_one():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM emp WHERE name = '박사원'"
        cursor.execute(sql)
        #  데이터 1건 가져오기
        row = cursor.fetchall()
        print(row)

def update():
    with sqlite3.connect("c:/pydb/mydb.db") as conn:
            cursor = conn.cursor()
            sql = "UPDATE emp SET name = '장그레' " \
            "WHERE id = 'e101'"
            cursor.execute(sql)
            conn.commit() # 작업 완료
            print("직원 수정 완료!")


#  함수 호출
# insert()
update()
select()
# select_one()


