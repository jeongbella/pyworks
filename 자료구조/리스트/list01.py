# 리스트 - 여러개의 데이터를 저장하는 자료구조
# 변수 - 한 개의 데이터를 저장하는 공간(변경가능
cart1 = "포도"
cart2 = "커피"
print(cart1, ",",cart2)

#리스트의 특징
#순서가 있다. 0부터 시작, 포도=0
#중복 가능
carts = ["포도", "커피", "바나나", "달걀"]
print(carts) #["포도", "커피", "바나나", "달걀"]

print(type(carts)) #<class 'list'>

# 특정 요소 조화(접근)
print(carts[0]) # 포도
print(carts[1]) # 커피
print(carts[2]) # 바나나
print(carts[2]) # 달걀

print(carts[-1]) # 달걀, 맨 뒤부터 -1
print(carts[-2]) # 바나나
print(carts[-3]) # 커피
print(carts[-4]) # 포도

# 요소 변경(수정)
carts[2] = "토마토" #바나나가 토마토로 변경
print(carts) # ['포도', '커피', '토마토', '달걀']

# 요소삭제
del carts[1] #커피 삭제
print(carts) # ['포도', '토마토', '달걀']

#  요소 유무 판단
print("달걀" in carts) # True
print("양파" in carts) # False
print("양파" not in carts) # True

# 전체 요소 출력
for cart in carts:
    print(cart)