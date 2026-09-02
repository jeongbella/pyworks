# 딕셔너리로 회원 정보(이름, 나이, 도시)를 만들고, 나이를 한 살 늘린 뒤 "이름님은 도시에 사는 나이살입니다." 형태로 출력하세요.

member = {"name" : "꾸꾸", "age" : 13, "city" : "서울"}
print(member)

member["age"] += 1
print(member) 

print(member["name"],"님은", member["city"], "에 사는", member["age"], "살 입니다.") # 꾸꾸 님은 서울 에 사는 14 살 입니다.
print(f'{member["name"]}님은 {member["city"]}에 사는 {member["age"]}살 입니다.')   # 꾸꾸님은 서울에 사는 14살 입니다.

