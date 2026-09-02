# 딕셔너리(dictionary) - 여러개의 값을 저장
# 키(key)와 값(value)의 쌍
# 중괄호 - {}

student  = {
    "name" : "한강", 
    "age" : 21,
    "university" : "한국대학교"
}

print(student) # {'name': '한강', 'age': 21, 'univerticy': '한국대학교'}
print(type(student)) # <class 'dict'>

# 요소에 접근 - 요소에 접근할떄는 key로 검색
print(student["name"]) # 한강
print(student["age"]) # 21

# 요소 조회(get(key)) 무언가를 가져올때 // 무언가를 저장할때 set
print(student.get("university")) # 한국대학교

#요소 추가
student["major"] = "전자공학과"
print(student) # {'name': '한강', 'age': 21, 'university': '한국대학교', 'major': '전자공학과'}

# 요소 수정
student["age"] = 25
print(student)



print(student.keys()) # dict_keys(['name', 'age', 'university', 'major'])
print(student.values()) # dict_values(['한강', 25, '한국대학교', '전자공학과'])

# for문 사용
for key in student.keys():
    print(key) #name / age / univesity / major


for key in student.keys():
    print(key, ':', student[key]) # name : 한강/  age : 25 / university : 한국대학교 / major : 전자공학과

#요소삭제 
student.pop("major")
for key in student.keys():
    print(key, ':', student[key]) # name : 한강/  age : 25 / university : 한국대학교


