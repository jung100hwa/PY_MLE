from datetime import date
from datetime import datetime, timedelta
from enum import IntEnum

# 파이썬 3.4부터 지원함. Enum, IntEnum 등 상위클래스로부터 상속받아서 수행
# 단지 쓰는 이유가 관계된 것을 모아놓고 가독성을 높이기 위함

# IntEnum 클래스로부터 상속
class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_menu(input_date):
    weekday = input_date.isoweekday()
    if weekday == Week.MONDAY:
        menu = "김치찌개"
    elif weekday == Week.TUESDAY:
        menu = "비빔밥"
    elif weekday == Week.WEDNESDAY:
        menu = "된장찌개"
    elif weekday == Week.THURSDAY:
        menu = "불고기"
    elif weekday == Week.FRIDAY:
        menu = "갈비탕"
    elif weekday == Week.SATURDAY:
        menu = "라면"
    elif weekday == Week.SUNDAY:
        menu = "건빵"
    return menu


print(get_menu(date(2020, 12, 6)))
print(get_menu(date(2023, 8, 26)))