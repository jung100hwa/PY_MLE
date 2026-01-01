import sys
sys.path.append("c:\\work\\PLangVim")

import PY_PKG.SU_DirFile_MO as pFile
import PY_PKG.SU_File_Convert as pConvert
import PY_PKG.SU_Mail_Send_Mo as pMail
import openpyxl as op
import datetime
import os
import platform
import pymysql
import pyodbc
import time
import cx_Oracle


######################################################## 기본 변수 설정
GPR_CUR_POS = os.getcwd()       # 현재 실행 위치 담기

GPR_CUR_TIME = datetime.datetime.now().strftime('%Y-%m-%d')     # 오늘날짜 세팅

GPR_PLATFORM    = platform.system()     # 플랫폼 및 구분자
GPR_SPLIT_GUBUN = ''

if GPR_PLATFORM == 'Windows':
    GPR_CUR_POS = GPR_CUR_POS + '\\'
    GPR_SPLIT_GUBUN = '\\'
else:
    GPR_CUR_POS = GPR_CUR_POS + '/'
    GPR_SPLIT_GUBUN = '/'

GPR_LOGFOLDER       = GPR_CUR_POS + "LOG" + GPR_SPLIT_GUBUN             # 로그파일 기록 폴더
GPR_INIT_FILEFOLDER = GPR_CUR_POS + "INITFILE" + GPR_SPLIT_GUBUN        # 원본파일
GPR_TRNS_PDFFOLDER  = GPR_CUR_POS + "PDF" + GPR_SPLIT_GUBUN             # PDF 변환파일


######################################################## 데이터베이스 연결
print("==================> 데이터베이스 연결")
os.putenv('NLS_LANG', '.UTF8')
GPR_Connection = cx_Oracle.connect('scott/tiger2@192.168.56.1:1521/XE')
GPR_Cursor     =  GPR_Connection.cursor()

######################################################## 데이터베이스 모니터링
print("==================> 데이터베이스 모니터링")
rowcount   = 1
strLogList = []

while True:
    or_sql = "SELECT * FROM T_MON"
    GPR_Cursor.execute(or_sql)
    rows = GPR_Cursor.fetchall()

    if len(rows) > 0:
        for row in rows:
            strAC    = str(row[0])
            strBC    = str(row[1])
            strLog   = str(rowcount) + " ===> " + strAC + " , " + strBC
            rowcount = rowcount + 1

            # 이력테이블에 넣고 기존데이터 삭제
            or_sql = """INSERT INTO T_MON_BAK VALUES('%s','%s')""" % (strAC, strBC)
            GPR_Cursor.execute(or_sql)
            print(or_sql)
    
            or_sql = """DELETE FROM T_MON WHERE AC = '%s'""" % (strAC)
            GPR_Cursor.execute(or_sql)
            GPR_Connection.commit()

            strLogList.append(strLog)

        # 한글 파일을 PDF 파일로 변환 
        # pConvert.sfc_hwptopdf(GPR_INIT_FILEFOLDER,GPR_TRNS_PDFFOLDER)
        
        # pdf 파일을 읽음
        # pFile.SU_MO_PdfRead_Tika(GPR_TRNS_PDFFOLDER)
        
        # 한글 파일을 한글 파일로 변환(버전만, 예를 들면 hwpx -> hwp) 
        # pConvert.sfc_hwptopdf3(GPR_INIT_FILEFOLDER,GPR_TRNS_PDFFOLDER)
        
        # 한글문서에서 독소조항, 추천항목을 사용자아이디별로 결과를 돌려준다.

        listNo = ["현지어 기업 페이지","구성(IP주소로", "착수계"]
        listOk = ["매칭·상담·계약 등 全"]
        userID = "jung100hwa"
        pFile.SU_MO_HwpRead_NoOk(GPR_TRNS_PDFFOLDER,listNo,listOk, userID)

        # listNo = ["현지어 기업 페이지","구성(IP주소로", "착수계"]
        # listOk = ["매칭·상담·계약 등 全"]
        # userID = "jung100hwa"
        # pFile.SU_MO_HwpRead_NoOk(GPR_TRNS_PDFFOLDER,listNo,listOk, userID)
        
        # 메일 보내기
        # msgsubject = "주제"
        # msgbody    = "메일테스트"
        # msgaddr    = "jung2hwa@naver.com"
        # fileadd    = GPR_TRNS_PDFFOLDER + "[별지 5] 정보화사업 착수계(행정기관 및 공공기관 정보시스템 구축·운영 지침).hwp"
        # pMail.SU_MO_MailSend(msgsubject, msgbody, msgaddr, fileadd)

                
        # 로그파일 기록   
        pFile.SU_MO_FileWrite3(GPR_LOGFOLDER, strLogList, GPR_SPLIT_GUBUN, 700)
        
        strLogList = []
    else:
        strdate = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        print(strdate + " event waiting....")

    time.sleep(5)