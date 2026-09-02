import re #정규표현식 관련 모듈

# match(표현식, 문자열), [] - 일치, 첫번째 문자 일치
m = re.match('[a-z]+', 'korea')
print(m) #<re.Match object; span=(0, 5), match='korea'
print(m.group())   #korea

#  search() - 문자열 "어디든" 반환
#  \d - 숫자(decimal)
s = re.search('\d+', 'abc123de')
print(s.group()) #group은여러개를                                                출력하는 함수