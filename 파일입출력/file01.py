# 파일 쓰기(저장)
# 1. 파일 열기
f = open("data.txt", 'w', encoding="utf-8")

# 2. 파일 쓰기
f.write("안녕하세요\n")
f.write("1500\n") #숫자는 쓸수 없어서 문자로 변환 저장
f.write("This is a bag.\n")
num = 2700
f.write(str(num) + '\n')

# 3. 파일 종료
f.close()
