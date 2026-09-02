# 반복문 - while, break문
# 1부터 5까지 출력
'''
n=1
while True: # break가 없으면 무한반복
    if n > 5:
        break
    print(n)
    n += 1


# 1부터 5까지의 합계
n=1
total = 0
while True:
    if n > 5 :
        break
    total = total + n
    print("n=", n, ", total=", total) #디버그, 로그
    n += 1
print("합계:", total)
'''

#종료가 나올때까지 반복
while True: 
    msg = input("입력('exit'를 입력하면 종료) : ")
    if msg == "exit":
        print("대화를 종료합니다.")
        break
    print("입력된말 :", msg)