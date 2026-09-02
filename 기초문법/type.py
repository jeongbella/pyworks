# 자료형(Data Type)
# 파이썬은 자료형을 명시하지 않음
# type(데이터) 함수로 자료형을 인지

num = 10
pi = 3.14
language= "파이썬"
is_merried = False

print(num)

print(type(num)) # int
print(type(pi)) # float
print(type(language)) # str
print(type(is_merried)) # bool

#형 변환(type conversion)
a="10" 
b=5
# print(a+b) # ""문자로 인식, 에러 : can only concatenate str (not "int") to str

#문자를 정수로 변환하는 함수 - int(문자)
a = int(a)
print(a+b) # 15

#숫자를 문자로 변환하는 함수 - str(숫자)
age = 26
print("나이:" + str(age)) #나이 : 26

#연습문제
x = "7"
y = "3"
print(int(x) + int(y)) #10

x=int(x)
y=int(y)
print(x+y)

'''
# 십진수 -> 이진수 변화 함수 - bin(십진수)
print(bin(33)) #0b100001
print(bin(65)) #0b1000001

# 아스키코드를 문자로 변환하는 함수 - chr(코드)
print(chr(65)) #A
print(chr(33)) #!

#문자를 코드값으로 변환하는 함수 - ord(문자)
print(ord('A')) #65
print(ord('!')) #33
'''

