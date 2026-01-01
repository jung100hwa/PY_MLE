import openpyxl as op
import datetime
import os
import platform
import pymysql
import pyodbc

############################################################### 기본 변수 세팅
# 현재 실행 위치 담기
gtm_filepos = os.getcwd()

# 오늘날짜 세팅
gtm_now = datetime.datetime.now().strftime('%Y-%m-%d')

# 플랫폼 담기
gtm_platform = platform.system()

gtm_splitdef = ''

# 필요한 파일들 여기에다 위치시키기
if gtm_platform == 'Windows':
    gtm_filepos = gtm_filepos + '\\BK\\FILE\\'
    gtm_splitdef = '\\'
else:
    gtm_filepos = gtm_filepos + '/BK/FILE/'
    gtm_splitdef = '/'

os.putenv('NLS_LANG', '.UTF8')

############################################################### 데이터베이스 연결
# 티베로 연동
print("==================> 티베로 연결 테스트")
gtm_Tconn  = pyodbc.connect(DSN='DATAWARE',UID='BKUSER',PWD='KOTRABK')
gtm_Tcur  = gtm_Tconn.cursor()

# 마리아 DB연동
print("=================> 마리아 연결 테스트")
gtm_Mconn = pymysql.connect(host='180.100.215.207',port=13306, user='root', 
                       password='mariadb2022!', db='db_bk', charset='utf8')
gtm_Mcur = gtm_Mconn.cursor()



############################################################### 티베로 데이터 가져오기 및 컬럼개수 세팅
# 티베로 테이블 값 리스트에 담기
print("=================> 티베로 데이터 가져오기")
gtm_Tcur.execute("SELECT * FROM BKUSER.bk_auth_acd_t")
gtm_Trows = gtm_Tcur.fetchall()

gtm_Trows2 = []
for row in gtm_Trows:
    gtm_Trows2.append(tuple(row))

gtm_Tconn.close()


# 마리에 넣을 인서트 구문 넣기
print("=================> 마리아에 넣기 위한 인서트 구문 만들기")
colCount = len(gtm_Trows2[0])
gtm_Tinsert = "INSERT INTO bkdb.bk_auth_acd_t VALUES("
for item in range(0,colCount):
    gtm_Tinsert =gtm_Tinsert+"%s,"
gtm_Tinsert = gtm_Tinsert[0:-1] +")"


############################################################### 마리아에 티베로 데이터 넣기
print("=================> 마리아 데이터 인서트")
gtm_Mcur.executemany(gtm_Tinsert, gtm_Trows2)
gtm_Mconn.commit()


gtm_Mconn.close()