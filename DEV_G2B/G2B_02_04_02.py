# 나라장터 입찰공고정보서비스 [나라장터검색조건에 의한 입찰공고용역조회]
# 2. 나라장터 입찰공고정보서비스 (BidPublicInfoService02)
# 이 버전은 G2B_02_04 이전보다 상세하게 엑셀로 출력함
import sys
sys.path.append("c:\\work\\PLangVim")


import bs4
import requests
from datetime import datetime, timedelta
import PY_PKG.SU_Pandas_MO as sp
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import Request, urlopen
from lxml import html
import pandas as pd
from re import sub
import re


print("======================> 데이터추출 시작\n\n")

# 데이터프레임 전역변수
gdf = pd.DataFrame()

# 파일명
fname = datetime.now().strftime('%Y-%m-%d')

# 변수선언
xmlUrl = 'http://apis.data.go.kr/1230000/BidPublicInfoService03/getBidPblancListInfoServcPPSSrch'
My_API_Key = unquote(
    'E1j62il6jQPHJEDMntSkDvz5bhOQZYjv%2Bx8s%2F8m84uwkxeZy6CJk%2Bsv5rK4FJu2aZt7l98VLSybWfoJzElQnjg%3D%3D')


# 탭처리가 귀찮아서 일단 날짜별 5번씩 돌자. 5개만 해도 충분함
tabList = [1, 2, 3, 4, 5]

# 자정은 금일이 6일이라고 하면 202212060000로 표시하거나 202212052400으로 표시 함
start_find_d = datetime(2022, 12, 23)                            # 찾기를 원하는 시작일
end_find_d = datetime.now().strftime('%Y%m%d') + '0000'         # 종료일자(금일정보). 즉 시작일부터 금일까지 공공조회

fday = start_find_d                         # 기간검색의 시작일
bday = start_find_d + timedelta(days=1)     # 기간검색의 다음일(시작일 + 1)

# 기간 검색을 위한 것
from_d = fday.strftime('%Y%m%d') + '0000'   # fday에 시간만 붙인것
to_d = bday.strftime('%Y%m%d') + '0000'  # bday에 시간만 붙인것

while from_d <= end_find_d:
    for tabnum in tabList:
        strtabnum = str(tabnum)

        queryParams = '?' + urlencode(
            {
                quote_plus('numOfRows'): '900',                # 한 페이지 결과수
                quote_plus('pageNo'): strtabnum,               # 페이지 번호
                quote_plus('ServiceKey'): My_API_Key,          # 키
                # 1.공고일시, 2.개찰일시
                quote_plus('inqryDiv'): '1',
                quote_plus('inqryBgnDt'): from_d,         # 조회시작일(YYYYMMDDHHMM)
                # 조회종료일(YYYYMMDDHHMM)
                quote_plus('inqryEndDt'): to_d,
                quote_plus('presmptPrceBgn'): 1000,
                # quote_plus('bidNtceNm'): '화학',               # 입찰명, 적용할일 없음
                # quote_plus('dminsttCd') : 'Z021143',          # 수요기관코드, 특정기간만 구할 때
                quote_plus('indstrytyCd'): '1468',
                # quote_plus('indstrytyNm') : '소프트웨어사업자',  # 업종명
                quote_plus('bidClseExcpYn'): 'Y'               # 입찰마감제외여부
                # quote_plus('intrntnlDivCd') : '1'             # 국내-1, 국제-2 구분
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

                    if i == 0:   # 컬럼헤더를 담는다. 첫번째 일때만
                        colName.append(itemResult[j].name)

                    rValue = itemResult[j].text
                    rValueList.append(rValue)

                resultList.append(rValueList)

            # 컬럼값을 소문자로 일괄 변경해야 편한다. 나중에 오라클에 한방에 넣어서 뭔가 분석할 때
            for index in range(len(colName)):
                colName[index] = str(colName[index]).lower()

            # 결과를 데이터프레임으로 변경
            df1 = pd.DataFrame(resultList, columns=colName)

            if len(df1.index) > 0:
                if gdf.shape[0] == 0:
                    gdf = df1.copy()
                else:
                    gdf = pd.concat([gdf, df1], axis=0, ignore_index=True)

            print(fday.strftime('%Y-%m-%d =======>> ' + strtabnum))

    # 날짜를 하루씩 업데이트
    fday   = fday + timedelta(days=1)
    bday   = bday + timedelta(days=1)
    
    from_d = fday.strftime('%Y%m%d') + '0000'
    to_d   = bday.strftime('%Y%m%d') + '0000'  

if len(gdf) == 0:
    print("======================> 결과가 존재하지 않음")
else:
    strQ = "(infobizyn == 'Y')"
    gresult = gdf.query(strQ)

    # strQ = "bidntcenm.str.contains('구축|개선|시스템|포털|홈페이지|정보|db', na=False, regex=True, case=False)"
    # gresult = gresult.query(strQ)

    # 사업금액이 있는 것만 조회
    # strQ = "asignbdgtamt.str.contains('\d', regex=True)"
    # gresult = gresult.query(strQ)
    
    # 유지보수라는 단어가 없는 것
    gresult = gresult[~gresult['bidntcenm'].str.contains('유지',regex=True)]

    # 사업금액을 숫자형태로 변환
    gresult['asignbdgtamt'] = gresult['asignbdgtamt'].astype('float')

    columns = {'bidntceno':'입찰공고번호','bidntceord': '입찰공고차수','rentceyn':'재공고여부','ntcekindnm':'공고종류명',
               'ntcekindnm':'공고종류명','bidntcedt':'입찰공고일시','bidqlfctrgstdt':'입찰참가자격등록마감일시','bidclsedt':'입찰마감일시','asignbdgtamt':'사업금액',
               'opengdt':'개찰일시','bidntcenm':'입찰공고명','bidmethdnm':'입찰방식명','cntrctcnclsmthdnm':'계약체결방법명','dminsttcd':'수요기관코드',
               'dminsttnm':'수요기관','rbidpermsnyn':'재입찰허용여부','prearngprcedcsnmthdnm':'예정가격결정방법명','opengplce':'개찰장소','dcmtgoprtndt':'설명회실시일시',
               'dcmtgoprtnplce':'설명회실시장소','bidntcedtlurl':'입찰공고상세url','bfspecrgstno':'사전규격등록번호','sucsfbidmthdnm':'낙찰방법명','infobizyn':'정보화사업',
               'bidprtcptlmtyn':'입찰참가제한여부'}
    gresult = gresult[columns]
    gresult.rename(columns=columns, inplace=True)


    # 중복값을 제거하자, 조달청 api가 조금 명확하지 않음
    gresult = gresult.drop_duplicates()
    sp.SU_MO_To_excel(gresult, "C:\\work\\제안요청서\\"+fname+"_공고현황.xlsx")

    print("======================> 완료")
