from decimal import Decimal

# 정확한 계산을 위해서 필요

# 이진수 기반의 파이썬은 아래와 같은 문제가 발생
if (0.1 * 3) == 0.3:
    print('ok')
else:
    print(0.1 * 3)

if (1.2 - 0.1) == 1.1:
    print('ok')
else:
    print(1.2 - 0.1)

print('=' * 50)

# Decimal 연산은 생성자 함수의 인자로 문자열을 넘겨야 한다.!!!
if (Decimal('0.1') * 3) == Decimal('0.3'):
    print('ok')

print(Decimal('0.1') * 3)

print(Decimal('2.2') - Decimal('0.1'))

# Decimal은 속도가 느리다. 대신 정확한 돈계산시 유용하다
# 그리고 정수연산을 가능하나 실수 연산은 불가능 하다. Decimal('반드시 문자 형태')
# Decimal('0.1') * 0.3 이런 실수 연산은 불가능. 오류 => 소수점 연산은 무조건 Decimal으로 계산한다고 생각하면됨