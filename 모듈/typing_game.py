# 타자 연습 게임
import random
import time

word = ["python", "programming", "challenge", "developer", "algorithm"]
n = 1 #문제 번호

print("[타자 게임] 준비되면 엔터!")
input()

start_time = time.time() # 시작시간

while n <= 5:
    print("문제:", n)
    q = random.choice(word)
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