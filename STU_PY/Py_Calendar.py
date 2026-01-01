import calendar as ca

#  23년 전체를 표시
print(ca.calendar(2023))

# 무슨 요일인지
re = ca.weekday(2023, 5, 14)

if re == 0:
    print('MO')
elif re == 1:
    print('TU')
elif re == 2:
    print('WE')
elif re == 3:
    print('TH')
elif re == 4:
    print('FR')
elif re == 5:
    print('SA')
else:
    print('SU')


# 해당월이 1일은 무슨요일이고 며칠까지 있는지
print(ca.monthrange(2023,5))

# 샘플을 한번 작성해 보자

def weeksam(re):
    if re == 0:
        return 'MO'
    elif re == 1:
        return 'TU'
    elif re == 2:
        return 'WE'
    elif re == 3:
        return 'TH'
    elif re == 4:
        return 'FR'
    elif re == 5:
        return 'SA'
    else:
        return 'SU'
for mon in range(1,13):
    tu = ca.monthrange(2023,mon)
    print("2023,{}={},{}까지".format(mon,weeksam(tu[0]),tu[1]))
