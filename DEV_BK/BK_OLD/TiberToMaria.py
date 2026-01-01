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
print("==================================================================> 티베로 연결 테스트")
gtm_Tconn  = pyodbc.connect(DSN='DATAWARE',UID='BKUSER',PWD='KOTRABK')
gtm_Tcur  = gtm_Tconn.cursor()



# 인서트구문만들기
gtm_Tinsert = "INSERT INTO bkdb.bk_acn_info_t VALUES("
for item in range(0,23):
    gtm_Tinsert =gtm_Tinsert+"%s,"
gtm_Tinsert = gtm_Tinsert[0:-1] +")"

# 테이블 값 리스트에 담기
# gtm_Tcur.execute("SELECT * FROM BKUSER.BK_ACN_INFO_T WHERE ACN_SN =833")
gtm_Tcur.execute("SELECT * FROM BKUSER.BK_ACN_INFO_T")
gtm_Trows = gtm_Tcur.fetchall()


for row in gtm_Trows:
    print(row)

gtm_Trows2 = []
for row in gtm_Trows:
    gtm_Trows2.append(tuple(row))


gtm_Tconn.close()


print("==================================================================> 마리아 연결 테스트")

# gtm_Tinsert = """INSERT INTO bkdb.bk_acn_info_t3(ACN_SN,ACN_DATE,ACN_BEGIN_TIME,ACN_END_TIME,ACN_REQ_END_DATE,ACN_DATE_KR,ACN_BEGIN_TIME_KR,ACN_END_TIME_KR,ACN_REQ_END_DATE_KR,OPENER_ID,ACN_STATUS,CMMRC_PBLINSTT_CODE,CMMRC_PBLINSTT_NATION_CODE,CMMRC_PBLINSTT_NM,MEM_ID,ACN_GOODS_SN,ACN_GOODS_NM,CTGRY_CODE,DELETE_YN,REGISTER_ID,RGSDE_DT,UPDUSR_ID,UPDDE_DT) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


# gtm_Tinsert = "INSERT INTO bkdb.bk_acn_info_t3(ACN_SN,ACN_DATE) values(%s,%s)"

# gtm_Trows = []
# str = (1731.0, '20170102', '1000', '1050', 'None', '20170102', '1400', '1450', 'None', 'sherboss@list.ru', 4.0, 'KTC147', 5315', 'TASHKENT', 'None', 3057930.0, 'NONWOVEN MACHINERY', '712101', 'N', 'sherboss@list.ru', datetime.datetime(2016, 12, 24, 14, 53, 36), 'sherboss@list.ru', datetime.datetime(2016, 12, 24, 14, 53, 36))

# str ="""('a', 'b', '1000', '1050', 'None', '20170102', '1400', '1450', 'None', 'c', '4.0', 'KTC147', '5315', 'TASHKENT', 'None', '3057930.0', 'd', '712101', 'N', 'k', 'kkk', 'a', 'kkk')"""

# gtm_Tinsert = "INSERT INTO bkdb.bk_acn_info_t3(ACN_SN,ACN_DATE,ACN_BEGIN_TIME,ACN_END_TIME,ACN_REQ_END_DATE,ACN_DATE_KR) values(%s,%s,%s,%s,%s,%s)"
# gtm_Tinsert = "INSERT INTO bkdb.bk_acn_info_t3(ACN_SN,ACN_DATE,ACN_BEGIN_TIME,ACN_END_TIME,ACN_REQ_END_DATE,ACN_DATE_KR) values(%s)"
# # str ="(984.0, '20151028', '1600', '1650', '201510251600', '20151028', '1700', '1750', '201510251700', 'abcor_ind_corp05@yahoo.com.ph', 90.0, 'KTC052', '1109', 'MANILA', 'aaaa', 0.0, 'aaa', 'aaaa', 'N', '970089', datetime.datetime(2015, 10, 27, 18, 6, 30), 'seoulsec09', datetime.datetime(2015, 10, 28, 17, 8, 59)"
# str ="(984.0)"

# gtm_Trows.append(str)

# 마리아 DB연동
gtm_Mconn = pymysql.connect(host='180.100.215.207',port=13306, user='root', 
                       password='mariadb2022!', db='db_bk', charset='utf8')
gtm_Mcur = gtm_Mconn.cursor()

# gtm_Tinsert="insert into bkdb.bk_acn_info_t2 values(%s,%s,%s,%s)"
# str = (111,'bbb','ccc',datetime.datetime(2016, 12, 24, 14, 53, 36))
# gtm_Trows.append(str)

# str = (222,'bbb','ccc',datetime.datetime(2016, 12, 24, 14, 53, 36))
# gtm_Trows.append(str)

# gtm_Tinsert = "INSERT INTO bkdb.bk_acn_info_t3(ACN_SN,ACN_DATE) values(%s,%s)"
# str =(232, 'aaaa')

# gtm_Trows = []
# str= (8333.0, '20150910', '1000', '1050', '201509071000', '20150910', '1700', '1750', '201509071700', 'pep@amleg.dk', 47.0, 'KTC023', '5107', 'COPENHAGEN', None, 0.0, None, None, 'N', '203017', datetime.datetime(2015, 9, 10, 15, 33, 3), '208035', datetime.datetime(2015, 9, 10, 17, 23, 33))
# gtm_Trows.append(str)

# str = gtm_Trows[0]

# gtm_Trows = []
# gtm_Trows.append(str)

# print(str)
# gtm_Mcur.executemany(gtm_Tinsert,gtm_Trows[0])
# gtm_Mcur.executemany(gtm_Tinsert, gtm_Trows2)
# gtm_Mcur.executemany(gtm_Tinsert, gtm_Trows)

# print(gtm_Trows[0])



# # strinsert = "INSERT INTO bkdb.bk_acn_info_t3(ACN_SN) values(333)"
# # gtm_Mcur.execute(strinsert)

# aaa = []
# aaa.append(gtm_Trows[0])
# aaa.append(gtm_Trows[1])

# str = (833.0, '20150910', '1000', '1050', '201509071000', '20150910', '1700', '1750', '201509071700', 'pep@amleg.dk', 47.0, 'KTC023', '5107', 'COPENHAGEN', None, 0.0, None, None, 'N', '203017', datetime.datetime(2015, 9, 10, 15, 33, 3), '208035', datetime.datetime(2015, 9, 10, 17, 23, 33))
# print(str)
# aaa.append(str)
# str = (864.0, '20150921', '0900', '0950', '201509180900', '20150921', '1100', '1150', '201509181100', 'rejeki_agung_makmursby@yahoo.com', 47.0, 'KTC146', '1105', 'SURABAJA', None, 0.0, None, None, 'N', '970089', datetime.datetime(2015, 9, 21, 14, 55, 46), '715016', datetime.datetime(2015, 9, 21, 18, 17, 6))
# aaa.append(str)
# gtm_Mcur.executemany(gtm_Tinsert, aaa)

# for row in gtm_Trows:
#     gtm_Mcur.execute(gtm_Tinsert,row)

# gtm_Mconn.commit()
# gtm_Mconn.close()


# str= (833.0, '20150910', '1000', '1050', '201509071000', '20150910', '1700', '1750', '201509071700', 'pep@amleg.dk', 47.0, 'KTC023', '5107', 'COPENHAGEN', None, 0.0, None, None, 'N', '203017', datetime.datetime(2015, 9, 10, 15, 33, 3), '208035', datetime.datetime(2015, 9, 10, 17, 23, 33))


# (984.0, '20151028', '1600', '1650', '201510251600', '20151028', '1700', '1750', '201510251700', 'abcor_ind_corp05@yahoo.com.ph', 90.0, 'KTC052', '1109', 'MANILA', None, 0.0, None, None, 'N', '970089', datetime.datetime(2015, 10, 27, 18, 6, 30), 'seoulsec09', datetime.datetime(2015, 10, 28, 17, 8, 59)


# (833.0, '20150910', '1000', '1050', '201509071000', '20150910', '1700', '1750', '201509071700', 'pep@amleg.dk', 47.0, 'KTC023', '5107', 'COPENHAGEN', None, 0.0, None, None, 'N', '203017', datetime.datetime(2015, 9, 10, 15, 33, 3), '208035', datetime.datetime(2015, 9, 10, 17, 23, 33))


# str = (833.0, '20150910', '1000', '1050', '201509071000', '20150910', '1700', '1750', '201509071700', 'pep@amleg.dk', 47.0, 'KTC023', '5107', 'COPENHAGEN', None, 0.0, None, None, 'N', '203017', datetime.datetime(2015, 9, 10, 15, 33, 3), '208035', datetime.datetime(2015, 9, 10, 17, 23, 33))
# print(str)
# aaa.append(str)
# str = (864.0, '20150921', '0900', '0950', '201509180900', '20150921', '1100', '1150', '201509181100', 'rejeki_agung_makmursby@yahoo.com', 47.0, 'KTC146', '1105', 'SURABAJA', None, 0.0, None, None, 'N', '970089', datetime.datetime(2015, 9, 21, 14, 55, 46), '715016', datetime.datetime(2015, 9, 21, 18, 17, 6))
# aaa.append(str)
# bList = [
# (83344.0, '20150910'),
# (86444.0, '20150921')
# ]
# aList = []
# aList.append(gtm_Trows[0])
# aList.append(gtm_Trows[1])

# bList.append(tuple(gtm_Trows[0]))
# bList.append(tuple(gtm_Trows[1]))
gtm_Mcur.executemany(gtm_Tinsert, gtm_Trows2)
gtm_Mconn.commit()
gtm_Mconn.close()
# print(aList)
# print(bList)