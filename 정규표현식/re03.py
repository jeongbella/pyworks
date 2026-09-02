import re

# findall() - 찾은 문자열을 리스트로 반환
text = "오늘은 2026-09-02입니다. 내일은 2026-09-03입니다."
reg_exp = r"\d{4}-\d{2}-\d{2}"

dates = re.findall(reg_exp, text)
print("날짜 목록:", dates)

'''
for date in dates
print(date)
'''

# sub() - 마스킹 처리
pattern = r"\d{3}-\d{3,4}-\d{4}"
text = "내 전화번호는 010-1234-5678입니다."
masked_text = re.sub(pattern, "xxx-xxxx-xxxx", text)
print(masked_text)

#예제
print(re.sub('\d', '*', 'a1b2c3'))

# 주민등록번호 뒷자리 마스킹 예제
text = "주민등록번호는 900101-1234567입니다."
pattern = r"\b(\d{6})-(\d{7})\"

masked_text = re.sub(pattern, r"\1-*******", text)
print(masked_text)

