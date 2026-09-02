# 변수의 유효 범위
def click_a():
    x = 0 # 지역(local)변수 , 괄호안에 있으면 매개변수
    x = x+1
    print("x =", x)

click_a() # x = 1
click_a() # x = 1
click_a() # x = 1

#전역변수
quantity = 2 # 전역변수 - 지역까지 영향을 미친다...
def get_price():
    price = 1000 * quantity #price는 지역(local)변수
    print(f'{quantity}개에 {price}원 입니다.')

get_price() # 2개에 2000원 입니다. // 한번호출하면 사라짐
print(quantity) # 2
# print(price) # 위에서 이미 한번 호출했기에 이미 소멸한 변수이므로 오류 발생, 값 정의 필요. NameError: name 'price' is not defined. Did you mean: 'print'?

'''
age = 21
print(age) #age 값을 줘서 출력 가능
'''

# 값이 유지되는 변수
def click_b():
    global x #지역변수가 전역변수화 함
    x += 1
    print("x =", x)

x= 0 # 전역변수()

click_b() # x = 1
click_b() # x = 2
click_b() # x = 3


