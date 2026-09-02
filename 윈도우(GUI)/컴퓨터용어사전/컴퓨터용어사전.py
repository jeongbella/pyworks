# 컴퓨터 용어 사전(윈도우 GUI 버전)
# tkinter는 파이썬에서 창, 버튼, 입력 상자 등을 만들 때 사용하는 모듈입니다.
from tkinter import *


# 용어와 뜻을 한 쌍으로 저장하는 딕셔너리입니다.
dictionary = {
    "변수": "데이터를 저장하기 위한 이름이 있는 공간입니다.",
    "함수": "특정 작업을 수행하도록 묶어 둔 코드입니다.",
    "CPU": "컴퓨터의 계산과 제어를 담당하는 중앙 처리 장치입니다.",
    "RAM": "실행 중인 프로그램의 데이터를 잠시 저장하는 메모리입니다.",
}


def show_message(message):
    """결과 출력 상자에 안내 문구를 보여 줍니다."""
    output.delete("1.0", END)  # 기존에 출력된 내용을 모두 지웁니다.
    output.insert(END, message)  # 새 메시지를 출력 상자 끝에 넣습니다.


def search_word():
    """입력한 용어를 사전에서 찾아 뜻을 보여 줍니다."""
    # get()으로 입력 상자의 글자를 가져오고, strip()으로 앞뒤 공백을 지웁니다.
    word = search_entry.get().strip().upper()

    if not word:
        show_message("검색할 용어를 입력하세요.")
        return  # 아래 코드를 실행하지 않고 함수를 끝냅니다.

    # get(용어)는 용어의 뜻을 가져오며, 없으면 두 번째 값을 사용합니다.
    meaning = dictionary.get(word, "사전에 없는 용어입니다.")
    show_message(f"{word}\n\n{meaning}")


def add_word():
    """새로 입력한 용어와 뜻을 딕셔너리에 추가합니다."""
    word = new_word_entry.get().strip().upper()
    meaning = meaning_entry.get().strip()

    # 용어와 뜻 모두 입력했는지 먼저 확인합니다.
    if not word or not meaning:
        show_message("새 용어와 뜻을 모두 입력하세요.")
        return

    # 딕셔너리에 같은 용어가 있으면 뜻이 새 내용으로 바뀝니다.
    dictionary[word] = meaning

    # 추가가 끝난 뒤 입력 상자를 비워 다음 용어를 쉽게 입력할 수 있게 합니다.
    new_word_entry.delete(0, END)
    meaning_entry.delete(0, END)
    search_entry.delete(0, END)
    search_entry.insert(0, word)  # 방금 추가한 용어를 검색 상자에 표시합니다.
    search_word()  # 방금 저장한 용어를 딕셔너리에서 바로 검색해 보여 줍니다.


# 프로그램의 기본 창을 만듭니다.
window = Tk()
window.title("컴퓨터 용어 사전")
window.geometry("480x390")

# 검색 영역
Label(window, text="용어 검색", font=("맑은 고딕", 12, "bold")).grid(
    row=0, column=0, columnspan=2, sticky=W, padx=10, pady=(10, 5)
)
Label(window, text="검색할 용어:").grid(row=1, column=0, sticky=W, padx=10, pady=5)
search_entry = Entry(window, width=38)
search_entry.grid(row=1, column=1, sticky=W, padx=10, pady=5)
Button(window, text="검색", command=search_word).grid(row=2, column=1, sticky=E, padx=10, pady=5)

# 새 용어 추가 영역
Label(window, text="새 용어 추가", font=("맑은 고딕", 12, "bold")).grid(
    row=3, column=0, columnspan=2, sticky=W, padx=10, pady=(15, 5)
)
Label(window, text="새 용어:").grid(row=4, column=0, sticky=W, padx=10, pady=5)
new_word_entry = Entry(window, width=38)
new_word_entry.grid(row=4, column=1, sticky=W, padx=10, pady=5)
Label(window, text="뜻:").grid(row=5, column=0, sticky=W, padx=10, pady=5)
meaning_entry = Entry(window, width=38)
meaning_entry.grid(row=5, column=1, sticky=W, padx=10, pady=5)
Button(window, text="용어 추가", command=add_word).grid(row=6, column=1, sticky=E, padx=10, pady=5)

# 검색 결과와 추가 안내를 여러 줄로 보여 주는 상자입니다.
output = Text(window, width=54, height=8)
output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# 창이 닫힐 때까지 이벤트를 처리합니다.
window.mainloop()