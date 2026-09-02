# 파일에 리스트 자료로 저장(쓰기)하기
fruits = ["포도", "딸기", "참외", "토마토"]
with open("output/fruits.txt", 'w', encoding='utf-8') as f:
    for fruit in fruits:
        f.write(fruit + '\n')

# 파일 읽기 - 자료를 리스트에 담기
with open("output/fruits.txt", 'r', encoding='utf-8') as f:
    '''lines = []
    for line in f:
        # strip()은 공백 제거 기능
        lines.append(line.strip())'''
    lines = [line.strip() for line in f]
print(lines) #['포도', '딸기', '참외', '토마토']