from datetime import date, timedelta

year, month, day = map(int, input().split(' '))
d = date(year, month, day)
delta = timedelta(int(input()))
result = d + delta
print(result.year, result.month, result.day)
