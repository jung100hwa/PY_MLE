# 나라장터의 낙찰자정보서비스중 [나라장터 검색조건에 의한 낙찰된 목록 현황 용역조회]
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
import xml.etree.ElementTree as ET
from SU_MO import SU_Init
from SU_MO import SU_Pandas_MO
from SU_MO import SU_Excel_MO
from datetime import datetime, timedelta

SU_Init.SU_MO_VarInit()

################################################################################# 1. 나라장터 낙찰정보서비스 (ScsbidInfoService)
# 시작은 2021.01.01부터 해서 1주간격으로 1000건씩 오늘날짜까지 구하기
# 검색조건을 구할 때에는 항상 데이터베이스를 보고 이 다음부터 자료를 모은다.
startday = datetime(2021, 1, 1)
strendday   = datetime.now().strftime('%Y%m%d') + '0000'

beforeday = startday
afterday  = startday + timedelta(days=1)

# 기간 검색을 위한 것
strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
strafterday  = afterday.strftime('%Y%m%d')  + '0000'

xmlUrl = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getScsbidListSttusServcPPSSrch'
# xmlUrl = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfoServcPPSSrch' # 낙착율이 정확히 나오지 않음

My_API_Key = unquote('E1j62il6jQPHJEDMntSkDvz5bhOQZYjv%2Bx8s%2F8m84uwkxeZy6CJk%2Bsv5rK4FJu2aZt7l98VLSybWfoJzElQnjg%3D%3D')

# 변수 선언 및 초기화
checkindex = 0
TDF = pd.DataFrame(columns=['A','B'])

while strbeforeday <= strendday:
    queryParams = '?' + urlencode(
        {
            quote_plus('numOfRows') : '900',
            quote_plus('pageNo') : '1',
            quote_plus('ServiceKey') : My_API_Key,
            # quote_plus('type') : 'json',                  # json으로 받고 싶을 때. json 기입
            quote_plus('inqryDiv'): '1',                    # 1.공고일시, 2.개찰일시, 4.입찰공고번호
            quote_plus('inqryBgnDt'): strbeforeday,         # 조회시작일(YYYYMMDDHHMM)
            quote_plus('inqryEndDt'): strafterday           # 조회종료일(YYYYMMDDHHMM)
            # quote_plus('bidNtceNo') : '0000000000',       # 입찰공고번호
            # quote_plus('bidNtceNm') : '0000000000',       # 입찰공고명
            # quote_plus('ntceInsttCd') : '0000000000',     # 공고기관코드(7자리)
            # quote_plus('ntceInsttNm') : '0000000000',     # 공고기관명(보통은 조달청)
            # quote_plus('dminsttCd') : '0000000000',       # 수요기관코드(7자리)
            # quote_plus('dminsttNm') : '0000000000',       # 수요기관명(보통은 조달청)
            # quote_plus('refNo') : '0000000000',           # 참조번호(뭔지 잘 모르겠음)
            # quote_plus('prtcptLmtRgnCd') : '0000000000',  # 참가제한지역코드
            # quote_plus('prtcptLmtRgnNm') : '0000000000',  # 참가제한지역명
            # quote_plus('indstrytyCd') : '0000000000',     # 업종코드
            # quote_plus('indstrytyNm') : '0000000000',     # 업종명
            # quote_plus('presmptPrceBgn') : '0000000000',  # 추정가격시작(이해안됨)
            # quote_plus('presmptPrceEnd') : '0000000000',  # 추정가격종료(이해안됨)
            # quote_plus('dtilPrdctClsfcNo') : '0000000000',# 검색하고자하는 세부품명번호
            # quote_plus('masYn') : '0000000000',           # 검색하고자하는 다수공급경쟁자여부
            # quote_plus('prcrmntReqNo') : '0000000000',    # 검색하고자하는 조달요청번호
            # quote_plus('intrntnlDivCd') : '0000000000',   # 검색하고자하는 국제구분코드 국내:1, 국제:2
         }
    )

    response=requests.get(xmlUrl + queryParams).text.encode('utf-8')
    xmlobj=bs4.BeautifulSoup(response, 'lxml-xml')

    # 실제데이터는 테그는 item
    rows=xmlobj.findAll('item')

    # 단지 컬럼명을 구하기 위한 것
    if len(rows) > 0:
        columns=rows[0].find_all()

        rowList=[]
        nameList=[]
        columnList=[]
        rowsLen=len(rows)

        for i in range(0, rowsLen):
            columns=rows[i].find_all()
            columnsLen=len(columns)
            for j in range(0, columnsLen):
                if i == 0:  # 컬럼헤더를 담는다. 첫번째 일때만
                    nameList.append(columns[j].name)
                eachColumn=columns[j].text
                columnList.append(eachColumn)
            rowList.append(columnList)
            columnList=[]

        # 컬럼값을 소문자로 일괄 변경해야 오라클에 한방에 들어간다.
        i=0
        for item in nameList:
            nameList[i]=str(item).lower()
            i=i + 1

        result=pd.DataFrame(rowList, columns=nameList)

        print(strbeforeday + "=======> 불러오기 성공 " + str(len(rowList)))

        if checkindex == 0:
            TDF=result.copy()
        else:
            TDF=pd.concat([TDF, result], axis=0, ignore_index=True)

        # 아래의 방법으로 하자. 그리고 중요한 것은 무조건 컬럼이든 테이블명이든 소문자로 해야 한다. 아니면 경고 등 잘 안된다.
        print("=" * 50 + str(len(rowList)) + "=======> 데이터베이스 저장 중")
        SU_Pandas_MO.SU_MO_To_Sql(result, "gb01", SU_Init.G_SU_Engine, 2, SU_Init.G_SU_Connection)

    beforeday=beforeday + timedelta(days=1)
    afterday=afterday + timedelta(days=1)
    strbeforeday=beforeday.strftime('%Y%m%d') + '0001'
    strafterday=afterday.strftime('%Y%m%d') + '0000'
    checkindex = checkindex + 1

print("=" * 50 + " 엑셀로 내보내기 중")
SU_Pandas_MO.SU_MO_To_excel(TDF, SU_Init.G_SU_ExFilePosOut + "G4b_01.xlsx")

print("=" * 50 + " 데이터베이스 구축 완료")