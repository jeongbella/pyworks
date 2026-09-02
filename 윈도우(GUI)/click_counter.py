from tkinter import *

count = 0   #전역 변수
def add():
    global count  #지역변수가 전역변수화 함
    count += 1
    label.config(text=f"클릭 횟수: {count}")

root = Tk()
root.title("1증가하기")
root.geometry("250x100")

label = Label(root, text="클릭 횟수: 0", font=("맑은 고딕", 14))
label.pack(pady=10)
Button(root, text="누르기", command=add).pack(pady=5)
root.mainloop()