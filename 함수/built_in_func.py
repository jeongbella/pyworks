# 내장 함수 - 파이썬에서 제공되는 함수
a = [1, 3, 5, 1] # 리스트는 중복 가능

print(sum(a)) # 10

print(len(a)) # 4

print(min(a)) # 1

# 반올림 = round()
b = 32.567
print(round(b)) #33
print(round(b, 1)) #32.6
print(round(b, 2)) #32.57
print(round(b, -1)) #30.0 1의자리에서 반올림
print(round(b, -2)) # 0.0

c = 352.567
print(round(c)) #353
print(round(c, 1)) #352.6
print(round(c, 2)) #352.57 (소수 둘째)
print(round(c, -1)) #350 (일의자리 반올림)
print(round(c, -2)) # 400 (십의자리 반올림)

# 절대값 - abs(x) absolute
print(abs(8)) # 8
print(abs(-8)) # 8

# 직접 만든 절대값 함수
def my_abs(x):
    if x < 0:
        return -x
    else :
        return x
        
print(my_abs(-7)) # 7

