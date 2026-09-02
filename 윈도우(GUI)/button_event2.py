from tkinter import *

def click():
    name = entry.get()  #입력된 문자열을 가져옴
    # result.config(text="안녕하세요, " + name + "님!")
    result.config(text=f"안녕하세요, {name}님!")

root = Tk()
root.title("인사하기 프로그램")
root.geometry("240x150")

# 입력 상자(한 줄)
entry = Entry(root)
entry.pack(pady=10)
# 버튼
Button(root, text="인사하기", command=click).pack()
# 라벨
result = Label(root, text="")
result.pack(pady=10)

root.mainloop()