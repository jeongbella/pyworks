# 리스트의 연산
score = [80, 70, 90, 75]

# 갯수 - len(리스트)
count = len(score)
print("갯수:", count) #갯수: 4

#합계
total = score[0] + score[1] + score[2] + score[3]
print(total) #315
print(score[0] + score[1]) #150

#합계 - sum(리스트)
total = sum(score)
print("합계:", total) #합계: 315

#평균 = 합계 / 개수
average = total / count
print("평균 :", average)  # 평균 : 78.75

# 최대값 - max(리스트)
max_val =  max(score)
print("최고 점수:", max_val) # 최고점수: 90

# 최소값 - min(리스트)
min_val= min(score)
print("최저 점수:", min_val) #최저 점수: 70

# score = [80, 70, 90, 75]
# 평균 이상인 점수만 골라서 출력하기
for s in score:
    if s >= average:
        print(s) #80, 90
