import random  #random.py를 임포트

# 한번만 랜덤하게 - 시드(seed) 설정
# random.seed(42)  # 시드 설정
print(random.random()) # 0.0 ~ 1.0 사이의 난수 발생

# 1 ~ 10 사이의 난수 발생
print(random.randint(1, 10)) # 1 ~ 10 사이의 난수

# 동전 던지기
# 0이면 앞면, 1이면 뒷면
coin = random.randint(0, 1)
if coin == 0:
    print("앞면")
else:
    print("뒷면")

# 리스트에서 랜덤하게 선택 - choice() 사용
fruits = ["사과", "바나나", "딸기"]
print(random.choice(fruits)) # 리스트에서 랜덤하게 선택

# 랜덤하게 섞기 - shuffle() 사용
random.shuffle(fruits)
print(fruits)

# 1 ~ 45 사이의 로또 번호 6개를 랜덤하게 선택
# 방법1
lotto = [] #빈 리스트

# 6번 반복
while len(lotto) < 6: # 요소의 개수가 6개인 동안
    n = random.randint(1, 45) # 1 ~ 45 사이의 난수 발생
    if n not in lotto: # 중복 방지
        lotto.append(n) # 리스트에 추가
print(lotto) 

# 방법2 - sample() 사용
print(random.sample(range(1, 46), 6))
