#중첩 for (nested for)
#5행 5열
for i in range(1, 6):
    for j in range(1, 6): #1~5
        print('가', end='')  # 가가가가가가가가가가가가가가가가가가가가가가가가가
    print() #줄바꿈
print("-----------")

for i in range(5): # 0~4
    for j in range(5):
        print('가', end='')  
    print() #줄바꿈
print("-----------")

for i in range(5): # 0~4
    for j in range(5):
        print('*', end='')  
    print() #줄바꿈
print("-----------")

# 구구단 전체 출력
for i in range(2,10):
    for j in range(2,10):
        print(f"{i} x {j} = {i*j}")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')  
    print() #줄바꿈
print("-----------")


'''
i=1
 j=1
j=2
 j=1
 j=2

'''

#역삼각형 출력
n = 5
for i in range(1, n + 1):
    # 공백 출력
    for j in range(n - i):
        print(" ", end="")

    # 별 출력
    for j in range(i):
        print("*", end="")

    # 한 줄 끝나면 줄바꿈
    print()


for i in range(1, 6):
    # 공백 출력
    for j in range(5 - i):
        print(" ", end="")

    # 별 출력
    for j in range(i):
        print("*", end="")

    # 한 줄 끝나면 줄바꿈
    print()