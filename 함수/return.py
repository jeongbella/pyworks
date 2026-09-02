# return이 있는 함수
# 제곱수 계산하는 함수
def square(x):
    return x * x

# 두 수의 합을 구하는 함수
def add(x,y):
    return x+y

value = square(4) # 호출
print(value)

value2 = add(10,20)
print(value2)

# 원의 넓이를 계산하는 함수
def circle_area(r):
    return 3.14 * r * r

c_area = circle_area(5)
print ("원의 넓이:", c_area)