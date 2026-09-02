#조건문 - if ~ else

age = 14

#콜론 다음줄에 4칸 들여쓰기(indent)
if age >= 15: #조건식 결과값이 true일때 실행
    print("입장 가능합니다.") #age=16일때
else: #age<15
    print("입장할 수 없습니다.") #age=14일때

    
    
# 다중 조건문 - if ~ elif ~ else
# 횡단보도 신호등  구현
signal = input("색상을 입력하세요(빨강, 파랑, 노랑):")

if signal == "빨강": #같다 == 2개
    print("멈추세요")
elif signal == "노랑":
    print("주의하세요")
elif signal == "파랑":
    print("건너가세요")
else:
    print("신호등 색상이 아닙니다.")
    

