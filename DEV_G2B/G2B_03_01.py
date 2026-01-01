# 나라장터 입찰공고정보서비스 [나라장터검색조건에 의한 입찰공고용역조회]
# 3. 나라장터 발주계획서비스 (OrderPlanSttusService)

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
import re


print("======================> 데이터추출\n\n")
# 데이터프레임 전역변수
gdf = pd.DataFrame()

# 파일명
fname = datetime.now().strftime('%Y-%m-%d')

# 변수선언
xmlUrl = 'http://apis.data.go.kr/1230000/OrderPlanSttusService/getOrderPlanSttusListServc'
My_API_Key  = unquote('E1j62il6jQPHJEDMntSkDvz5bhOQZYjv%2Bx8s%2F8m84uwkxeZy6CJk%2Bsv5rK4FJu2aZt7l98VLSybWfoJzElQnjg%3D%3D')


# 탭처리가 귀찮아서 일단 날짜별 5번씩 돌자.
tabList = [1,2,3,4,5]

# 만약에 오늘이라고 하면 어제날짜부터 해야 함. 보통 공고일일 202203060000 이기 때문에
# 오늘잘짜부터 하면 202203060001 이렇게 검색하다보니 오늘 날짜가 나오지 않는다.
startday = datetime(2022, 5, 20)
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
                quote_plus('inqryEndDt'): strafterday          # 조회종료일(YYYYMMDDHHMM)
                # quote_plus('orderInsttNm') : '00000000000'      # 발주기관 코드
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

            if len(df1.index) > 0 :
                if gdf.shape[0] == 0:
                    gdf = df1.copy()
                else:
                    gdf = pd.concat([gdf, df1], axis=0, ignore_index=True)
                    
            print(beforeday.strftime('%Y-%m-%d =======>> ' +strtabnum))

    # 날짜를 하루씩 업데이트
    beforeday = beforeday + timedelta(days=1)
    afterday  = afterday + timedelta(days=1)
    strbeforeday = beforeday.strftime('%Y%m%d') + '0000'
    strafterday  = afterday.strftime('%Y%m%d') + '0000'
        
print("======================> 원하는 정보 추출")

strQ = "(bsnsdivnm == '5') and (cnsttydivnm == '일반용역')"
gdf1 = gdf.query(strQ)

strQ = "biznm.str.contains('시스템|포털|홈페이지|정보|db|DB', regex=True)"
gdf2 = gdf.query(strQ)

result = pd.concat([gdf1, gdf2], axis=0, ignore_index=True)

# 사업금액이 있는 것만 조회
strQ = "sumorderamt.str.contains('\d', regex=True)"
result = result.query(strQ)

# 사업금액을 숫자형태로 변환
result['sumorderamt'] = result['sumorderamt'].astype('float')

columns = {'orderinsttnm':'발주기관명','biznm':'공고사업명','sumorderamt':'사업금액', 'orderyear':'발주년도','ordermnth':'발주월'}
result = result[columns]
result.rename(columns=columns, inplace=True)


# 중복값을 제거하자, 조달청 api가 조금 명확하지 않음
result = result.drop_duplicates()
SU_Pandas_MO.SU_MO_To_excel(result, "C:\\work\\03.제안작성\\"+fname+"_발주계획.xlsx")

print("======================> 완료")
