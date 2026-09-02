# 문자열 - string
# 인덱싱 - 1개 추출, 슬라이싱 - 여러개추출
a = ["s", "k", "y"]
print(a[0]) # s

s = "python"
print(s[0]) # p
print(s[0:2]) # py #2-1=1. 0:1을 나타냄
print(s[:3]) # pyt 0 1 2 추출
print(s[2:]) # thon
print(s[:-1]) # pytho

#spilt(구분기호) - 문자열을 리스트로 변환
fruit = "banana, grape, apple"
furit_list = fruit.split(',') #새로운 변수정의, fruit을 split 해서 fruit_list로 정의
print(furit_list) #['banana', ' grape', ' apple']
print(furit_list[0]) #banana

# replace() - 문자 수정(대체)
msg = "hello, world"
print(msg) # hello, world

msg = msg.replace("world", "korea")
print(msg) # hello, korea

#공백제거 strip()
msg2 = " hi, jun "
msg2 = msg2.strip()
print(msg2) #'hi, jun'

# 실습문제 9-1 : 이메일 "user@naver.com"에서 @를 기준으로 나눠 아이디(user)와 도메인(naver.com)을 각각 출력하세요
email = "user@naver.com"
data=email.split("@") #data에 새로운 변수 지정
print(data) # ['user', 'naver.com']
id=data[0]
domain=data[1]
print(f'아이디:{id}', ",",f'도메인:{domain}') # 아이디:user , 도메인:naver.com
print("아이디:", id) # 아이디: user
print("도메인:", domain) # 도메인: naver.com