# 타자 연습 게임
import random
import time

# 외부의 word.txt 파일 읽기
try:
    with open("output/word.txt", 'r', encoding='utf-8') as f:
        word = [line.strip() for line in f]
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
# print(word)
n = 1 #문제 번호

print("[타자 게임] 준비되면 엔터!")
input()

start_time = time.time() # 시작시간

while n <= 10:
    print("문제:", n)
    q = random.choice(word) #word 리스트에서 랜덤하게 단어 추출
    print(q) # 문제

    you = input() # 사용자 입력
    if you == q:
        print("정답!")
        n = n + 1
    else:
        print("오답! 다시 도전!")

end_time = time.time()
es = end_time - start_time
print(f"게임에 걸린 시간: {es:.2f}초")