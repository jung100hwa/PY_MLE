import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import PY_PKG.SU_ALLMO_Init_MO as psai
import PY_PKG.SU_DirFile_MO as pFile
import PY_PKG.SU_File_Convert as pConvert
import PY_PKG.SU_Mail_Send_Mo as pMail
import openpyxl as op
import datetime
import platform
import time
import cx_Oracle


######################################################## 기본 변수 설정
psai.SU_MO_VarInit(psai.G_SU_INIT_LIST,"DV_PROCUREMENT")

GPR_CUR_POS  = psai.G_SU_ProFilLoc                               # 현재 실행 위치 담기
GPR_PLATFORM = platform.system()                                 # 플랫폼 및 구분자

GPR_SPLIT_GUBUN     = psai.G_SU_SplitDef
GPR_LOGFOLDER       = GPR_CUR_POS + "LOG" + GPR_SPLIT_GUBUN             # 로그파일 기록 폴더
GPR_INIT_FILEFOLDER = GPR_CUR_POS + "INITFILE" + GPR_SPLIT_GUBUN        # 원본파일
GPR_TRNS_PDFFOLDER  = GPR_CUR_POS + "PDF" + GPR_SPLIT_GUBUN             # PDF 변환파일
GPR_TRNS_HWPFOLDER  = GPR_CUR_POS + "HWP" + GPR_SPLIT_GUBUN             # HWP 조달사업지침서



######################################################## 데이터베이스 연결
print("==================> 데이터베이스 연결")
os.putenv('NLS_LANG', '.UTF8')
GPR_Connection = psai.G_SU_Connection
GPR_Cursor     = psai.G_SU_Cursor


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

            # 모니터링 테이블에서는 삭제
            or_sql = """DELETE FROM T_MON WHERE AC = '%s'""" % (strAC)
            GPR_Cursor.execute(or_sql)
            GPR_Connection.commit()

            # 로그리스트에 등록
            strLogList.append(strLog)

        # 한글 파일을 PDF 파일로 변환, 
        # pConvert.sfc_hwptopdf(GPR_INIT_FILEFOLDER, GPR_TRNS_PDFFOLDER)
        
        # 변환된 pdf 파일에서 독소조항, 희망조항 찾기
        # listNo = ["변환"]
        # listOk = ["허길양", "만세"]
        # userID = "jung100hwa"
        # pFile.SU_MO_PdfRead_Tika_NoOk(GPR_TRNS_PDFFOLDER,listNo, listOk, userID )

        # # 한글 파일을 한글 파일로 변환(버전만, 예를 들면 hwpx -> hwp)
        # pConvert.sfc_hwptopdf3(GPR_INIT_FILEFOLDER,GPR_TRNS_PDFFOLDER)

        # # 한글문서에서 독소조항, 추천항목을 사용자아이디별로 결과를 돌려준다.
        listNo = ["소재지가 경상남도 내", "고압가스특정제조(1473)"]
        listOk = ["세부품명번호 1214190401(산소가스)"]
        userID = "jung100hwa"
        pFile.SU_MO_HwpRead_NoOk(GPR_TRNS_HWPFOLDER, listNo, listOk, userID)

        # # 메일 보내기
        # msgsubject = "주제"
        # msgbody    = "메일테스트"
        # msgaddr    = "jung2hwa@naver.com"
        # attachments = [os.path.join(os.getcwd(), 'aa.txt'), os.path.join(os.getcwd(), 'bb.txt')]
        # pMail.SU_MO_MailSend(msgsubject, msgbody, msgaddr, attachments)

        # # 로그파일 기록
        # pFile.SU_MO_FileWrite3(GPR_LOGFOLDER, strLogList, GPR_SPLIT_GUBUN, 700)

        strLogList = []
    else:
        strdate = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        print(strdate + " event waiting....")

    time.sleep(1)