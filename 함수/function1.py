# 함수 예제
def message():
    return "Good Luck!"

msg = message()
print(message())

# 응원메시지
msg = message() # 반환값이 있을때는 한번 넣어주기
print(msg)

# 사각형의 면적 계산 함수
def area(w, h):
    return w*h

# 사각형의 면적 : 가로(w) x 세로(h)
area = area (4, 3)
print("사각형의 면적:",area) # 사각형의 면적: 12

# 삼각형의 면적
def triangle(w,h):
    return w*h/2
tri_area=triangle(3,4)
print("삼각형의 면적:", tri_area) # 삼각형의 면적: 6.0, 나누기가 들어가면 실수로 나옴(6.0). 정수로 안나옴(6 x)


def triangle():
    pass #중간에 정지할때, 에러안남

# 구구단 함수 호출
def gugudan(dan):
    for i in range(1,10):
        print(f"{dan} x {i} = {dan*i}")

gugudan(5)
