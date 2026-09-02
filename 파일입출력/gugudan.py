# with ~ as 구문은 close()를 사용하지 않음
# 파일에 구구단 쓰기
try:
    with open("output/gugu.txt", 'w', encoding='utf-8') as f:
        dan = 3 # 단을 저장
        for i in range(1, 10):
            f.write(f"{dan} x {i} = {dan * i}\n")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")