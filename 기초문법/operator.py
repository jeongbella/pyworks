# 산술 연산자

n1 = 7 # 대입연산자 ('=')
n2 = 2

print(n1 + n2, n1-n2, n1*n2) #9 5 4
print(n1 /n1) #나누기 1.0
print(n1 // n2) #몫 3
print(n1 % n2) #나머지 1 
print(n1 ** n2) #거듭제곱 49

#빵 30개를 4명이 나눠 가질 때, 한 사람이 몇 개씩 갖고(몫) 몇 개가 남는지(나머지)를 계산해 출력하세요.

#몫과 나머지 구하기
#변수 선언과 초기화
bread= 30
people=4

#계산(연산)
share = bread // people #몫
remain = bread % people #나머지

#출력
print("한사람 몫:", share,"개") # 한사람 몫: 7 개
print(f"한사람 몫: {share}개") #한사람 몫: 7개
print("남는빵:", remain,"개") # 남는빵: 2 개
print(f"남는빵: {share}개")  #남는빵: 7개

'''
#복합 대입 연산자
count = 10
count += 2 # count = count + 2
print(count) # 12

count -= 1 #count = count - 2 #12-2 = 10 / 오른쪽부터 계산 후 왼쪽 대입
print(count) # 10

count *= 1 #count = count * 1  #10 = 10*2
print(count) # 20

count /= 1 #count = count / 1  #20 = 10/2
print(count) #10.0 (나누기는 실수로 출력됨)

'''

# 비교 연산자
a = 3
b = 4
print(a > b) #False
print(a < b) #True
print(a == b) #False
print(a != b)  #True

# 논리연산자 - and, or, not
result = (a < b) and (a ==b)
print(result) # T and F ,False

result = (a < b) or  (a ==b)
print(result) # T or F , True

result =  not(a != b) 
print(result) # not T, False
