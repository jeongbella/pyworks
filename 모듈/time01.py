import time  #time.py

# 1970년 1월 1일 자정부터 지금까지의 시간을 초로 환산
print(time.time()) #1787138113.344514 

# 일로 환산
days = round(time.time() / (24 * 60 * 60)) #20684
print(days)

years = round(days / 365)
print(years) #57

# 시간 대기(지연)
'''
print("3초 후에 메시지가 출력됩니다...")
time.sleep(3)
print("3초가 지났습니다.")
'''

# 0.5초 간격으로 1 ~ 10까지 출력 
for i in range(1, 11):
    time.sleep(0.5)
    print(i)