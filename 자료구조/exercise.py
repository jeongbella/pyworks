# 리스트 [88, 92, 79, 95, 60]에서 평균 이상인 점수만 골라 출력하는 코드
score = [88, 92, 79, 95, 60]

total = sum(score)
print(total) #414

count = len(score)
print(count) #5

average = total / count
print(average) #82.8

max_max=max(score)
print(max_max) #95

min_min=min(score)
print(min_min) #60

#요소 전체 출력
for s in score:
    if s>average:
        print(s) # 88, 92, 95