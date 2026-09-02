# 리스트

fruit = "grape" # 문자열을 저장하는 변수
print(fruit)

fruits = ["grape", "apple", "strawberry"] #리스트
print(fruits)

# 순서 - 앞에서부터 0 1 2 , 뒤에부터 -1 -2 -3
print(fruits[1])
print(fruits[-2])

# 요소 추가(맨 뒤) 함수 - append()
fruits.append("kiwi")
print(fruits) # ['grape', 'apple', 'strawberry', 'kiwi']

# 요소 삭제 - remove()
fruits.remove("strawberry")
print(fruits) #['grape', 'apple', 'kiwi']

#요소 수정
fruits[1] = 'banana'
print(fruits) #['grape', 'banana', 'kiwi']

# 전체 요소 출력(목록)
for f in fruits:
    print(f)

# 숫자 리스트 만들기
num = [] #빈 리스트
num.append(10)
num.append(20)
num.append(30)
print(num) # [10, 20, 30]

# 20을 삭제
num.remove(20)
print(num) # [10, 30]

# 빈 리스트 cart를 만들고 "우유", "빵", "계란"을 순서대로 추가한 뒤, "빵"을 삭제하고 결과를 출력하세요.
cart = []
cart.append("우유")
cart.append("빵")
cart.append("계란")
print(cart) # ['우유', '빵', '계란']

# cart.remove("빵")
cart.pop() #맨 뒤 삭제 "빵"
print(cart) #['우유', '계란']

#커피,과자
# cart.append("커피","과자") #오류, 하나(요소)만 추가, 두개 불가 
cart.extend(["커피","과자"]) #여러개)(리스트) 가능


# 전체 요소 출력
# i = 변수, in 다음에 리스트
for i in cart: 
    print(i) # 우유 // 계란

for i in cart: 
    print(i, end=" ") # 공백문자, 따옴표 사이 공백, 우유 계란

# 공백 출력
for i in cart: 
    print(i, end="") # 우유계란