# "안녕하세요!"를 3번 출력
# 1.while문

num = 1
while num <= 3:
    print("안녕하세요")
    num = num + 1
print("반복종료")

#2. for 문
for x in range(3): #range(0,3) - 0 1 2
    print("안녕하세요")

# 구구단 - 3 x 1 = 3 
dan = 3
for i in range(1, 10):
    print(dan, "x", i, "=", dan*i)


# 구구단 - 3 x 1 = 3 
dan = int(input("단을 입력하세요:"))
for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")


# 구구단 - 3 x 1 = 3 
dan = input("단을 입력하세요:") #int가 없으면.... 7 x 8 = 77777777
for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")

