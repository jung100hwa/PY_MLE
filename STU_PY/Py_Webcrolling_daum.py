# 인코딩 방식이 틀려서 오류가 많이 남
# 이럴때에는 아래와 같이 습관적으로 utf-8로 만들어 놓고 시작
# 아래와 같이 하면 ", 숫자 등이 깨짐
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as ur         # 웹사이트를 불러오고
from bs4 import BeautifulSoup as bs # 불러온 웹사이트데이터를 가공

news = 'https://news.daum.net'
soup = bs(ur.urlopen(news), 'html.parser')

# quote = soup.find_all('div',{"class" : "item_issue"})
quote = soup.find_all('div',{"class" : "box_peruse"})

# 해당 영역 안에서 다시 조건에 맞는 것만 출력
# 즉 find_all로 찾은 것은 하나의 리스트로 이것이 또하나의 영역이 되고
# 이 영역에서 다시 find_all로 이런식으로 찾는다. 중요한 것은 크롤링 대상 사이트를 분석하는 것이 필요
for item in quote:
    item = item.find_all('a')
    for subitem in item:
        title = subitem.text
        title = title.replace(' ','')
        title = title.replace('\n','')
        if title:
            link = subitem.get('href')
            print('타이틀 : %s' %title)
            print('링크사이트 : %s\n' %link)
