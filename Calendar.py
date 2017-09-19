import calendar

from datetime import date
inp = map(int, raw_input().split())
x = date(inp[2],inp[0],inp[1]).weekday()
print calendar.day_name[x].upper()