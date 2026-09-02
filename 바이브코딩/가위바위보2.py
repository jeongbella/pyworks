import random

# 1. 게임에 사용할 선택지 리스트 정의
choices = ["가위", "바위", "보"]

# 2. 사용자 입력 받기
user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

# 사용자가 올바르게 입력했는지 확인
if user_choice not in choices:
  print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 정확히 입력해주세요.")
else:
  # 3. 컴퓨터의 무작위 선택 (random 모듈 활용)
  computer_choice = random.choice(choices)
  print(f"컴퓨터의 선택: {computer_choice}")

  # 4. 승부 판정 로직 (초보자용 주석 설명)
  # 비기는 경우를 먼저 처리합니다.
  if user_choice == computer_choice:
    print("비겼습니다!")

  # 사용자가 이기는 경우의 수를 조건문(or)으로 묶어줍니다.
  # (가위 vs 보) 또는 (바위 vs 가위) 또는 (보 vs 바위)
  elif (
      (user_choice == "가위" and computer_choice == "보")
      or (user_choice == "바위" and computer_choice == "가위")
      or (user_choice == "보" and computer_choice == "바위")
  ):
    print("축하합니다! 당신이 이겼습니다! 🎉")

  # 위 두 가지 조건(비김, 승리)이 모두 아니라면 나머지는 컴퓨터가 이긴 경우입니다.
  else:
    print("아쉽네요! 컴퓨터가 승리했습니다. 🤖")