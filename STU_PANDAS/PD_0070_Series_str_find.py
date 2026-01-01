import pandas as pd

s = pd.Series(['Lionon baby', 'Monkey', 'Rabbit'])
print(s)

# 찾은 인덱스의 가장 낮은 값, 없으면 -1
print(s.str.find(sub='on'))

# 찾은 인덱스 중 가장 높은 값, 하나의 문자열에 2개의 해당 문자열이 존재할 때
print(s.str.rfind(sub='on'))

# findall()은 정규식을 지원한다, 그리고 일치하는 모든 문자열을 리스트 형태로 리턴한다.
print(s.str.findall('Monkey'))

print(s.str.findall('on'))
##########################################
res = s.str.findall('on')
i = 0
for item in res:
    li = list(item)
    if len(li) > 0 :
        print(s[i])
    else:
        print("no")
    i = i +1
##########################################

# 정규식을 지원한다. y 또는 n으로 끝나는 것
print(s.str.findall(r'[yn]$'))


# Lionon으로 시작하고 baby로 끝나는 문자열
print(s.str.findall('^Lionon baby$'))

########################################## test
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}


df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

print(df['수학'].astype(str).str.findall('^9'))


# R로 시작하고 it로 끝나며 중간에 영문자가 하나이상인 것
print(s)
print(s.str.findall('^R\w+it$'))



s = pd.Series(["'javascript:goDetail('20120943015','B001');'", "'javascript:goDetail('20120943016','B002');'"])
s1 = s.str.findall('[0-9]+')[0][0]
s2 = f"B{s.str.findall('[0-9]+')[0][1]}"

s3 = s.str.findall('[0-9]+')
print(s3)