import requests
# pip install requests

# 1. 파이썬 사이트 방문

# 2. url 가져오기
url = "https://www.python.org/"
response = requests.get(url)
print(response) #<Response [200]> 정상
print(response.text) # html을 보여줌

# 3. html 다루기 - BeautifulSoup