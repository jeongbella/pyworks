# 타자 연습 게임 (tkinter GUI 버전)
import os
import random
import time
import tkinter as tk
from tkinter import messagebox

# word.txt 파일 경로 찾기 (스크립트 위치 기준, 없으면 상위 폴더의 output도 확인)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = [
    os.path.join(BASE_DIR, "output", "word.txt"),
    os.path.join(BASE_DIR, "..", "output", "word.txt"),
]

words = []
for path in CANDIDATES:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        break

if not words:
    words = ["python", "programming", "challenge", "developer", "algorithm"]

TOTAL_QUESTIONS = 10


class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("타자 연습 게임")
        self.root.geometry("420x260")
        self.root.resizable(False, False)

        self.n = 1  # 문제 번호
        self.start_time = None
        self.current_word = ""

        self.info_label = tk.Label(root, text=f"[타자 게임] 준비되면 시작 버튼을 누르세요! (총 {TOTAL_QUESTIONS}문제)",
                                    font=("맑은 고딕", 11))
        self.info_label.pack(pady=10)

        self.progress_label = tk.Label(root, text="", font=("맑은 고딕", 10))
        self.progress_label.pack()

        self.word_label = tk.Label(root, text="", font=("맑은 고딕", 20, "bold"), fg="blue")
        self.word_label.pack(pady=15)

        self.entry = tk.Entry(root, font=("맑은 고딕", 14), justify="center")
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_answer)

        self.start_button = tk.Button(root, text="시작", font=("맑은 고딕", 11), command=self.start_game)
        self.start_button.pack(pady=2)

        self.result_label = tk.Label(root, text="", font=("맑은 고딕", 11))
        self.result_label.pack(pady=5)

        self.entry.config(state="disabled")

    def start_game(self):
        self.n = 1
        self.start_time = time.time()
        self.start_button.config(state="disabled")
        self.entry.config(state="normal")
        self.result_label.config(text="")
        self.next_question()
        self.entry.focus_set()

    def next_question(self):
        if self.n > TOTAL_QUESTIONS:
            self.finish_game()
            return
        self.progress_label.config(text=f"문제: {self.n} / {TOTAL_QUESTIONS}")
        self.current_word = random.choice(words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)

    def check_answer(self, event=None):
        if self.start_time is None:
            return
        you = self.entry.get()
        if you == self.current_word:
            self.result_label.config(text="정답!", fg="green")
            self.n += 1
            self.next_question()
        else:
            self.result_label.config(text="오답! 다시 도전!", fg="red")
            self.entry.delete(0, tk.END)

    def finish_game(self):
        elapsed = time.time() - self.start_time
        self.word_label.config(text="완료!")
        self.progress_label.config(text="")
        self.entry.config(state="disabled")
        self.result_label.config(text=f"게임에 걸린 시간: {elapsed:.2f}초", fg="blue")
        self.start_button.config(state="normal", text="다시 시작")
        messagebox.showinfo("게임 종료", f"모든 문제를 완료했습니다!\n걸린 시간: {elapsed:.2f}초")


if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
