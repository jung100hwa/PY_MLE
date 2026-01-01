# 나라장터 입찰공고정보서비스 [나라장터검색조건에 의한 사전규격]
# 공공데이터 포털에서 먼저 신청하자

import bs4
import requests
from datetime import datetime, timedelta
import PY_PKG.SU_Pandas_MO as sp
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd

print("======================> 데이터추출 시작\n\n")

gdf = pd.DataFrame() # 데이터프레임 전역변수
resultList  = []     # 전체 결과값 리스트
colName     = []     # 컬럼리스트


fname = datetime.now().strftime('%Y-%m-%d') # 저장할 파일명

# 입찰 공고사이트에 대한 키이다.
xmlUrl = 'http://apis.data.go.kr/1230000/HrcspSsstndrdInfoService/getPublicPrcureThngInfoServcPPSSrch'
My_API_Key = unquote('oMstZp2MAQx1Unmt7q6GJP7ZX5tNhNptyCW6sCVA30Jwf9Tg6ChLe2SbHiq4eJhtyKsC839ujDfCBs4IKBwz4g%3D%3D')

# 웹페이지의 탭번호를 의미하는듯. 중요한것도 아니기때문에 그냥 세팅하고 해놓고 하자
tabList = 1

# 자정은 금일이 6일이라고 하면 202212060000로 표시하거나 202212052400으로 표시 함
start_find_d = datetime(2024, 12, 25)                             # 찾기를 원하는 시작일
end_find_d = datetime.now().strftime('%Y%m%d') + '0000'           # 종료일자(금일정보). 즉 시작일부터 금일까지 공공조회

fday = start_find_d                         # 기간검색의 시작일
bday = start_find_d + timedelta(days=1)     # 기간검색의 다음일(시작일 + 1)

# 기간 검색을 위한 것
from_d = fday.strftime('%Y%m%d') + '0000'   # fday에 시간만 붙인것
to_d = bday.strftime('%Y%m%d') + '0000'     # bday에 시간만 붙인것

# 안쪽 while은 돌리기 위한 변수. 참이면 계속, 거짓이면 멈춤.
gTrue = True

while from_d <= end_find_d:
    tabList=1
    gTrue=True

    while gTrue:
        strtabnum = str(tabList)
        queryParams = '?' + urlencode(
            {
                quote_plus('numOfRows'): '20',                 # 한 페이지 결과수
                quote_plus('pageNo'): strtabnum,               # 페이지 번호
                quote_plus('ServiceKey'): My_API_Key,          # 키
                quote_plus('inqryDiv'): '1',                   # 1.접수일시 2.사전규격등록번호 3.참조번호
                quote_plus('inqryBgnDt'): from_d,              # 조회시작일(YYYYMMDDHHMM)
                quote_plus('inqryEndDt'): to_d,                # 조회종료일(YYYYMMDDHHMM)
                quote_plus('swBizObjYn'): 'Y'                  # SW사업대상여부
                }
        )

        # 여기서 데이터를 가져온다.
        response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
        xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

        # 실제데이터 테그는 item, 기간에 해당하는 모든 데이터를 담고 있다.
        allResult = xmlobj.findAll('item')

        # 단지 컬럼명을 구하기 위한 것
        if len(allResult) > 0:
            resultCount = len(allResult)  # 결과개수

            for i in range(0, resultCount):
                itemResult = allResult[i].find_all()
                colCount   = len(itemResult)
                rValueList = []  # 한건에 대한 결과값 리스트. 이것을 resultList에 추가

                for j in range(0, colCount):
                    if len(colName) != colCount:   # 컬럼헤더를 담는다. 첫번째 일때만
                        colName.append(itemResult[j].name)
                    rValue = itemResult[j].text   # 컬럼에 대한 값을 담는다.
                    rValueList.append(rValue)
                resultList.append(rValueList)

            print(fday.strftime('%Y-%m-%d =======>> ' + strtabnum))
            tabList += 1
        else:
            gTrue=False

    # 날짜를 하루씩 업데이트
    fday   = fday + timedelta(days=1)
    bday   = bday + timedelta(days=1)
    
    from_d = fday.strftime('%Y%m%d') + '0000'
    to_d   = bday.strftime('%Y%m%d') + '0000'  

if len(resultList) == 0:
    print("======================> 결과가 존재하지 않음")
else:
    # 컬럼값을 소문자로 일괄 변경해야 편한다. 나중에 오라클에 한방에 넣어서 뭔가 분석할 때
    for index in range(len(colName)):
        colName[index] = str(colName[index]).lower()

    gdf = pd.DataFrame(resultList, columns=colName)  # 결과를 데이터프레임으로 변경

    # 여기에다 필요한 조건을 입력한다.
    # strQ = "(infobizyn == 'Y')" # 정보화 사업여부
    # gresult = gdf.query(strQ)
    # gresult = gresult[~gresult['bidntcenm'].str.contains('유지',regex=True)]   # 유지보수라는 단어가 없는 것
    # gresult['asignbdgtamt'] = gresult['asignbdgtamt'].astype('float')         # 사업금액을 숫자형태로 변환

    strQ = "(asignbdgtamt !='')"
    gresult = gdf.query(strQ)
    gresult['asignbdgtamt'] = gresult['asignbdgtamt'].astype('float')  # 사업금액을 숫자형태로 변환

    columns = {'prdctclsfcnonm': '품명','orderinsttnm': '발주기관명', 'rldminsttnm': '실수요기관명',
               'swbizobjyn': '사업대상여부', 'asignbdgtamt': '배정예산금액'}

    gresult = gresult[columns.keys()]               # 원하는 컬럼만
    gresult.rename(columns=columns, inplace=True)

    # 중복값을 제거하자, 조달청 api가 조금 명확하지 않음
    gresult = gresult.drop_duplicates()
    sp.SU_MO_To_excel(gresult, "C:\\work\\"+fname+"_사전용역역공고현황.xlsx")

    print("======================> 완료")
