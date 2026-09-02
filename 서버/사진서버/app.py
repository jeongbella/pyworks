from flask import Flask, render_template
import os #운영체제 관련 모듈

app = Flask(__name__)

@app.route('/')
def index():
    # 웹 페이지 업로드
    return render_template("index.html")

@app.route('/gallery')
def gallery():
    # 디렉터리(폴더) 지정
    photo_list = os.listdir("static/photos")
    return render_template("gallery.html", photos=photo_list)

app.run(debug=True)