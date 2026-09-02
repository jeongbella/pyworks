#입력 처리 - input()
name = "우영우"
age = 31
print(type(age)) #int 숫자

# name =  input("이름 입력 : ")
'''
print("이름을 입력하세요:") #다음줄에 입력
name = input()


# name = input("이름 입력:") #같은줄에 입력
age = input("나이 입력:")

print(type(age)) #str 문자 '31'

age = int(input("나이 입력:"))  #int 숫자 31


#출력 1
print("나이:" + str(age)) # 문자는 문자끼리 연결

#출력 2
print("나이:", (age))

#출력 3
print(f"나이: {age}")
'''

#사각형의 넓이 계산
# 넓이(area) = 가록(w), 세로(h)
'''
w = 5
h= 4

area = w * h

print("사각형의 넓이:", area)



w = input("가로")
h= input("세로")

area = w * h #문자*문자 // 입력받은 숫자는 문자 타입으로 숫자로 변환 필요

print("사각형의 넓이:", area)
'''
w = int(input("가로:"))
h= int(input("세로:"))

area = w * h 

print("사각형의 넓이:", area) #5*5=25

#float(문자) -> 실수형으로 변환
w = float(int(input("가로:")))
h= float(int(input("세로:")))

area = w * h #5*5=25.0

print("사각형의 넓이:", area)

