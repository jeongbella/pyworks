# 변수
print("hello")

count = 4  #변수의 선언과 초기화(값을 기억)
print("학생수: ", count)

scores = [90, 75, 80, 40] 

x = [1, 2, 3] #리스트의 선언과 초기화
y = [4, 5, 6]

print(x + y) #[1, 2, 3, 4, 5, 6]
print(x * 2) #[1, 2, 3, 1, 2, 3]

# 1 ~ 5까지 리스트에 저장
number = []  #빈 리스트
# number.append(1)
# number.append(2)
for i in range(1, 6):
    number.append(i)
print("number=", number)

# 리스트의 내포
number2 = [i for i in range(1, 6)]
print("number2=", number2)

# 1 ~ 10까지 중에서 짝수만 저장
evens = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)
print("evens=", evens)

# 리스트 내포
evens2 = [x for x in range(1, 11) if x % 2 == 0]
print("evens2=", evens)



