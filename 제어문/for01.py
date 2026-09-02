# 반복문 for 
# range(시작값, 종료값, 중간값)
'''
print(range(5)) #range(0. 5)
print(list(range(5))) #[0,1,2,3,4]
print(list(range(1,6))) #[1,2,3,4,5]

#1부터 5까지 출력
for i in range(1,6,1):
    print (i)
print("반복을 종료합니다")

#1부터 5까지 출력
total = 0
for i in range(1,6,1):
    total = total + i
print("합계:", total)
'''

total = 0
for i in [1,2,3,4,5]:
    total = total + i
print("합계:", total)