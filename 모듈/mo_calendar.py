# 칼렌더(calendar) 모듈 사용

import calendar

# 2026년 전체달력

#calendar.prcal(2026)

calendar.prmonth(2026, 8)

# 요일 이름 출력
print(calendar.day_name[0]) #Monday
print(calendar.day_name[6]) #Sunday
print(calendar.day_name[:]) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_of_week = calendar.weekday(2026,8,10)
print(day_of_week) # 0 / day_of_week 0~6까지 출력
print(calendar.day_name[day_of_week]) #Monday

day_of_week = calendar.weekday(2026,12,25)
print(day_of_week) # 4
print(calendar.day_name[day_of_week]) #Friday

print(calendar.weekday(2026,12,25))
print(calendar.day_name[calendar.weekday(2026,12,25)]) #Friday