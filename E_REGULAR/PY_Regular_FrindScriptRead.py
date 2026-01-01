# 파일관련은 부분실행이 잘 안됨

import os, re

######################################################### 특정인 대사 모으기(Monica), 파일로 저장
if os.path.isfile('monicatext.txt'):
    os.remove('monicatext.txt')

monicatext = open('monicatext.txt', 'a', encoding='utf-8')
f = open('friends101.txt','r', encoding='utf-8')
fs = f.read()
com = re.compile(r'Monica:.+') # 모니카 대화만
ml = com.findall(fs)

for item in ml:
    monicatext.write(item +'\n')
monicatext.close()
f.close()

######################################################### 사람의 대사부분만 모으기
if os.path.isfile('peoplelist.txt'):
    os.remove('peoplelist.txt')
peoplelist = open('peoplelist.txt', 'a', encoding='utf-8')

f = open('friends101.txt', 'r', encoding='utf-8')
fs = f.read()
com = re.compile(r'[A-Z][a-z]+:')
ml = com.findall(fs)

# todo 중복을 제거하기 위해 set으로 변경
# set은 중복을 허용하지 않고 순서가 없다
ml = set(ml)

for item in ml:
    item = str(item).replace(':','')
    peoplelist.write(item + '\n')
peoplelist.close()
f.close()


######################################################### 지문만 출력하기(지문 행동 지시)
if os.path.isfile('nonconversation.txt'):
    os.remove('nonconversation.txt')
comv = open('nonconversation.txt', 'a', encoding='utf-8')

f = open('friends101.txt', 'r', encoding='utf-8')
fs = f.read()
# com = re.compile(r'\([A-Za-z].+[a-z|\. ]\)') # \ 이것은 뒤의 (를 문자로 인식하라
com = re.compile(r'\([A-Za-z].+\)') # \ 이것은 뒤의 (를 문자로 인식하라
ml = com.findall(fs)

for item in ml:
    comv.write(item + '\n')
comv.close()
f.close()

######################################################### 특정 단어가 들어간 대사만 추출('would'가 들어간 문장 찾기)
if os.path.isfile('conversation.txt'):
    os.remove('conversation.txt')
comv = open('conversation.txt', 'a', encoding='utf-8')

f = open('friends101.txt', 'r', encoding='utf-8')
fs = f.readlines() # 이렇게 하면 줄단위로 리스트. 즉 줄마다 \n을 추가
com = re.compile(r'[A-Z][a-z]+:')

#match, search의 결과값은 group() 함수로 출력
for item in fs:
    if com.match(item) and re.search('would',item):
        comv.writelines(item)
comv.close()
f.close()