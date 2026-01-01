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
import io
from tika import parser
from urllib import request
from requests import get
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi
import datetime


######################################################## 기본 변수 설정
GPR_CUR_POS  = "/home/jung100hwa/PLangVim/ALL_FILE/DV_PROCUREMENT/"                               # 현재 실행 위치 담기
GPR_SPLIT_GUBUN     = "/"
GPR_LOGFOLDER       = GPR_CUR_POS + "LOG" + GPR_SPLIT_GUBUN             # 로그파일 기록 폴더
GPR_INIT_FILEFOLDER = GPR_CUR_POS + "INITFILE" + GPR_SPLIT_GUBUN        # 원본파일
GPR_TRNS_PDFFOLDER  = GPR_CUR_POS + "PDF" + GPR_SPLIT_GUBUN             # PDF 변환파일
GPR_TRNS_HWPFOLDER  = GPR_CUR_POS + "HWP" + GPR_SPLIT_GUBUN             # HWP 조달사업지침서
GPR_TXT_SALVEFOLDER = GPR_CUR_POS + "RESULT" + GPR_SPLIT_GUBUN          # HWP 조달사업지침서PR_Connection.commit()

GPR_Connection = ''
GPR_Cursor = ''

######################################################## 데이터베이스 연결
def Pro_Init():
    print("==================> 데이터베이스 연결")
    global  GPR_Connection
    global GPR_Cursor
    os.putenv('NLS_LANG', '.UTF8')
    GPR_Connection = cx_Oracle.connect("scott/tiger2@192.168.56.1:1521/XE")
    GPR_Cursor = GPR_Connection.cursor()


########################################################  파일 존재 여부
def SU_MO_FindFilename(Source, FName):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            fn = os.path.basename(file)
            fn = fn.upper()
            if str(FName).upper() == fn:
                return True
    except:
        pass
    return False


########################################################  HWPX 내용추출
def SU_MO_HwpRead_Hwpx(SourceFolder, sfile):
    hwpxstr = ""
    flist = []
    try:
        com = re.compile("<hp:t>.+?</hp:t>", re.MULTILINE)
        com2 = re.compile(r"Contents/section.+")  # 한글은 이런 xml 파일명으로 변경됨. 하나 이상일것 같아서 이렇게 함

        # 파일존재 여부
        if SU_MO_FindFilename(SourceFolder, sfile) == False:
            print("file exist not !!")
            return

        # 풀네임
        fullfilename = SourceFolder + sfile

        # 1. zip으로 파일명 변경
        filen = str(os.path.splitext(sfile)[0])
        file_ext = str(os.path.splitext(sfile)[1])
        nfile = str(sfile).replace(file_ext, ".zip")
        nfilezip = SourceFolder + nfile
        os.rename(fullfilename, nfilezip)

        # 2. 압축해제
        my_zip = zipfile.ZipFile(nfilezip)
        ilist = my_zip.namelist()
        for item in ilist:
            ml = com2.findall(item)
            if len(ml) > 0:
                flist.append(ml[0])

        for name in flist:
            with my_zip.open(name) as readfile:
                for line in io.TextIOWrapper(readfile, "utf-8"):
                    ml = com.findall(line)
                    hwpxstr = hwpxstr + ','.join(ml)

        # 나머지 테그 제거
        p = re.compile('<hp:.+?>|</hp:.+?>')
        hwpxstr = p.sub('', hwpxstr)
        
        return hwpxstr
    except:
        pass
    
    return ""




########################################################  시간
def SU_MO_TimeReturn2():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')


########################################################  로그 파일 적기
def SU_MO_FileWrite3(Source, FileConList, SplitDef, reSize):
    # 로그 파일에 적을 내용
    FileCon = ''

    if len(FileConList) > 0:
        for item in FileConList:
            FileCon = FileCon + "[" + SU_MO_TimeReturn2() + "] : " + item + '\n'

    # 날짜 디렉토리를 만든다.
    strDate = SU_MO_TimeReturn(3)
    Source = Source + strDate + SplitDef

    # 파일명을 시간단위로 설정(6)
    Filename = ''
    F = ''
    try:
        if os.path.isdir(Source):
            fileList = os.listdir(Source)
            if len(fileList) > 0:

                # 같은 폴더내의 가장 최근 파일 조사(여기가 핵심)
                fileList = [x.replace(".log", "") for x in fileList]
                Filename = Source + str(max(fileList)) + ".log"

                # 파라미터 reSize 사이즈가 넘어가면 새로 파일 만든다.
                if os.path.getsize(Filename) > reSize:
                    Filename = Source + SU_MO_TimeReturn(6) + ".log"
                    F = open(Filename, 'w')
                    F.write(FileCon)
                else:
                    F = open(Filename, 'a')
                    F.write(FileCon)
            else:
                Filename = Source + SU_MO_TimeReturn(6) + ".log"
                F = open(Filename, 'w')
                F.write(FileCon)
        else:
            os.mkdir(Source)
            Filename = Source + SU_MO_TimeReturn(6) + ".log"
            F = open(Filename, 'w')
            F.write(FileCon)
        F.close()
    except:
        pass
    finally:
        F.close()