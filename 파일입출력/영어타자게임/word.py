# 영어 단어 쓰기
words = ["python", "programming", "challenge", "developer", "algorithm"]
try:
    with open("output/word.txt", 'w', encoding='utf-8') as f:
        for word in words:
            f.write(word + '\n')
except FileNotFoundError:
    print('파일을 열 수 없습니다.')