import re

# 휴대폰 번호 검사
# match() - 첫글자가 일지하는지 확인
# pullmatch() - 전체가 일치하는지 확인
phone = "010-12-5678"
if re.fullmatch(r'010-\d{3,4}-\d{4}', phone):
    print("올바른 휴대폰 번호입니다.")
else: 
    print("잘못된 휴대폰 번호입니다.")


# 이메일
# @의 전후 표현식 확인, .은 '\.'으로 표기
email = "hong_12.#K@gmail.com"
re_exp = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}"
if re.fullmatch(re_exp, email):
    print("올바른 이메일 형식입니다.")
else:
    print("잘못된 이메일 형식입니다.")
