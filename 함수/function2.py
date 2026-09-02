# 매개변수 - 변수
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-10)) #10

# 매개변수 - 리스트
def func(a):
    a2 = []
    for i in a:
        a2.append(i * 4)
    return a2

arr = [1, 2, 3, 4] 
print(func(arr)) #[4, 8, 12, 16]

# 기본 매개변수는 변수가 여러 개일때 뒤쪽에 만든다.
# 함수를 호출할때 기본 매개변수는 생략 가능하다.
def take_bus(passenger, fare=1500):
    print(f"승객수는 {passenger}명, 버스 요금은 {fare}원")

take_bus(5) #일반버스
take_bus(6, 1900) #프리미엄 버스

