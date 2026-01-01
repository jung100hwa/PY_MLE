import sys
import os

sys.path.append(os.getcwd())

import platform
import datetime
import cx_Oracle
from sqlalchemy import create_engine

# 데이터베이스 전역변수 설정
G_SU_Connection = None
G_SU_Cursor     = None
G_SU_Engine     = None

# 파일결과 출력
G_SU_ExFilePosIn  = ''
G_SU_ExFilePosOut = ''
G_SU_ExFilePos    = ''
G_SU_ExFileDetail = ''
G_SU_ProFilLoc    = ''


# 시간 등 설정
G_SU_Now          = ''
G_SU_Now_C        = ''
G_SU_Platform     = ''
G_SU_SplitDef     = ''
G_SU_ExFilePosImg = ''
G_SU_LOG          = ''

# 원격서버 정보
G_SU_REMOTE_SERVER = ''
G_SU_REMOTE_USER   = ''
G_SU_REMOTE_PASSWORD = ''
G_SU_REMOTE_PORT = ''

# 초기 일반적인 세팅 리스트
G_SU_INIT_LIST = [0, "c:\\projects\\PY_MLE", "/home/jung100hwa/MLE","scott/tiger2@192.168.56.1:1521/XE",
                  "oracle://scott/tiger2@192.168.56.1:1521/XE","E_FILE", "MONITORING",
                  ["192.168.56.1","jung100hwa","!!hgl1651ok",22]]


# 리스트 순서
# 인덱스 0 : 데이터베이스 연결 유무(0-연결, 1-연결하지 않음), 23년 03월 사용하지 않고, 인자로 받음
# 인덱스 1 : 실제 프로젝트 실행 위치 ex) c:\\work\\MLE
# 인덱스 2 : 리눅스 일때 위치 ex) /home/jung100hwa/MLE
# 인덱스 3 : 아이디와패소드를 포함한 연결 FULL. 예) scott/tiger2@192.168.56.1:1521/XE
# 인덱스 4 : 오라클 핸들링을 위한 엔진 설정으로 사실 필요 없을 듯 예) oracle://scott/tiger2@192.168.56.1:1521/XE
# 인덱스 5 : 파일쓰고 읽기 할 원위치 ex) "E_FILE"
# 인덱스 6 : 모니터링 파일 위치 ex) "MONITORING"
# 인덱스 7 : 원격서버 정보. 이것은 리스트로 작성

# USEFILENAME : 파일명

def SU_MO_VarInit(GVSETTING:list, USEFILENAME='', DBCONNECTION='1'):

    global G_SU_Connection              # 데이터베이스 연결
    global G_SU_Cursor                  # 데이터베이스 커서
    global G_SU_Engine                  # 데이터베이스 좀더 세부적 컨트롤(사용되지 않을 수 있음)

    global G_SU_LOG                     # 모니터링 로그 사이는 위치
    global G_SU_Platform                # os
    global G_SU_SplitDef                # os 분리자
    global G_SU_ExFilePos               # 현재 프로젝 위치
    global G_SU_ExFileDetail            # 프로젝트 아래. 파일 입출력 폴더명(E_FILE)
    global G_SU_ProFilLoc               # E_FILE아래 폴더명


    
    global G_SU_Now                     # 현재 일자
    global G_SU_Now_C                   # 현재 일자를 년-월-일만 표현
    
    global G_SU_REMOTE_SERVER           # 원격서버정보
    global G_SU_REMOTE_USER             # 원격서버 유저
    global G_SU_REMOTE_PASSWORD         # 원격서버 유저 암호
    global G_SU_REMOTE_PORT             # 원격서버 포트


    # 플랫폼 담기
    G_SU_Platform       = platform.system()

    if G_SU_Platform == 'Windows':
        os.chdir(GVSETTING[1])
        G_SU_SplitDef = '\\'
    else:
        os.chdir(GVSETTING[2])
        G_SU_SplitDef = '/'

    G_SU_ExFilePos = os.getcwd()
    G_SU_ExFileDetail = GVSETTING[5]
    G_SU_ProFilLoc    = G_SU_ExFilePos + G_SU_SplitDef + G_SU_ExFileDetail + G_SU_SplitDef + USEFILENAME
    G_SU_LOG = G_SU_ExFilePos + G_SU_SplitDef + G_SU_ExFileDetail + G_SU_SplitDef + GVSETTING[6] + G_SU_SplitDef
    
    # 데이터베이스 세팅, 리눅스에만 세팅되어 있기 때문에
    if DBCONNECTION == 0:
        os.putenv('NLS_LANG', '.UTF8')
        G_SU_Connection = cx_Oracle.connect(GVSETTING[3])
        G_SU_Cursor     = G_SU_Connection.cursor()
        G_SU_Engine     = create_engine(GVSETTING[4])

    # 오늘날짜 세팅
    G_SU_Now  = datetime.datetime.now()
    G_SU_Now_C = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 원격서버 세팅
    G_SU_REMOTE_SERVER = GVSETTING[7][0]
    G_SU_REMOTE_USER   = GVSETTING[7][1]
    G_SU_REMOTE_PASSWORD = GVSETTING[7][2]
    G_SU_REMOTE_PORT = GVSETTING[7][3]