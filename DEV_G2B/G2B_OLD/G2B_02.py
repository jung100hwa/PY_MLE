# 나라장터 입찰공고정보서비스 [나라장터검색조건에 의한 입찰공고용역조회]
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

################################################################################# 2. 나라장터 입찰공고정보서비스 (BidPublicInfoService02)
# 시작은 2021.01.01부터 해서 1주간격으로 1000건씩 오늘날짜까지 구하기
# 검색조건을 구할 때에는 항상 데이터베이스를 보고 이 다음부터 자료를 모은다.
startday = datetime(2021, 10, 1)
strendday   = datetime.now().strftime('%Y%m%d') + '0000'

beforeday = startday
afterday  = startday + timedelta(days=1)

# 기간 검색을 위한 것
strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
strafterday  = afterday.strftime('%Y%m%d')  + '0000'

xmlUrl = 'http://apis.data.go.kr/1230000/BidPublicInfoService02/getBidPblancListInfoServcPPSSrch'
My_API_Key = unquote('E1j62il6jQPHJEDMntSkDvz5bhOQZYjv%2Bx8s%2F8m84uwkxeZy6CJk%2Bsv5rK4FJu2aZt7l98VLSybWfoJzElQnjg%3D%3D')

# 변수 선언 및 초기화
checkindex = 0
TDF = pd.DataFrame(columns=['A','B'])

# 나머지 검색조건은 필요가 없는 듯 함
while strbeforeday <= strendday:
    queryParams = '?' + urlencode(
        {
            quote_plus('numOfRows') : '900',
            quote_plus('pageNo') : '1',
            quote_plus('ServiceKey') : My_API_Key,
            # quote_plus('type') : 'json',                  # json으로 받고 싶을 때. json 기입
            quote_plus('inqryDiv'): '1',                    # 1.공고일시, 2.개찰일시
            quote_plus('inqryBgnDt'): strbeforeday,         # 조회시작일(YYYYMMDDHHMM)
            quote_plus('inqryEndDt'): strafterday           # 조회종료일(YYYYMMDDHHMM)
            # quote_plus('bidNtceNm') : '0000000000',       # 입찰공고명
            # quote_plus('ntceInsttCd') : '0000000000',     # 공고기관코드
            # quote_plus('ntceInsttNm') : '0000000000',     # 공고기관명
            # quote_plus('dminsttCd') : '0000000000',       # 수요기관코드
            # quote_plus('dminsttNm') : '0000000000',       # 수요기관명
            # quote_plus('refNo') : '0000000000',           # 참조번호
            # quote_plus('prtcptLmtRgnCd') : '0000000000',  # 참가제한지역코드
            # quote_plus('prtcptLmtRgnNm') : '0000000000',  # 참가제한지역명
            # quote_plus('indstrytyCd') : '0000000000',     # 업종코드
            # quote_plus('indstrytyNm') : '0000000000',     # 업종명
            # quote_plus('presmptPrceBgn') : '0000000000',  # 추정가격시작
            # quote_plus('presmptPrceEnd') : '0000000000',  # 추정가격종료
            # quote_plus('dtilPrdctClsfcNo') : '0000000000',# 세부품명번호
            # quote_plus('prcrmntReqNo') : '0000000000',    # 조달요청번호
            # quote_plus('bidClseExcpYn') : '0000000000',   # 입찰마감제외여부
            # quote_plus('intrntnlDivCd') : '0000000000',   # 국제구분코드
            # quote_plus('masYn') : '0000000000',           # 다수공급경쟁자여부
         }
    )

    response=requests.get(xmlUrl + queryParams).text.encode('utf-8')
    xmlobj=bs4.BeautifulSoup(response, 'lxml-xml')

    # 실제데이터 테그는 item
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

        # 조건에 맞는 건수를 가져온다. 즉 하루치의 모든 정보를 불러온다.
        result=pd.DataFrame(rowList, columns=nameList)

        print(strbeforeday + "=======> 불러오기 성공 " + str(len(rowList)))

        if checkindex == 0:
            TDF=result.copy()
        else:
            # axis = 0 로우에 계속 추가. 1이면 컬럼으로 추가
            TDF=pd.concat([TDF, result], axis=0, ignore_index=True)

        checkindex=checkindex + 1

        # 아래의 방법으로 하자. 그리고 중요한 것은 무조건 컬럼이든 테이블명이든 소문자로 해야 한다. 아니면 경고 등 잘 안된다.
        # 데이터가 많아서 그런지 하세월이네 아래에서 직접 넣기로 함. 여기서는 하지 않음
        # print("=" * 50 + str(len(rowList)) + "=======> 데이터베이스 저장 중")
        # SU_Pandas_MO.SU_MO_To_Sql(result, "gb02", SU_Init.G_SU_Engine, 2, SU_Init.G_SU_Connection)

        # 정보화 사업만 불러오기
        strQ = "infobizyn == 'Y'"
        result = result.query(strQ)

        # 속도가 늦어 분활해서 DB넣기
        SU_Pandas_MO.SU_MO_DfOracleInsert(result, SU_Init.G_SU_Connection, 'GB02', 1)

    beforeday=beforeday + timedelta(days=1)
    afterday=afterday + timedelta(days=1)
    strbeforeday=beforeday.strftime('%Y%m%d') + '0001'
    strafterday=afterday.strftime('%Y%m%d') + '0000'

# print("=" * 50 + " 엑셀로 내보내기 중")
# SU_Pandas_MO.SU_MO_To_excel(TDF, SU_Init.G_SU_ExFilePosOut + "G4b_02.xlsx")

# 오라클에 직접 넣기
# 여기서 한꺼번에 하니 시간이 너무 많이 걸림
# SU_Pandas_MO.SU_MO_DfOracleInsert(TDF, SU_Init.G_SU_Connection,'GB02', 1)

print("=" * 50 + " 데이터베이스 구축 완료")