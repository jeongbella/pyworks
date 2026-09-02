# 컴퓨터 용어 사전(윈도우 버전)
from tkinter import *

# 딕셔너리 자료 생성
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다. ",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용이 가능하며 입력과 출력을 가질 수 있습니다. ",
    "CPU": "중앙 처리 장치(Central Processing Unit)의 약자로, 컴퓨터의 두뇌에 해당하는 핵심 부품입니다. ",
    "RAM": "임의 접근 메모리(Random Access Memory)의 약자로, 컴퓨터가 작업을 수행하는 동안 데이터를 일시적으로 저장하는 메모리입니다. ",
}

# 검색 함수 정의
def search():
    # strip(): 문자열 공백제거, upper(): 대문자로 변경
    word = entry.get().strip().upper()
    meaning = dic.get(word, "사전에 없는 용어입니다.") #없으면 안내문
    output.delete(1.0, END) #이전결과 지우기(1.0 - 첫째행의 첫번글자)
    output.insert(END, word + ":" + meaning) #검색 결과 출력

# 메인 윈도우 생성
window = Tk()
window.title("컴퓨터 용어 사전")

# 검색어 입력 레이블과 엔트리(입력상자- 한줄)
Label(window, text="용어를 입력하세요:") \
.grid(row=0, column=0, sticky=W, padx=10, pady=5)

entry = Entry(window, width=30)
entry.grid(row=1, column=0, sticky=W, padx=10, pady=5)

# 검색 버튼
Button(window, text="검색", command=search) \
.grid(row=2, column=0, sticky=W, padx=10, pady=5)

# 결과 출력 텍스트(여러줄)
output = Text(window, width=50, height=10)
output.grid(row=3, column=0, sticky=W, padx=10, pady=5)

window.mainloop()