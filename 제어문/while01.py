# 반복문 - while문
# 1부터 5까지 출력(시작값 1, 종료값 5, 증가값 1)
n = 1 #시작값
while n <= 5:
    print(n)
    n = n + 1
print("반복을 종료합니다.")

# 1부터 5까지 합계 구하기 (시작값 1, 종료값 5, 증가값 1)
#1 1+2+3+4+5
n=1 # 반복 변수
total=0 #합계 변수
while  n <= 5:
    total = total + n
    n = n + 1
print("합계:", total)

n=1 # 반복 변수
total=0 #합계 변수
while  n <= 5:
    total += n # totla = total + n // 복합연산자
    n +=  1 # n = n+1
print("합계:", total)