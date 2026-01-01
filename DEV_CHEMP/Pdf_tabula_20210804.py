# 보통 법정서식 같은 경우 표형태가 대부분인데 표를 읽어 올때 사용
# 대신 영역을 지정해야 한느데 법정서식이라도 기관마다 약간씩 다름
import tabula
import platform
import os
import shutil
import schedule
import time
import cx_Oracle
import paramiko
from stat import S_ISDIR
import datetime
import glob

# # 오라클 연결
# connection = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/XE')
# cursor = connection.cursor()


# 기술원 운영서버
os.putenv('NLS_LANG', '.UTF8')
connection = cx_Oracle.connect('chemp/chemp!1299@10.10.20.10:1521/chemp')
cursor = connection.cursor()


# 윈도우 또는 리눅스 플랫폼 검토
strPlatform = platform.system()
strFirst = os.getcwd()
strSplitDef = ''

if strPlatform == 'Windows':
    strOrg = strFirst + '\\IDT\\PDF\\'              # 윈도우에서 pdf 원본 파일이 저장되는 곳
    strExc = strFirst + '\\IDT\\'
    strExt = 'PDF'                                  # 확장자(PDF만 가능)
    strRead = strFirst + '\\IDT\\PDF_READ\\'        # PDF 성공적으로 읽은 파일 이동
    strError = strFirst + '\\IDT\\PDF_ERROR\\'      # PDF 오류 항목
    strSplitDef = '\\'
else:
    strOrg = strFirst + '/IDT/PDF/'
    strExc = strFirst + '/IDT/'
    strExt = 'PDF'
    strRead = strFirst + '/IDT/PDF_READ/'           # 리눅스에서는 여기가 최종 결과물이 저장되는 곳
    strError = strFirst + '/IDT/PDF_ERROR/'
    strSplitDef = '/'

# 운영서버 연결
Remote_Server = "210.220.13.165"
Remote_UserName = "chkusr"
Remote_UserPwd = "Qwer!234"
Remote_port = 2022
Remote_BaseDir = "/home/chkusr/ESB_AGENT1.5/FILE/receivework/"
Remote_ErrorDir = "/home/chkusr/ESB_AGENT1.5/FILE/receivework_BackUp/ALL_ERROR/"
Remote_BackDir = "/home/chkusr/ESB_AGENT1.5/FILE/receivework_BackUp/ALL_BACKUP/"
Remote_PdfResult = '/CPMS/WAS/reg/down/pdf/'


# 개발서버 연결
# Remote_Server = "127.0.0.1"
# Remote_UserName = "jung100hwa"
# Remote_UserPwd = "!!hgl1651ok"
# Remote_port = 22
# Remote_BaseDir = "/home/jung100hwa/PLangVim/IDT_Sample/"                # 시험기관 연계파일 원본
# Remote_PdfResult = '/home/jung100hwa/PLangVim/IDT/PDF/'            # 최종 결과물인 pdf가 싸이는 곳


# 기관 코드, 기관마다 유일한 코드가 있음, 이미 정의되어 있음
G_Govmen = ['9990304','9990043','9990296','9990040','9990279','9990053','9990044']

# 한국환경산업기술원
# 1. 2021.07.29 업데이트
keiti_xy = 0
keiti_001 = [336+keiti_xy, 112, 439+keiti_xy, 302]
keiti_002 = [205+keiti_xy, 302, 439+keiti_xy, 540]
keiti_003 = [498+keiti_xy, 83, 592+keiti_xy, 226]

# 한국건설생활환경시험연구원
# 1. 2021.07.29 업데이트
kcl_xy2 = 20
kcl_001 = [279+kcl_xy2, 83, 361+kcl_xy2, 307]
kcl_002 = [251+kcl_xy2, 307, 361+kcl_xy2, 540]
kcl_003 = [430+kcl_xy2, 52, 513+kcl_xy2, 244]


# kotiti 시험연구원
# 1. 2021.05.15 업데이트
kotiti_xy = 20
kotiti_001 = [290+kotiti_xy, 114, 400+kotiti_xy, 306]
kotiti_002 = [262+kotiti_xy, 306, 400+kotiti_xy, 538]
kotiti_003 = [450+kotiti_xy, 61, 526+kotiti_xy, 245]


# 한국의류시험연구원
# 1. 2021.07.29 업데이트
citi_xy = 20
citi_001 = [306+citi_xy, 87, 400+citi_xy, 298]
citi_002 = [280+citi_xy, 297, 400+citi_xy, 540]
citi_003 = [456+citi_xy, 56, 557+citi_xy, 195]


# 한국기제전기전자시험연구원
# 1. 2021.07.29 업데이트
ktc_xy = 10
ktc_001 = [306+ktc_xy, 80, 388+ktc_xy, 297]
ktc_002 = [280+ktc_xy, 297, 388+ktc_xy, 541]
ktc_003 = [434+ktc_xy, 55, 488+ktc_xy, 249]


# 한국화학융합시험연구원
# 1. 2021.07.29 업데이트
ktr_xy = 20
ktr_001 = [290+ktr_xy, 68, 371+ktr_xy, 310]
ktr_002 = [264+ktr_xy, 310, 371+ktr_xy, 554]
ktr_003 = [434+ktr_xy, 41, 520+ktr_xy, 187]

# FITI 시험연구원
# 1. 2021.08.06 업데이트
FITI_xy = 0
fiti_001 = [318+FITI_xy, 97, 402+FITI_xy, 298]
fiti_002 = [292+FITI_xy, 310, 402+FITI_xy, 541]
fiti_003 = [462+FITI_xy, 56, 534+FITI_xy, 283]

# 신고대상 코드 값 정의
str001 = {}
str002 = {}
str003 = {}
str004 = {}
str005 = {}
str006 = {}

# str001 분류는 확인결과서에 존재하지 않는다. 품목에 의해서 자동 설정

# str002 품목
cursor.execute("""SELECT CODE, CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
(SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC007' AND USE_AT = 'Y') AND USE_AT = 'Y'""")
rval = cursor.fetchall()
for item in rval:
    str002[item[0]] = item[1]


# str003 용도
cursor.execute("""SELECT CODE,CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN (
SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN (
SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC007' AND USE_AT = 'Y') AND USE_AT = 'Y') AND USE_AT = 'Y'""")
rval = cursor.fetchall()
for item in rval:
    str003[item[0]] = item[1]


# str004 상세용도
cursor.execute("""SELECT CODE, CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN (
SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN (
SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN (
SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC007' AND USE_AT = 'Y') AND USE_AT = 'Y') AND USE_AT = 'Y') AND USE_AT = 'Y'""")
rval = cursor.fetchall()
for item in rval:
    str004[item[0]] = item[1]


# str005 제형(분사형 또는 비분사형)
cursor.execute("""SELECT CODE, CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC005'""")
rval = cursor.fetchall()
for item in rval:
    str005[item[0]] = item[1]

# str006 상세제형
cursor.execute("""SELECT CODE, CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
(SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC005')""")
rval = cursor.fetchall()
for item in rval:
    str006[item[0]] = item[1]


# 여기는 확인 결과서의 제품명, 제형 등 왼쪽 부분을 처리한다.
def listSearch(listStr, keyNum, strGovcode, strGovNM):
    if keyNum == '01':
        strProduct = ''         # 제품명
        strJe = ''              # 제형
        strJe2 = ''             # 실제 코드에 존재하는 제형 넣기
        strDetJe = ''           # 상세제형
        strDetJe2 = ''          # 실제 코드에 존해하는 상세제형 넣기
        strNa = ''              # 제조국
        strIO = ''              # 수입인지 제조인지
        itemNo = 0              # 다음값을 위해 존재한다.

        # 제품명 구하기
        for index, name in enumerate(listStr):
            if name == '제형':
                itemNo = index
                break
            strProduct = strProduct + name

        if strProduct:
            strProduct = strProduct.replace("'", "' || chr(39) || '")

        # 제형 구하기
        for index, name in enumerate(listStr):
            if name == '제조국명(수입의 경우)' or name == '제조국명':  # 기술원만
                itemNo = index
                break
            if index > itemNo:
                strJe = strJe + name

        # 제조국 구하기
        for index, name in enumerate(listStr):
            if index > itemNo:
                strNa = strNa + name
                break

        # 제조인지 수입인지, 제조국명이 존재하는지로 판단
        if strNa:
            if strNa.replace(' ', '') == '-' or len(strNa) == 0:
                strIO = '제조'
            else:
                strIO = '수입'
        else:
            strIO = '제조'


        # 실제 DB 상의 제형 찾기. 기관마다 용어도 그렇고 정형화 되지 않음
        # 제형과 상세제형이 구분되어 들어오지 않는다. 즉 연소형 상세제형만 들어오는 경우가 많음
        # 즉 아래에서는 제형이 들어올때 일단  담아둔다.
        for key, val in str005.items():
            if val.replace(' ','') in strJe.replace(' ',''):
                strJe2 = key
                break


        # 상세 제형 찾기. 상세제형만 있는 경우 상위의 제형을 찾는다.
        for key, val in str006.items():
            if val.replace(' ','') in strJe.replace(' ',''):
                strDetJe2 = key
                if len(strJe2) == 0:
                    cursor.execute("""SELECT CODE_ID FROM COMTCCMMNDETAILCODE WHERE CODE='%s'""" %(strDetJe2))
                    rval = cursor.fetchone()
                    if rval:     # 상세제형만 있는 경우 상세제형에 해당되는 제형을 찾는다.
                        strJe2 = rval[0]
                    break


        # 데이터 입력하기
        if len(strGovcode) > 0:
            cursor.execute("""UPDATE TN_NLC_INSPCTSCRE_PUB SET STR1 = '%s', STR2='%s', STR3='%s', STR4='%s', STR5='%s' 
            WHERE ISSU_MSN='%s'""" % (strProduct, strJe2, strDetJe2, strNa, strIO, strGovcode))
            connection.commit()


    # 품목, 용도 등 확인결과서의 오른쪽에 있는 것 구하기
    if keyNum == '02':
        strGubun = ''                       # 분류
        strPun = ''                         # 품목
        strPun2 = ''                        # 실제 품목
        strYun = ''                         # 용도
        strYun2 = ''                        # 실제 DB에 있는 용도
        strDeYun = ''                       # 상세용도
        strDeYun2 = ''                      # 실제 DB에 있는 상세용도
        strJun = ''                         # 중량
        strCompany = ''                     # 제조사
        itemNo = 0
        
        # 품목
        for index, name in enumerate(listStr):
            if name == '용도':
                itemNo = index
                break
            strPun = strPun + name

        # 용도
        for index, name in enumerate(listStr):
            if name == '중량·용량·매수' or name == '중량ᆞ용량ᆞ매수' or name == '중량ᆞ용량ᆞ매수ᆞ크기' or name == '중량 · 용량 · 매수':
                itemNo = index
                break
            if index > itemNo:
                strYun = strYun + name

        # 중량
        for index, name in enumerate(listStr):
            if name == '제조회사명(수입의 경우)' or name == '제조회사명':
                itemNo = index
                break
            if index > itemNo:
                strJun = strJun + name

        # 제조사
        for index, name in enumerate(listStr):
            if index > itemNo:
                strCompany = strCompany + name

        # 가끔 아래 확인결과에서 확인결과가 찍히는 경우가 있음 이부분 삭제
        if len(strCompany) > 0:
            strCompany = strCompany.replace('결과', '')



        # 실제 품목과 분류 구하기(품목에 따라 분류는 이미 정해짐)
        for key, val in str002.items():
            if val.replace(' ', '') in strPun.replace(' ', ''):
                strPun2 = key

                # 분류코드 구하기
                if len(strPun2) > 0:
                    cursor.execute("""SELECT CODE_ID FROM COMTCCMMNDETAILCODE WHERE CODE='%s'""" %(strPun2))
                    rval = cursor.fetchone()
                    if rval:
                        strGubun = rval[0]
                    else:
                        strGubun = ''
                break


        # 실제 용도, 용도는 품목에 따라 용도가 같을 수 있다. 즉 세정제의 일반용, 제거제의 일반용
        for key, val in str003.items():
            if val.replace(' ', '') in strYun.replace(' ', ''):
                 # 용도의 상위코드인 품목 코드를 구해서 실제 품목코드와 일치하는 본다.
                cursor.execute("""SELECT CODE_ID FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
                (SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
                (SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC007' AND USE_AT = 'Y') AND USE_AT = 'Y') AND USE_AT = 'Y' AND CODE ='%s'""" %(key))

                rval = cursor.fetchone()
                
                if rval:
                    if rval[0] == strPun2:
                        strYun2 = key
                        break       # break의 위치는 여기가 맞다. 동일 품목에 용도가 같을 수 있으니까
                else:
                    strYun2 = ''


        # 실제 상세용도, 여기도 마찬가지이다. 하나의 용도에 상세용도가 동일할 수 있다. 즉 일반용-욕실용, 악기용-일반용
        for key, val in str004.items():
            if val.replace(' ', '') in strYun.replace(' ', ''):
                cursor.execute("""SELECT CODE_ID FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
                (SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
                (SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID IN 
                (SELECT CODE FROM COMTCCMMNDETAILCODE WHERE CODE_ID='NLC007' AND USE_AT = 'Y') 
                AND USE_AT = 'Y') AND USE_AT = 'Y') AND USE_AT = 'Y' AND CODE = '%s'""" %(key))

                rval = cursor.fetchone()
                if rval:
                    if rval[0] == strYun2:
                        strDeYun2 = key
                        break
                else:
                    strDeYun2 = ''


        if len(strGovcode) > 0:
            cursor.execute("""UPDATE TN_NLC_INSPCTSCRE_PUB SET STR11='%s', STR6='%s', STR7='%s', STR8='%s', STR9='%s', STR10='%s' 
                WHERE ISSU_MSN='%s'""" % (strGubun, strPun2, strYun2, strDeYun2, strJun, strCompany, strGovcode))
            connection.commit()


# 확인결과서 어린이 보호포장 등
def listSearch2(df, strGovcode):
    listStr001_1 = df[df.columns[0]].dropna(how='all')
    listStr002_1 = df[df.columns[1]].dropna(how='all')

    # 확인결과서의 검사구분 열을 담든다.
    listStr001 = []
    strlist001_01 = ''
    strlist001_02 = ''
    strlist001_03 = ''
    
    # 확인결과서의 판정을 담는다.
    listStr002 = []
    strlist002_01 = ''
    strlist002_02 = ''
    strlist002_03 = ''

    for item in listStr001_1:
        listStr001.append(item.replace(' ', ''))

    for item in listStr002_1:
        listStr002.append(item.replace(' ', ''))

    # 검사구분에 새로운 행에 확인결과가 있음 그래서 실제 3개행이 6개행으로 됨.
    # 이것을 지워서 3개 행으로 만듬
    while '확인결과' in listStr001:
        listStr001.remove('확인결과')

    for item in listStr001:
        if '화학' in item:
            strlist001_01 = '화학물질'
            if listStr002[1]:
                strlist002_01 = listStr002[0]
        if '용기' in item:  # 여기는 또 틀리네네
            strlist001_02 = '용기·포장및중량'
            if listStr002[1]:
                strlist002_02 = listStr002[1]
        if '어린이' in item:
            strlist001_03 = '어린이보호포장'
            if listStr002[1]:
                strlist002_03 = listStr002[2]

    # 이 기관은 좋합판정이 이미지 인듯 해서 이렇게 구함
    strtotalpan = '적합'
    if strlist002_01:
        if '부적합' in strlist002_01:
            strtotalpan = '부적합'
    if strlist002_02:
        if '부적합' in strlist002_02:
            strtotalpan = '부적합'
    if strlist002_03:
        if '부적합' in strlist002_03:
            strtotalpan = '부적합'

    cursor.execute("""UPDATE TN_NLC_INSPCTSCRE_PUB SET STR12 = '%s', STR13='%s', STR14='%s', STR15='%s', STR16='%s', 
                                                       STR17='%s', STR18='%s' WHERE ISSU_MSN='%s'""" % (
    strtotalpan, strlist001_01, strlist002_01, strlist001_02, strlist002_02, strlist001_03, strlist002_03, strGovcode))
    connection.commit()



strGov = ''
strRoot = ''
G_strDFname = ''

def dirsearch(strOrgdir, strExt):
    try:
        dirname = os.listdir(strOrgdir)  # 리스트 형식으로 리턴

        # 파일 또는 폴더가 하나라도 있으면
        if len(dirname) >= 1:
            for fname in dirname:
                full_fname = os.path.join(strOrgdir, fname)
                G_strDFname = full_fname

                # 만약에 디렉토리이면 자기참조
                if os.path.isdir(full_fname):

                    # 디렉토리 안에 파일이 존재하면
                    for root, dirs, files in os.walk(full_fname):
                        if files:
                            if len(files) == 1 or len(files) == 0:
                                shutil.rmtree(G_strDFname)
                                break
                            else:
                                dirsearch(full_fname, strExt)
                                shutil.rmtree(G_strDFname)
                        else:
                            shutil.rmtree(root)
                else:
                    if len(full_fname) > 0:

                        # 확장자를 검색해서 PDF 이면 수행
                        try:
                            if (os.path.splitext((full_fname))[-1]).upper() == "." + strExt:

                                # 시험성적서 파일만 읽는다. 아닌 파일을 삭제
                                if full_fname[-25:-18] in G_Govmen:

                                    # 이슈넘버
                                    strGov = os.path.dirname(full_fname)
                                    strGov = strGov[-23:]

                                    # 시험성적서 발행 기관 조회
                                    cursor.execute("""SELECT EXPR_INSPCT_OG_NM FROM TN_NLC_INSPCTSCRE_PUB WHERE ISSU_MSN='%s'""" % (strGov))
                                    strGovNM = cursor.fetchone()

                                    # 법정서식인데 기관마다 다름.
                                    GKTR_001 = []   # 제형 등
                                    GKTR_002 = []   # 품목, 용도 등
                                    GKTR_003 = []   # 적합판정 등

                                    if strGovNM:
                                        if strGovNM[0] == '한국화학융합시험연구원':
                                            GKTR_001 = ktr_001
                                            GKTR_002 = ktr_002
                                            GKTR_003 = ktr_003

                                        if strGovNM[0] == '한국기계전기전자시험연구원':
                                            GKTR_001 = ktc_001
                                            GKTR_002 = ktc_002
                                            GKTR_003 = ktc_003

                                        if strGovNM[0] == '한국의류시험연구원':
                                            GKTR_001 = citi_001
                                            GKTR_002 = citi_002
                                            GKTR_003 = citi_003

                                        if strGovNM[0] == 'KOTITI시험연구원':
                                            GKTR_001 = kotiti_001
                                            GKTR_002 = kotiti_002
                                            GKTR_003 = kotiti_003

                                        if strGovNM[0] == '한국건설생활환경시험연구원':
                                            GKTR_001 = kcl_001
                                            GKTR_002 = kcl_002
                                            GKTR_003 = kcl_003

                                        if strGovNM[0] == '한국환경산업기술원':
                                            GKTR_001 = keiti_001
                                            GKTR_002 = keiti_002
                                            GKTR_003 = keiti_003

                                        if strGovNM[0] == 'FITI 시험연구원':
                                            GKTR_001 = fiti_001
                                            GKTR_002 = fiti_002
                                            GKTR_003 = fiti_003

                                    if strGovNM:

                                        # 좌측의 제품명, 제형, 상세제형, 제조국명을 구하기
                                        strContent = tabula.read_pdf(full_fname, pages=1, area=GKTR_001,
                                                                     multiple_tables=False, stream=True)
                                        df = strContent[0]
                                        listStr001 = df[df.columns[0]]
                                        listSearch(listStr001, '01', strGov, strGovNM[0])

                                        # 우측의 품목, 용도, 중량, 제조사 구하기
                                        strContent = tabula.read_pdf(full_fname, pages=1, area=GKTR_002,
                                                                     multiple_tables=False, stream=True)
                                        df = strContent[0]
                                        listStr001 = df[df.columns[0]]
                                        listSearch(listStr001, '02', strGov, strGovNM[0])

                                        # 아래의 확인결과 구하기
                                        strContent = tabula.read_pdf(full_fname, pages=1, area=GKTR_003,
                                                                     multiple_tables=False, stream=True)
                                        df = strContent[0]
                                        listSearch2(df, strGov)
                                        print(full_fname + "===>ok")

                                    strSplitFilename = os.path.basename(full_fname)
                                    strCreateRead = strRead + strSplitDef + strSplitFilename
                                    shutil.copy(full_fname, strCreateRead)
                                else:
                                    strSplitFilenameError = os.path.basename(full_fname)
                                    strCreateRead = strError + strSplitDef + strSplitFilenameError
                                    shutil.copy(full_fname, strCreateRead)
                        except:
                            strSplitFilenameError = os.path.basename(full_fname)
                            strCreateRead = strError + strSplitDef + strSplitFilenameError
                            shutil.copy(full_fname, strCreateRead)
                            pass
        else:
            print("==========> not file exist")
    except PermissionError:
        pass

def directorydrop(strOrg):
    try:
        dirname = os.listdir(strOrg)  # 리스트 형식으로 리턴
       
        for fname in dirname:
            full_fname = os.path.join(strOrg, fname)

            # 만약에 디렉토리이면 자기참조
            if os.path.isdir(full_fname):
                shutil.rmtree(full_fname)
    except:
        print("==========> file error")
        pass

# 스케줄러에 등록(10초에 한번씩)
# schedule.every(30).seconds.do(dirsearch,strOrg, strExt)
# # schedule.every().day.at("4:30").do(dirsearch,strOrg, strExt)
#
# if __name__ == "__main__":
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# ssh 원격파일 열기
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(Remote_Server, username=Remote_UserName, password=Remote_UserPwd, port=Remote_port)
sftp = ssh.open_sftp()

# ######################################################## 년월일시간분값을 리턴
def Get_ID_Make():
    sYear = str(datetime.datetime.now().year)
    sMon = str(datetime.datetime.now().month)
    if len(sMon) == 1:
        sMon = "0" + sMon

    sDay = str(datetime.datetime.now().day)
    if len(sDay) == 1:
        sDay = "0" + sDay

    sHour = str(datetime.datetime.now().hour)
    if len(sHour) == 1:
        sHour = "0" + sHour

    sMin = str(datetime.datetime.now().minute)
    if len(sMin) == 1:
        sMin = "0" + sMin

    sss = sYear + sMon + sDay + sHour + sMin
    return sss

# ######################################################## 1. 원격 파일을 로컬상으로 다운로드 한다.
def Remote_FileDown(RemoteDir, LocalDir):
    for remotedir in sftp.listdir_attr(RemoteDir):
        l_dir = LocalDir+remotedir.filename
        r_dir = RemoteDir+remotedir.filename

        if S_ISDIR(remotedir.st_mode):   
            if not os.path.exists(l_dir):
                os.makedirs(l_dir)
            Remote_FileDown(r_dir+'/',l_dir+'\\')
            sftp.rmdir(r_dir)                   # 서버쪽에 디렉토리를 지운다. 디렉토리안에 파일은 아래에서 지운다.
        else:
            if not os.path.exists(l_dir):
                sftp.get(r_dir, l_dir)          # 디렉토리안에 파일을 먼저 삭제한다.
            sftp.remove(r_dir)

# ######################################################## 2. 원격 파일을 원격서버에 백업한다.
def Remote_FileBackUp(Source, Target):
    try:
        os.chdir(Source)
        SysPlt = "/"
        for file in glob.iglob('**/*', recursive=True):
            Source_f = Source + file
            Target_f = Target + file

            # 폴더일경우 원격에 폴더를 만들고 자기참조
            if os.path.isdir(Source_f):
                sftp.mkdir(Target_f)
                Remote_FileBackUp(Source_f + strSplitDef,
                                    Target_f + SysPlt)
            # 파일일 경우만 원격 전송
            if os.path.isfile(Source_f):
                sftp.put(Source_f, Target_f)
    except:
        print("connect error")

# ######################################################## 3. 결과물을 원격 파일로 전송
def Remote_FileUp(RemoteDir, LocalDir):
    dirname = os.listdir(LocalDir)
    for fname in dirname:
        full_fname = os.path.join(LocalDir, fname)
        r_dir = RemoteDir+fname
        sftp.put(full_fname, r_dir)         # 서버쪽으로 전송
        os.remove(full_fname)               # 로컬결과물 삭제


# ######################################################## 4. 결과물 파일을 삭제
def Local_DirRemove(LocalDir):
    os.chdir(LocalDir)
    dirname = os.listdir(LocalDir)
    for fname in dirname:
        rd = LocalDir+fname
        if os.path.isdir(rd):
            shutil.rmtree(rd)


# ######################################################## 5. 오류 파일을 원격서버로 전송
def Remote_ErrorFileUp(v_Remote_ErrorDir, v_strError):
    dirname = os.listdir(v_strError)
    for fname in dirname:
        full_fname = os.path.join(v_strError, fname)
        r_dir = v_Remote_ErrorDir+fname
        sftp.put(full_fname, r_dir)         # 서버쪽으로 전송
        os.remove(full_fname)               # 로컬결과물 삭제


######################################################## 1단계. 원격 파일을 로컬상으로 다운로드
print("=====================================>파일복사중")
Remote_FileDown(Remote_BaseDir, strOrg)


# ######################################################## 2단계. 원본파일 백업
print("=====================================>원본파일 백업 중")
sss = Get_ID_Make()
sss = "receivework_" + sss + "/"
v_Remote_BackDir = Remote_BackDir + sss
sftp.mkdir(v_Remote_BackDir)
Remote_FileBackUp(strOrg,v_Remote_BackDir)


# ######################################################## 3단계. 실제 여기서 처리 작업을 한다.
print("=====================================>작업처리중")
dirsearch(strOrg, strExt)


# ######################################################## 4단계. 결과물을 서버쪽에 전송한다.
print("=====================================>결과전송중")
Remote_FileUp(Remote_PdfResult, strRead)


# ######################################################## 5단계. 로컬상의 존재하는 결과물을 삭제한다.
print("=====================================>파일삭제중")
Local_DirRemove(strOrg)


# ######################################################## 6단계. 오류정보 서버로 전송한다.
print("=====================================>오류정보서버로 이관 중")
sss = Get_ID_Make()
v_Remote_ErrorDir = Remote_ErrorDir + sss + "/"
sftp.mkdir(v_Remote_ErrorDir)
Remote_ErrorFileUp(v_Remote_ErrorDir,strError)

sftp.close()
print("=====================================>작업완료")