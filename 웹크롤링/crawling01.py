# pip install BeautifulSoup4
from bs4 import BeautifulSoup
import requests

# 1. 서울시청 사이트 > 메뉴 글자 수집

# 2. url 가져오기
url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)
# print(response.text)

# 3. BeautifulSoup으로 html 다루기
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) # title 태그 가져옴
print(soup.title.text) #동행·매력 특별시 서울 | 서울특별시

# 4. 메뉴 글자 수집 - select()-여러개, select_one() - 1개
all_li = soup.select('div.m_service ul li')
# print(all_li) #리스트
# print(all_li[0])

# 5. 전체 목록
for li in all_li:
    print(li.text.strip())