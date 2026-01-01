# 나라장터 입찰공고정보서비스 [나라장터검색조건에 의한 입찰공고용역조회]
# 2. 나라장터 입찰공고정보서비스 (BidPublicInfoService02)

from re import sub
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
import xml.etree.ElementTree as ET
import SU_Init as SU_Init
import SU_Pandas_MO
import SU_Excel_MO
from datetime import datetime, timedelta
import time
import numpy as np

# 변수선언
xmlUrl = 'http://apis.data.go.kr/1230000/BidPublicInfoService02/getBidPblancListInfoServcPPSSrch'
My_API_Key  = unquote('E1j62il6jQPHJEDMntSkDvz5bhOQZYjv%2Bx8s%2F8m84uwkxeZy6CJk%2Bsv5rK4FJu2aZt7l98VLSybWfoJzElQnjg%3D%3D')

# 기본적으로 데이터베이스 연결
SU_Init.SU_MO_VarInit(0)

startday = datetime(2022, 2, 28)
strendday = datetime.now().strftime('%Y%m%d') + '0000'

beforeday = startday
afterday  = startday + timedelta(days=1)

# 기간 검색을 위한 것
strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
strafterday  = afterday.strftime('%Y%m%d')  + '0000'

while strbeforeday <= strendday:
    queryParams = '?' + urlencode(
        {
            quote_plus('numOfRows') : '999',
            quote_plus('pageNo') : '1',
            quote_plus('ServiceKey') : My_API_Key,
            # quote_plus('type') : 'json',                  # json으로 받고 싶을 때. json 기입
            quote_plus('inqryDiv'): '1',                    # 1.공고일시, 2.개찰일시
            quote_plus('inqryBgnDt'): strbeforeday,         # 조회시작일(YYYYMMDDHHMM)
            quote_plus('inqryEndDt'): strafterday,          # 조회종료일(YYYYMMDDHHMM)
            # quote_plus('bidNtceNm') : '시스템',            # 입찰공고명
            # quote_plus('ntceInsttCd') : '0000000000',     # 공고기관코드
            # quote_plus('ntceInsttNm') : '0000000000',     # 공고기관명
            # quote_plus('dminsttCd') : '0000000000',       # 수요기관코드
            # quote_plus('dminsttNm') : '0000000000',       # 수요기관명
            # quote_plus('refNo') : '0000000000',           # 참조번호
            # quote_plus('prtcptLmtRgnCd') : '0000000000',  # 참가제한지역코드
            # quote_plus('prtcptLmtRgnNm') : '0000000000',  # 참가제한지역명
            # quote_plus('indstrytyCd') : '1468',           # 업종코드
            quote_plus('indstrytyNm') : '소프트웨어사업자',    # 업종명
            # quote_plus('presmptPrceBgn') : '0000000000',  # 추정가격시작
            # quote_plus('presmptPrceEnd') : '0000000000',  # 추정가격종료
            # quote_plus('dtilPrdctClsfcNo') : '0000000000',# 세부품명번호
            # quote_plus('prcrmntReqNo') : '0000000000',    # 조달요청번호
            # quote_plus('bidClseExcpYn') : '0000000000',   # 입찰마감제외여부
            quote_plus('intrntnlDivCd') : '1',              # 국내-1, 국제-2 구분
            # quote_plus('masYn') : '0000000000',           # 다수공급경쟁자여부
            }
    )

    # 여기서 데이터를 가져온다.
    response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

    # 실제데이터 테그는 item, 기간에 해당하는 모든 데이터를 담고 있다.
    allResult = xmlobj.findAll('item')

    # 단지 컬럼명을 구하기 위한 것
    if len(allResult) > 0:
        
        resultList  = []   # 전체 결과값 리스트
        colName     = []   # 컬럼리스트
        resultCount = len(allResult)  # 결과개수

        for i in range(0, resultCount):
            
            itemResult = allResult[i].find_all()
            colCount   = len(itemResult)
            rValueList = []  # 한건에 대한 결과값 리스트. 이것을 resultList에 추가
            
            for j in range(0, colCount):
                
                if i == 0:                              # 컬럼헤더를 담는다. 첫번째 일때만
                    colName.append(itemResult[j].name)

                rValue = itemResult[j].text
                rValueList.append(rValue)

            resultList.append(rValueList)

        # 컬럼값을 소문자로 일괄 변경해야 오라클에 한방에 들어간다.
        for index in range(len(colName)):
            colName[index]=str(colName[index]).lower()

        # 결과를 데이터프레임으로 변경
        df1 = pd.DataFrame(resultList, columns=colName)

        # 정보화 사업인데 정보사업컬럼에 NULL 인게 있다. 용역구분, 기술용역은 대체적으로 토목공사 등
        # 그런데 기술용역 중에 GIS DB 구축이 있다. 정말 일관성이라고는...
        # strQ = "(infobizyn == 'Y') and (srvcedivnm == '일반용역')"
        # strQ = "srvcedivnm == '일반용역'"
        # df1 = df1.query(strQ)

        if len(df1.index) > 0 :
            # 속도가 늦어 분활해서 DB넣기
            SU_Pandas_MO.SU_MO_DfOracleInsert(df1, SU_Init.G_SU_Connection, 'GB021', 1)

    # 날짜를 하루씩 업데이트
    beforeday = beforeday + timedelta(days=1)
    afterday  = afterday + timedelta(days=1)
    strbeforeday = beforeday.strftime('%Y%m%d') + '0001'
    strafterday  = afterday.strftime('%Y%m%d') + '0000'
        
print("======================> 기본 정보화 사업완료")