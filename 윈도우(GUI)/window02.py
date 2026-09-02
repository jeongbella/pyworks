
from tkinter import *

# 로그인 폼
root = Tk()
root.title("로그인")

# 라벨(Label)
Label(root, text="아이디").grid(row=0, column=0, padx=5, pady=10)
# 입력상자(Entry)
Entry(root).grid(row=0, column=1, padx=10)
# 라벨(Label)
Label(root, text="비밀번호").grid(row=1, column=0, padx=5, pady=5)
# 입력상자(Entry)
Entry(root, show="*").grid(row=1, column=1, padx=10)
Button(root, text="로그인").grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()