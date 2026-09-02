# 서버 프로그램 만들기
from flask import Flask

app = Flask(__name__) # 서버 객체 생성

# http://127.0.0.1:5000/ 내컴퓨터:포트번호
@app.route('/') # 루트 경로
def home():
    return "<h1>Hello~ Flask!</h1>"

# http://127.0.0.1:5000/login
@app.route('/login')
def login():
    return "<h2>로그인 페이지입니다</h2>"

app.run(debug=True) # 서버 실행