import sys
import os
import glob
import shutil
import paramiko
from stat import S_ISDIR
import platform
import datetime
from tika import parser
import filecmp
import zipfile
import PY_PKG.SU_DirFile_MO as psd
import PY_PKG.SU_Hwp_Read_MO as phwp
import io
import re
import openpyxl as op
import csv

############################################################# 로그 파일에 기록
# 로그라든지 어떠한 내용을 정해진 파일에 적기
# 특정 폴더에 금일날짜로 만들어진다.
# Source : 저장할 디렉토리명
# FileCon : 파일에 적을 내용
# Plt 원격 프랫폼 1이면 윈도우, 2이면 유닉스
# Index : 오늘날짜에 만들어지는 인덱스 번호, 일정한 라인수가 되면 index를 증가해서 다른 파일에 적는다. 보통 1부터 시작
def SU_MO_FileWrite(Source, FileCon, Plt, Index):
    dt_now = datetime.datetime.now()
    strDate = str(dt_now.date()).replace('-', '')
    Filename = strDate + "_" + str(Index) + ".log"

    fexist = psd.SU_MO_FindFilename(Source, Filename)

    F = ""
    Filename = Source + Filename

    try:
        if fexist:
            F = open(Filename, 'r')
            strList = F.readlines()
            strList = list(strList)
            strCount = len(strList)

            if strCount > 100:
                Index = Index + 1
                SU_MO_FileWrite(Source, FileCon, Plt, Index)
            else:
                F = open(Filename, 'a')
                F.write(FileCon)
        else:
            F = open(Filename, 'w')
            F.write(FileCon)
    except:
        pass
    finally:
        F.close()


############################################################# 로그 파일에 기록
# SU_MO_FileWrite 업그레이드 버젼으로 모니터링 폴더아래 날짜 폴더를 만들고 지정한 사이즈를 넣으면
# 로그 파일을 초까지 해서 만든다. 같은 날짜에 여러개의 파일이 존재할 경우 가장 최근 파일의 사이즈를 조사해서 만들지
# 추가할지를 결정한다.

# Source   : 저장할 디렉토리명
# FileCon  : 파일에 적을 내용
# SplitDef : os에 맞는 디렉토리 구분자.
# reSize   : 적당한 파일사이즈. 가장 최신 파일이 이 사이즈를 넘으면 파일을 새로 만든다.(로그 찾기 쉽게 하기 위해)
def SU_MO_FileWrite2(Source, FileCon, SplitDef, reSize):
    # 로그 내용에 시분초를 더한다.
    FileCon = "[" + psd.SU_MO_TimeReturn(6) + "] : " + FileCon

    # 날짜 디렉토리를 만든다.
    strDate = psd.SU_MO_TimeReturn(3)
    Source = Source + strDate + SplitDef

    F = ''
    # 파일명을 시간단위로 설정(6)
    Filename = ''
    try:
        if os.path.isdir(Source):
            fileList = os.listdir(Source)
            if len(fileList) > 0:

                # 같은 폴더내의 가장 최근 파일 조사(여기가 핵심)
                fileList = [x.replace(".log", "") for x in fileList]
                Filename = Source + str(max(fileList)) + ".log"

                # 파라미터 reSize 사이즈가 넘어가면 새로 파일 만든다.
                if os.path.getsize(Filename) > reSize:
                    Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
                    F = open(Filename, 'w')
                    F.write(FileCon)
                else:
                    F = open(Filename, 'a')
                    F.write(FileCon)
            else:
                Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
                F = open(Filename, 'w')
                F.write(FileCon)
        else:
            os.mkdir(Source)
            Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
            F = open(Filename, 'w')
            F.write(FileCon)
    except:
        pass
    finally:
        F.close()


############################################################# 로그 파일에 기록
# 데이터베이스 한번에 한번씩 파일에 적는 다는 것은 성능상의 문제가 있음. 적을 내용을 리스트에 담아서 일정수가 차면
# 한번에 로그파일에 적은 것을 함. 이렇게 하면 해당 파일 사이즈를 조금은 넘길 수 있다.
# Source       : 저장할 디렉토리명
# FileConList  : 파일에 적을 내용 리스트
# SplitDef     : os에 맞는 디렉토리 구분자.
# reSize       : 적당한 파일사이즈. 가장 최신 파일이 이 사이즈를 넘으면 파일을 새로 만든다.(로그 찾기 쉽게 하기 위해)
def SU_MO_FileWrite3(Source, FileConList, SplitDef, reSize):
    # 로그 파일에 적을 내용
    FileCon = ''

    if len(FileConList) > 0:
        for item in FileConList:
            FileCon = FileCon + "[" + psd.SU_MO_TimeReturn2() + "] : " + item + '\n'

    # 날짜 디렉토리를 만든다.
    strDate = psd.SU_MO_TimeReturn(3)
    Source = Source + strDate + SplitDef

    F = ''
    Filename = ''

    try:
        if os.path.isdir(Source):
            fileList = os.listdir(Source)
            if len(fileList) > 0:

                # 같은 폴더내의 가장 최근 파일 조사(여기가 핵심)
                fileList = [x.replace(".log", "") for x in fileList]
                Filename = Source + str(max(fileList)) + ".log"

                # 파라미터 reSize 사이즈가 넘어가면 새로 파일 만든다.
                if os.path.getsize(Filename) > reSize:
                    Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
                    F = open(Filename, 'w')
                    F.write(FileCon)
                else:
                    F = open(Filename, 'a')
                    F.write(FileCon)
            else:
                Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
                F = open(Filename, 'w')
                F.write(FileCon)
        else:
            os.mkdir(Source)
            Filename = Source + psd.SU_MO_TimeReturn(6) + ".log"
            F = open(Filename, 'w')
            F.write(FileCon)
    except:
        pass
    finally:
        F.close()


############################################################# 추출된 파일내용을 텍스트 파일로 변환
# targetfolder : 저장할 폴더
# filename     : 저장할 파일명
# filecon      : 파일내용
# gubun        : 폴더명 구분자 보통 "\\"
def SU_MO_FileWrite4(targetfolder, filename, filecon, gubun):
    strDate = datetime.datetime.now().strftime('%Y-%m-%d')
    strDate = strDate.replace('-', '')

    F = ''
    # 날짜 디렉토리를 만든다.
    tfolder = targetfolder + strDate
    try:
        if not os.path.exists(tfolder):
            os.makedirs(tfolder)

        filename = tfolder + gubun + filename
        F = open(filename, 'w', encoding='utf-8')
        F.write(filecon)
    except OSError:
        print("make foler error")
    finally:
        F.close()


############################################################# 텍스트 파일에 문자열 쓰기
# strText       : 원본 텍스트. 그냥 문자열
# destTextFile  : 원본 텍스트 파일을 기록할 텍스트 파일
# 즉 strText 문자열을 destTextFile에 기록 함
def SU_MO_StrToText(strText, destTextFile):
    F = ''
    try:
        # 파일이 존재하면 삭제함
        if os.path.isfile(destTextFile):
            os.remove(destTextFile)

        F = open(destTextFile, 'w', encoding='UTF-8')
        F.write(strText)
    except:
        pass
    finally:
        F.close()


############################################################# tika 모듈을 이용해서 pdf 파일읽기
# pdfdir : pdf 파일 디렉토리
def SU_MO_PdfRead_Tika(pdfdir):
    try:
        for file in glob.iglob(pdfdir + "**/*", recursive=True):

            if not os.path.isdir(file):
                filename = os.path.splitext(file)
                ext = filename[1]  # 확장자

                if ext.upper() == ".PDF":
                    raw_pdf = parser.from_file(file)
                    strContent = raw_pdf['content']
                    print(strContent)
    except:
        pass


#############################################################  pdf파일내 특정 키워드 찾기
# Target : 읽을 PDF 파일 위치(디렉토리)
# listNO : 독소조항
# listOk : 희망조항
# userID : 사용자 아이디, 이것은 사용자마다 독소조항, 희망사항이 다르기 때문
def SU_MO_PdfRead_Tika_NoOk(Target, listNo, listOk, userID):
    try:
        for file in glob.iglob(Target + "**/*", recursive=True):

            if not os.path.isdir(file):
                orgfilename = os.path.basename(file)
                filename = os.path.splitext(file)
                ext = filename[1]  # 확장자

                if ext.upper() == ".PDF":
                    raw_pdf = parser.from_file(file)
                    strContent = raw_pdf['content']

                    if len(strContent) > 0:
                        for noitem in listNo:
                            if noitem in strContent:
                                print(orgfilename + " 독소조항 : " + noitem)

                        for okitem in listOk:
                            if okitem in strContent:
                                print(orgfilename + " 희망조항 : " + okitem)
                    else:
                        print("Content No")
    except:
        pass


############################################################# 한글 파일내 특정키워드 찾기
# Target : 읽을 한글 파일 위치(디렉토리)
# listNO : 독소조항
# listOk : 희망조항
# userID : 사용자 아이디, 이것은 사용자마다 독소조항, 희망사항이 다르기 때문
def SU_MO_HwpRead_NoOk(Target, listNo, listOk, userID):
    try:
        for file in glob.iglob(Target + "**/*", recursive=True):

            if os.path.isfile(file):
                Ext = str(os.path.splitext(file)[1])
                Ext = Ext[1:]

                if Ext.upper() == "HWP":
                    filename = os.path.basename(file)
                    dirname = file.replace(filename, "")
                    hwpReader = phwp.HwpReader(dirname, filename)
                    hwpReader = hwpReader.bodyStream()

                    for keyItem in hwpReader.keys():
                        strVList = str(hwpReader.get(keyItem))
                        strVList = strVList.replace('\n', '')

                        if len(strVList) > 0:

                            for noitem in listNo:
                                if noitem in strVList:
                                    print(filename + " 독소조항 : " + noitem)

                            for okitem in listOk:
                                if okitem in strVList:
                                    print(filename + " 희망조항 : " + okitem)
                else:
                    print("no")
    except:
        pass


########################################################  HWP 내용 추출
# 단지 한글 파일을 읽어서 본문 내용을 리턴(hwp)
# Targetfile : 파일명
def SU_MO_HwpRead_Extract(Targetfile):
    try:
        filename = os.path.basename(Targetfile)
        dirname = Targetfile.replace(filename, "")

        hwpReader = phwp.HwpReader(dirname, filename)
        hwpReader = hwpReader.bodyStream()

        strVList = ""

        for keyItem in hwpReader.keys():
            strbody = str(hwpReader.get(keyItem))
            strbody = strbody.replace('\n', '')
            if len(strbody) > 0:
                strVList = strVList + strbody

        return strVList
    except:
        print("hwp read err")
        pass

    return ""


########################################################  HWPX 내용 추출
'''
# 한글파일 : hwpx를 위한 문제 해결
# 문제    : 파일 포맷이 다른 경우로 일반적인 방법으로 읽어올 수 없음
# 해결 방법
  1. 먼저 한글 파일 확장자를 .zip로 변경
  2. 이 파일을 압축 해제
     : 해제하면 이런 구조가 됨. (1) Contents-(section0.xml, 기타파일) (2) META-INF (3) Preview
     : 우리가 필요한 것 : (1) 딕렉토리 아래 section0.xml 파일
  3. 이 파일을 읽어서 <hp:t> </hp:t> 이 테크내용만 불러옴
  4. 이 파일의 내용만 리턴

# 파라미터
  1. SourceFolder : 마지막에 '/' 까지
  2. sfile : hwpx 파일명
'''
def SU_MO_HwpRead_Hwpx(SourceFolder, sfile):
    hwpxstr = ""
    flist = []
    try:
        com = re.compile("<hp:t>.+?</hp:t>", re.MULTILINE)
        com2 = re.compile(r"Contents/section.+")  # 한글은 이런 xml 파일명으로 변경됨. 하나 이상일것 같아서 이렇게 함

        # 풀네임
        fullfilename = SourceFolder + sfile

        # 1. zip으로 파일명 변경
        filen = str(os.path.splitext(sfile)[0])
        file_ext = str(os.path.splitext(sfile)[1])
        nfile = str(sfile).replace(file_ext, ".zip")
        nfilezip = SourceFolder + nfile
        os.rename(fullfilename, nfilezip)

        # 2. 압축해제하고 section0.xml 파일만 찾음(여기에 hwpx 내용이 존재함)
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
    except:
        hwpxstr = ''
        pass
    return hwpxstr


########################################################  PDF 파일 읽기
# Targetfile : pdf 파일명(경로 포함)
def SU_MO_PdfRead_Extract(Targetfile):
    try:
        raw_pdf = parser.from_file(Targetfile)
        strContent = raw_pdf['content']

        if len(strContent) > 0:
            return strContent
        else:
            return ""
    except:
        pass

    return ""


############################################################# 텍스트 파일을 열어서 텍스트를 문자열로 리턴(리스트형)
# sourceFile       : 읽어올 텍스트 원본 파일
# 유의사항 : 만약에 \n 없이 통으로된 문자열일 경우 한 라인이 텍스파일 자체이다.
# txt 파일을 만들때 utf-8로 저장했으면 반드시 utf-8로 읽어와야 한다. 그렇치 않으면 오류
# hwp,hwpx,pdf 등 텍스트 읽어서 저장시 utf-8로 저장함
def SU_MO_TextFileToStr(sourceFile):
    f = ''
    reList = []
    try:
        f = open(sourceFile, 'r', encoding='UTF-8')
        lines = f.readlines()
        for line in lines:      # '\n'를 제거하기 위해
            line = line.strip()
            reList.append(line)
        return reList
    except:
        pass
    finally:
        f.close()
    return []

############################################################# 텍스트 파일을 열어서 텍스트를 문자열로 리턴
# sourceFile       : 읽어올 텍스트 원본 파일
# txt 파일을 만들때 utf-8로 저장했으면 반드시 utf-8로 읽어와야 한다. 그렇치 않으면 오류
# hwp,hwpx,pdf 등 텍스트 읽어서 저장시 utf-8로 저장함
def SU_MO_TextFileToStr2(sourceFile):
    f = ''
    try:
        f = open(sourceFile, 'r', encoding='UTF-8')
        strfile = f.read()
        return strfile
    except:
        pass
    finally:
        f.close()
    return ""


############################################################# 텍스트 파일을 열어서 텍스트를 "."으로 분리하여 리스트 형식으로 반환
# sourceFile       : 읽어올 텍스트 원본 파일
# txt 파일을 만들때 utf-8로 저장했으면 반드시 utf-8로 읽어와야 한다. 그렇치 않으면 오류
# hwp,hwpx,pdf 등 텍스트 읽어서 저장시 utf-8로 저장함
# SU_MO_TextFileToStr와 다른 점은 텍스트 파일의 문자열 자체가 하나의 문장이기 때문에 라인단위로 읽는 것보다 마침표"." 분리한다.
# 이렇게 분리하는 이유는 네이버 맞춤범 검사할때 글자수 제한이 있기 때문
def SU_MO_TextFileToStr3(sourceFile):
    f = ''
    reList = []
    try:
        f = open(sourceFile, 'r', encoding='UTF-8')
        strfile = f.read()
        reList = strfile.split(".")
        return reList
    except:
        pass
    finally:
        f.close()
    return []


############################################################# 엑셆 파일에서 텍스트만 추출해서 반환
# sourceFile : 엑셀파일
def SU_MO_ExcelRead_Extract(sourceFile):
    try:
        wb = op.load_workbook(sourceFile)
        wlist = wb.sheetnames
        rowListValue = []

        for name in wlist:
            ws = wb[name]
            for row in ws.rows:
                for col in row:
                    strvalue = col.value
                    if strvalue is not None:
                    # if len(strvalue) > 0:
                        rowListValue.append(str(strvalue))

        return ' '.join(rowListValue)
    except:
        return ''
