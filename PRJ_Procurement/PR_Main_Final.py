# os : 리눅스 기반 솔루션에서 작동
# 데이터베이스 : 오라클
import sys
import os
import openpyxl as op
import datetime
import platform
import time
import cx_Oracle
import glob
import re
import zipfile
import Pro_Hwp_Read_MO as phwp
import Pro_Mo as po
import io


po.Pro_Init()
######################################################## 데이터베이스 모니터링

rowcount = 1
strLogList = []

while True:
    or_sql = "SELECT * FROM T_MON"
    po.GPR_Cursor.execute(or_sql)
    rows = po.GPR_Cursor.fetchall()

    if len(rows) > 0:
        for row in rows:
            strAC = str(row[0])  # 공고번호
            strBC = str(row[1])  # 공고명
            strurl = str(row[2])  # 첨부파일위치
            strLog = str(rowcount) + " ===> " + strAC + " , " + strBC
            rowcount = rowcount + 1

            # URL에 포함된 파일을 다운로드 해보자. 현재는 하나의 파일 다운 -> 텍스트 추출
            strurl = po.SU_Http_Https_Find(strurl)
            po.SU_Http_File_Download(po.GPR_TRNS_HWPFOLDER, strurl, rowcount)

            # 첨부파일이 있는 특정 폴더를 모니터링 해서 DB에 넣는다.
            po.SU_FOLD_MONITORING2(po.GPR_TRNS_HWPFOLDER, po.GPR_TXT_SALVEFOLDER, strAC)

            # 이력테이블에 넣고 기존데이터 삭제. 이게 필요 없을 수도 있다.
            or_sql = """INSERT INTO T_MON_BAK VALUES('%s','%s')""" % (strAC, strBC)
            po.GPR_Cursor.execute(or_sql)
            print(or_sql)

            # 모니터링 테이블에서는 삭제.
            or_sql = """DELETE FROM T_MON WHERE AC = '%s'""" % (strAC)
            po.GPR_Cursor.execute(or_sql)
            po.GPR_Connection.commit()

            # 로그리스트에 등록
            strLogList.append(strLog)

        # 로그파일 기록
        po.SU_MO_FileWrite3(po.GPR_LOGFOLDER, strLogList, po.GPR_SPLIT_GUBUN, 700)
    else:
        strdate = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        print(strdate + " event waiting....")

    time.sleep(1)
