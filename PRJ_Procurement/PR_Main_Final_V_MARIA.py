import sys
import os

# 툴마다 틀려서 넣어 주는게 편하다.
sys.path.append(os.getcwd())

import datetime
import platform
import time
import pymysql
# import mysql.connector as pymysql
import PY_PKG.SU_WEB as SW
import PY_PKG.SU_Folder_Monitoring_MO as SM
import PY_PKG.SU_FILE_WRITE_READ as SFW


######################################################## 기본 변수 설정
G_Platform = platform.system()
G_SPLIT_GUBUN = ""
G_CUR_POS  = ""
if G_Platform == 'Windows':
    G_SPLIT_GUBUN = '\\'
    G_CUR_POS = "c:\\work\\MLE_FILE\\"
    
else:
    G_SPLIT_GUBUN = '/'
    G_CUR_POS="/home/jung100hwa/MLE_FILE"
    
# 상대경로 절대경로 설정이 애매해서 아에 세팅
sys.path.append(G_CUR_POS)

G_LOGFOLDER       = G_CUR_POS + "LOG" + G_SPLIT_GUBUN             # 로그파일 기록 폴더
G_INIT_FILEFOLDER = G_CUR_POS + "INITFILE" + G_SPLIT_GUBUN        # 원본파일
G_TRNS_PDFFOLDER  = G_CUR_POS + "PDF" + G_SPLIT_GUBUN             # PDF 변환파일
G_TRNS_HWPFOLDER  = G_CUR_POS + "HWP" + G_SPLIT_GUBUN             # HWP 조달사업지침서(웹에서 다운로드 받은 파일 저장 경로)
G_TXT_SALVEFOLDER = G_CUR_POS + "RESULT" + G_SPLIT_GUBUN          # HWP 조달사업지침서


######################################################## 데이터베이스 연결
print("======================> DataBase Connect")
os.putenv('NLS_LANG', '.UTF8')

try:
    G_Connection = pymysql.connect(host='192.168.56.1', user='jung100hwa',password='!!hgl1651ok', db='testDB', charset='utf8mb4')
    G_Cursor = G_Connection.cursor()
    
    print("DBConnection is success!!")
except:
    print("DBConnection is not availableon this machine")
    exit()

######################################################## 데이터베이스 모니터링
rowcount = 1

print("======================> Monitoring Start")
try:
    while True:

        strDate = datetime.datetime.now().strftime('%Y-%m-%d')

        # PR_T_MON은 조달사이트에서 수집한 입찰정보 저장 테이블로 읽고 비운다.
        sql = "SELECT AC, STRURL FROM PR_T_ADDFILE"
        G_Cursor.execute(sql)
        rows = G_Cursor.fetchall()
        G_Connection.commit()

        strLogList = []
        if len(rows) > 0:
            for row in rows:
                strAC = str(row[0])             # 공고번호
                strURL = str(row[1])            # 첨부파일위치
                strURLOrg = strURL              # 나중에 테이블에서 지우기 위해

                strLog = str(rowcount) + " ===> " + strAC + ", " + strURL
                rowcount = rowcount + 1
                print(strLog)

                # 첨부파일이 있어야 함. 본 프로젝트의 첨부파일 읽는 것
                if len(strURL) > 10 :
                    # HTTP이면 HTTPS를 붙인다. HTTP는 다운되지 않는 듯
                    strURL = SW.SU_Http_Https_Find(strURL)

                    # 예를 들면 사전규격은 날짜기 지나면(입찰공고가 나오면) 첨부파일을 조달청에서 삭제함
                    SW.SU_Http_File_Download(G_TRNS_HWPFOLDER, strURL, rowcount)

                    # 첨부파일 txt 추출 및 txt 파일 저장. 리턴값은 txt 파일 위치
                    retxtfile = SM.SU_FOLD_MONITORING2(G_TRNS_HWPFOLDER, G_TXT_SALVEFOLDER, G_Cursor, G_Connection, G_SPLIT_GUBUN, 0)

                    if len(retxtfile) > 0:
                        for textfilepath in retxtfile:
                    
                            # 추출한 파일 경로 삽입
                            sql = """INSERT INTO PR_T_MONFILE VALUES('%s','%s','%s')""" % (strAC, textfilepath, strDate)
                            sql=sql.replace('\\','\\\\')  # !!!! 마리아db문제인가 폴더 구분자를 이렇게 변경을 해야 들어가네.!!!!(다음이어서 하시는 분은 찾아서 바꾸세요.), 한글도 에러
                            G_Cursor.execute(sql)
                        
                            # 이력테이블에 삽입
                            sql = """INSERT INTO PR_T_ADDFILE_B VALUES('%s','%s')""" % (strAC, strURL)
                            G_Cursor.execute(sql)
                        
                            # 향후 데이터베이스 설계를 통해 해결해야겠지만 현재는 URL를 키로 해서 삭제 함
                            sql = """DELETE FROM PR_T_ADDFILE WHERE STRURL = '%s'""" % (strURLOrg)
                            G_Cursor.execute(sql)
                            G_Connection.commit()

                    retxtfile = ""

                # 로그리스트에 등록
                strLogList.append(strLog)

            # 로그파일 기록
            SFW.SU_MO_FileWrite3(G_LOGFOLDER, strLogList, G_SPLIT_GUBUN, 70000)
        else:
            strdate = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            print(strdate + " event waiting....")

        # 여기도 향후 테스트 후 sleep 간격 조정해야 함
        time.sleep(1)
except:
    print("error")
    exit(1)