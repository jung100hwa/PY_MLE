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

# 탭처리가 귀찮아서 일단 날짜별 5번씩 돌자.
tabList = [1,2,3,4,5]

# 만약에 오늘이라고 하면 어제날짜부터 해야 함. 보통 공고일일 202203060000 이기 때문에
# 오늘잘짜부터 하면 202203060001 이렇게 검색하다보니 오늘 날짜가 나오지 않는다.
startday = datetime(2022, 3, 6)
strendday = datetime.now().strftime('%Y%m%d') + '0000'

beforeday = startday
afterday  = startday + timedelta(days=1)

# 기간 검색을 위한 것
strbeforeday = beforeday.strftime('%Y%m%d') + '0000'
strafterday  = afterday.strftime('%Y%m%d')  + '0000'

while strbeforeday <= strendday:
    for tabnum in tabList:
        strtabnum = str(tabnum)

        queryParams = '?' + urlencode(
            {
                quote_plus('numOfRows') : '900',
                quote_plus('pageNo') : strtabnum,
                quote_plus('ServiceKey') : My_API_Key,
                quote_plus('inqryDiv'): '1',                    # 1.공고일시, 2.개찰일시
                quote_plus('inqryBgnDt'): strbeforeday,         # 조회시작일(YYYYMMDDHHMM)
                quote_plus('inqryEndDt'): strafterday,          # 조회종료일(YYYYMMDDHHMM)
                quote_plus('bidClseExcpYn') : 'Y',              # 입찰마감제외여부
                # quote_plus('dminsttCd') : '1480592',            # 수요기관코드
                quote_plus('intrntnlDivCd') : '1'               # 국내-1, 국제-2 구분
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
            
            # 정보화산업만
            # strQ = "(infobizyn == 'Y')"
            # df1 = df1.query(strQ)

            if len(df1.index) > 0 :
                # 속도가 늦어 분활해서 DB넣기
                SU_Pandas_MO.SU_MO_DfOracleInsert(df1, SU_Init.G_SU_Connection, 'GB021', 1)
                # SU_Pandas_MO.SU_MO_To_excel(df1, "C:\\temp\\" + strbeforeday+strtabnum+".xlsx")

            print(beforeday.strftime('%Y-%m-%d =======>> ' +strtabnum))

    # 날짜를 하루씩 업데이트
    beforeday = beforeday + timedelta(days=1)
    afterday  = afterday + timedelta(days=1)
    strbeforeday = beforeday.strftime('%Y%m%d') + '0000'
    strafterday  = afterday.strftime('%Y%m%d') + '0000'
        
print("======================> 기본 정보화 사업완료\n\n")


print("======================> 원하는 정보 뽑아내기\n\n")