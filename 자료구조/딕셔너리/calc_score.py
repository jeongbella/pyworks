# 학생 성적표 프로그램
student_list = [
    {"name" : "이대한", "kor" : 95, "eng" : 80, "math" : 80},
    {"name" : "박빈국", "kor" : 80, "eng" : 75, "math" : 75}, # alt+ shift + 방향키아래로 = 복사
    {"name" : "오상식", "kor" : 90, "eng" : 85, "math" : 90},
]

# 학생 리스트 출력
print("첫 번째 학생 검색 :", student_list[0]) # 첫 번째 학생 검색 {'name': '이대한', 'kor': 95, 'eng': 80, 'math': 80}
print("첫 번째 학생의 이름 :", student_list[0]["name"]) # 첫 번째 학생의 이름 : 이대한
print("첫 번째 학생의 국어점수 :", student_list[0]["kor"]) # 첫 번째 학생의 국어점수 : 95

#평균 : 총점 / 과목수
print("******* 학생 성적표 *******")
print("이름\t국어\t영어\t수학\t평균")
for student in student_list:
    name = student["name"]
    kor = student["kor"]
    eng = student["eng"]
    math = student["math"]
    total = kor + eng + math #총점
    average = total / (len(student)-1) # 평균 = 총점/과목수 : 이름 항목 제외 '-1'
    print(f"{name}\t{kor}\t{eng}\t{math}\t{average:.2f}") # .2f : 소수점 둘째자리, .1f : 소수점 첫째자리


