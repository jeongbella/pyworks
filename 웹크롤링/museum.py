import requests
from bs4 import BeautifulSoup

# 1. 국립중앙박물관 > 관람정보 > 관람안내
# 2. url 가져오기
url = "https://www.museum.go.kr/MUSEUM/contents/M0101000000.do?menuId=tour-guidance"
response = requests.get(url)
print(response) #<Response [200] > 성공
# print(response.text)

#  3. BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# 4. 관람시간 정보 추출 - select_one() 함수
first_ul = soup.select_one('ul.display-content')
print(first_ul)
#  print(first_ul.text)
print(first_ul.get_text()) #함수사용한것 위에것중 선택해 사용

# 5. 관람 정보 전체 항목 추출하기
contests = soup.select('ul.display-content-area > li > ul')
print(contests)
print(contests[1].get_text()) #휴관일