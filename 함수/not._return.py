# 사용자 정의 함수
# 함수 정의 및 호출

def greet():
    print("안녕하세요")

def greet_n(name):
    print(f'{name}님 안녕하세요!')

greet() #호출
greet_n("야옹")

# 연습문제 : 이름과 나이를 매개변수로 받아 "OOO님은 OO살입니다."를 출력하는 함수 info를 만들고, 서로 다른 값으로 두 번 호출하세요.
def info(name, age):
    print(f'{name}님은 {age}살 입니다.')

info("꾸꾸", 12)
info("야옹", 14)