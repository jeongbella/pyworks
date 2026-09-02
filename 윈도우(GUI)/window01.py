# tkinter 라이브러리(모듈이나 패키지)를 가져오기
from tkinter import *  # *은 모든 함수나 클래스를 의미함

# 객체 생성 - 창(윈도우) 만들기
root = Tk()
root.title("첫 윈도우 만들기")
root.geometry("300x100") # 창 크기(너비, 높이)

# 컴포넌트 배치 - pack(), 가운데 정렬
# 라벨(글자 출력) - Label 클래스 사용
Label(root, text="안녕하세요!").pack(pady=10)
Button(root, text="확인").pack()

root.mainloop()  # 창을 항상 유지