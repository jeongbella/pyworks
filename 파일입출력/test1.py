# 실습 2-1 메모 저장하기
try:
    f = open("memo.txt", "w", encoding="utf-8")
    f.write("파이썬은 재미있다\n매일 조금씩\n꾸준히\n")
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 파일 읽기
try:
    f = open("memo.txt", "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")