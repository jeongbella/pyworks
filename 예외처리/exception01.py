
try:
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(20 + '20')
except TypeError as e:
    print("자료형 오류가 발생했습니다.", e)

try:
    # ZeroDivisionError: division by zero
    n1 = 10 
    n2 = 0
    print(n1/n2)
except ZeroDivisionError as e:
    print(e)

# 다중 예외 처리
try:
    num = int(input("숫자 입력: "))
    print(10 / num)
except ValueError:
    print("숫자만 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
