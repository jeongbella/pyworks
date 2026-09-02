# 구구단 전체 파일 쓰기
try:
    with open("output/gugudan.txt", 'w', encoding='utf-8') as f:
        for i in range(2, 10):
            for j in range(1, 10):
                f.write(f"{i} x {j} = {i * j}\n")
            f.write('\n')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 파일 읽기
try:
    with open("output/gugudan.txt", 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")