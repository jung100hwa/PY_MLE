# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행 (시리즈 vs. 시리즈). 인덱스가 같은 것끼지 계산
# 만약에 한쪽에만 있으면 계산되지 않는다. 어느 프로그램이든지 Null 계산은 항상 Null
addition = student1 + student2               #덧셈
subtraction = student1 - student2            #뺄셈
multiplication = student1 * student2         #곱셈
division = student1 / student2               #나눗셈
print(addition)
print('\n')


# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
print('\n')


# 사칙연산 메소드를 활용하면 NaN를 특정값으로 바꾸어서 계산이 가능하다.
# fill_value옵션은 두항 모두 존재하는 NaN를 0으로 바꾼다.
sr_add = student1.add(student2, fill_value=0)    #덧셈
print(sr_add)
sr_sub = student1.sub(student2, fill_value=0)    #뺄셈
sr_mul = student1.mul(student2, fill_value=0)    #곱셈
sr_div = student1.div(student2, fill_value=0)    #나눗셈
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
print('\n')