# 딕셔너리 자료 구조
dic = {} #빈 딕셔너리 생성
dic[1] = 'a'
dic[2] = 'b'
dic[3] = 'c'

print(dic) #{1: 'a', 2: 'b', 3: 'c'}
print(type(dic)) #<class 'dict'>

# 예제
carts = {1: "양말", 2: "여름바지", 3: "손수건"}
# 2번 키의 값 출력
print(carts[2])

# 수정(key로 검색)
carts[3] = "반팔티"
print(carts) #{1: '양말', 2: '여름바지', 3: '반팔티'}

# for문 전체 출력
for key in carts.keys():
    print(key, ":", carts[key])
