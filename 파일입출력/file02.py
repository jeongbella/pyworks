# 파일 읽기
# 파일 열기
f = open("data.txt", 'r', encoding="utf-8")

# 파일 읽기
data = f.read()
print(data)

# 파일 종료
f.close()