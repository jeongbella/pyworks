import random

# 가위, 바위, 보를 숫자로 표현합니다. (0: 가위, 1: 바위, 2: 보)
choices = ["가위", "바위", "보"]


def judge(user, computer):
    """user와 computer는 choices 리스트의 인덱스(0,1,2)입니다."""
    # 같은 것을 냈으면 비긴 것
    if user == computer:
        return "무승부"

    # 가위바위보는 "내가 낸 것 + 1 == 상대가 낸 것" 이면 내가 이기는 규칙입니다.
    # 예) 가위(0)는 보(2)를 이기지 못하고 바위(1)를 이깁니다 -> 0 + 1 == 1
    #     바위(1)는 가위(0)를 이깁니다 -> 1 + 1 == 2(보) 가 아니라 가위(0)를 이기는 규칙이라
    #     인덱스 순서를 (가위=0, 바위=1, 보=2)로 정했을 때
    #     "다음 순서인 사람이 이긴다" 규칙을 3으로 나눈 나머지로 표현할 수 있습니다.
    if (user + 1) % 3 == computer:
        # 사용자가 낸 것의 다음 순서가 컴퓨터가 낸 것이면 컴퓨터가 이김
        return "패배"
    else:
        # 그 외의 경우는 사용자가 이김
        return "승리"


def get_user_choice():
    while True:
        user_input = input("가위, 바위, 보 중 하나를 입력하세요: ").strip()
        if user_input in choices:
            return choices.index(user_input)
        print("잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해 주세요.")


def main():
    print("=== 가위바위보 게임 ===")

    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)  # 컴퓨터는 무작위로 선택

    print(f"나: {choices[user_choice]} / 컴퓨터: {choices[computer_choice]}")

    result = judge(user_choice, computer_choice)
    print(f"결과: {result}!")


if __name__ == "__main__":
    main()
