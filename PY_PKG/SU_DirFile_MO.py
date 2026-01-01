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
import PY_PKG.SU_ALLMO_Init_MO as psai
import PY_PKG.SU_Hwp_Read_MO as phwp
import io
import re

psai.SU_MO_VarInit(psai.G_SU_INIT_LIST,"")

# 운영되는 플랫폼 확인
strSplitDef = psai.G_SU_SplitDef
strPlatform = psai.G_SU_Platform

# 원격서버 연결 정보(SSH)
Remote_Server   = psai.G_SU_REMOTE_SERVER
Remote_UserName = psai.G_SU_REMOTE_USER
Remote_UserPwd  = psai.G_SU_REMOTE_PASSWORD
Remote_port     = psai.G_SU_REMOTE_PORT


############################################################# 동일 OS에서 디렉토리 복사
# Source : 원본
# Target : 목표
def SU_MO_DirCopy(Source, Target):
    try:
        if not os.path.isdir(Source):
            print("Source 디렉토리가 존재하지 않음")
        if os.path.isdir(Target):
            shutil.rmtree(Target)               # 기존 디렉토리가 존재하면 삭제
        shutil.copytree(Source, Target)
    except:
        pass


 ############################################################# 동일 OS에서 특정 파일만 복사
# Source : 원본
# Target : 타킷
# CopyExt : 복사할 대상 확장자, *이면 모든 파일(디렉토리 복사와 동일)
def SU_MO_FileCopyExt(Source, Target, CopyExt):
    try:
        for file in glob.iglob(Source+"**/*", recursive=True):
            Source_f = file
            Target_f = Target + Source_f.replace(Source,'')

            # 일단 isdir 이것은 1.디렉토리가 존재하는지 2. 디렉토리인지 2개를 검사
            # 존재도 안하는 것을 디렉토리인지 파일인지 구분하지 못함. 그래서 원본 파일로 먼저 검사
            if os.path.isdir(Source_f):
                if not os.path.isdir(Target_f):
                    os.mkdir(Target_f)
                    print(Target_f + " 디렉토리 생성")
            else:
                if not os.path.isfile(Target_f):
                    if CopyExt != '*':
                        Ext = str(os.path.splitext(Source_f)[1])
                        Ext = Ext[1:]
                        if Ext.upper() == str(CopyExt).upper():
                            shutil.copyfile(Source_f, Target_f)
                            print(Target_f + " 파일복사")
                    else:
                        shutil.copyfile(Source_f, Target_f)
                        print(Target_f + " 파일복사")
    except:
        pass

############################################################# 원본 폴더에 있는 파일을 하나의 디렉토리로 복사
# 존재하면 복사하지 않음
# Source : 원본
# Target : 타킷
# CopyExt : 복사할 대상 확장자, *이면 모든 파일(디렉토리 복사와 동일)
def SU_MO_FileCopyExt2(Source, Target, CopyExt):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            Source_f = file
            Target_f = Target

            # 디렉토리가 아닌것만 복사
            if not os.path.isdir(Source_f):
                Target_f = Target + os.path.basename(file)
                if not os.path.isfile(Target_f):
                    if CopyExt != '*':
                        Ext = str(os.path.splitext(Source_f)[1])
                        Ext = Ext[1:]
                        if Ext.upper() == str(CopyExt).upper():
                            shutil.copyfile(Source_f, Target_f)
                            print(Target_f + " 파일복사")
                    else:
                        shutil.copyfile(Source_f, Target_f)
                        print(Target_f + " 파일복사")

    except:
        pass


############################################################# 특정 폴더 삭제
def SU_MO_DirRemove(Target):
    try:
        if os.path.isdir(Target):
            shutil.rmtree(Target)
    except:
        pass

############################################################# 특정 폴더 모든 파일 삭제
# Source  : 원본
def SU_MO_FileAllRemove(Source):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            if not os.path.isdir(file):
                shutil.rmtree(file)
            if os.path.isfile(file):
                os.remove(file)
    except:
        pass

############################################################# 원본 폴더에서 특정 확장자 삭제(대소문가 구문하지 않음)
# Source  : 원본
# RmExt   : 삭제할 확장자
def SU_MO_FileExtRemove(Source, RmExt):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            if not os.path.isdir(file):
                if os.path.isfile(file):
                    ext = os.path.splitext(file)
                    ext = ext[1][1:].upper()
                    if str(RmExt).upper() == ext:
                        os.remove(file)
    except:
        pass


############################################################# 원본 폴더에서 지정한 파일(대소문가 구문하지 않음) 삭제
# Source   : 원본
# filename : 삭제할 파일명
def SU_MO_FileNameRemove(Source, filename):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            if not os.path.isdir(file):
                if os.path.isfile(file):
                    fname = os.path.basename(file)
                    fname = fname.upper()
                    if str(filename).upper() == fname:
                        os.remove(file)
    except:
        pass


############################################################# 특정 폴더내에서 파일 존재 여부
# Source	 : 원본
# FName		 : 찾고자 파일명
# 리턴		 : 존재하면 true, 없으면 false
def SU_MO_FindFilename(Source, FName):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):
            fn = os.path.basename(file)
            fn = fn.upper()
            if str(FName).upper() == fn:
                return True
    except:
        print("FindFile Err")
    return False


############################################################# 원격파일 다운로드
# source : 원격 디렉토리
# target : 로컬 디렉토리. 보통은 윈도우 서버
# Mod가 1이면 복사, 2이면 이동
# Plt 원격 플랫폼 1이면 윈도우, 2이면 유닉스. 즉 다운로드할 원격 서버 플랫폼 보통은 리눅스
def SU_MO_Remote_FileDown(Source, Target, Mod=1, Plt=2):
    try:
        # 아래 부분은 시스템에 한번만 수행될 수 있도록 한다.
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(Remote_Server, username=Remote_UserName,
                    password=Remote_UserPwd, port=Remote_port)
        sftp = ssh.open_sftp()

        # 원격서버의 종류에 따라 폴더 구분자 정의
        SysPlt = "\\"
        if Plt == 1:
            SysPlt = "\\"
        else:
            SysPlt = "/"

        for remotedir in sftp.listdir_attr(Source):
            r_dir = Source + remotedir.filename
            l_dir = Target + remotedir.filename

            if S_ISDIR(remotedir.st_mode):  # 폴더이면
                if not os.path.exists(l_dir):
                    os.makedirs(l_dir)
                SU_MO_Remote_FileDown(
                    r_dir+SysPlt, l_dir+strSplitDef, Mod, Plt)
                if Mod == 2:
                    sftp.rmdir(r_dir)
            else:							# 파일이면
                if not os.path.exists(l_dir):
                    sftp.get(r_dir, l_dir)
                if Mod == 2:
                    sftp.remove(r_dir)
    except:
        print("connect error")
    finally:
        sftp.close()


############################################################# 원격파일로 업로드
# source : 로컬파일 일반적으로 윈도우 서버에 있는 디렉토리
# target : 목적지 파일 일반적으로 리눅스 또는 유닉스
# Mod가 1이면 복사, 2이면 이동
# Plt 원격 프랫폼 1이면 윈도우, 2이면 유닉스
# 현재 윈도우로 업로드 할 수는 없다. 윈도우 서버 고정 아이피가 없으니까
def SU_MO_Remote_FileUp(Source, Target, Mod, Plt):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(Remote_Server, username=Remote_UserName,
                    password=Remote_UserPwd, port=Remote_port)
        sftp = ssh.open_sftp()

        os.chdir(Source)

        SysPlt = "\\"
        if Plt == 1:
            SysPlt = "\\"
        else:
            SysPlt = "/"

        for file in glob.iglob('**/*', recursive=True):
            Source_f = Source + file
            Target_f = Target + file

            # 폴더일경우 원격에 폴더를 만들고 자기참조
            if os.path.isdir(Source_f):
                sftp.mkdir(Target_f)
                SU_MO_Remote_FileUp(Source_f + strSplitDef,
                                    Target_f + SysPlt, Mod, Plt)

            # 파일일 경우만 원격 전송
            if os.path.isfile(Source_f):
                sftp.put(Source_f, Target_f)

        if Mod == 2:
            shutil.rmtree(Source)

    except:
        print("connect error")
    finally:
        sftp.close()


############################################################# 파일비교(txt, pdf)
# 기본적인 파일일 경우에는 filecmp로 내용까지 검토가 되는 것 같은데
# PDF 같은 경우는 내용을 비교할려면 PDF 리더기로 읽어 내용을 비교한다.
# PDF는 같은 파일을 내용과 관계없이 생성일자, 파일 사이즈 등 상택값으로 비교하는 것 같음
def SU_MO_FileVS(filename1, filename2, filetype):
    filetype = filetype.upper()

    try:
        if filetype == "TXT":
            if(filecmp.cmp(filename1, filename2)):
                return 1
            else:
                return 0

        if filetype == 'PDF':
            raw_pdf = parser.from_file(filename1)
            strContent = raw_pdf['content']

            raw_pdf = parser.from_file(filename2)
            strContent2 = raw_pdf['content']

            if strContent == strContent2:
                return 1
            else:
                return 0
    except:
        pass


############################################################# 하나의 디렉토리 안의 파일 비교
# dir1, dir2 비교할 폴더
# 리스트[왼쪽에만 있는 파일리스트, 오른쪽에만 있는 파일리스트, 파일 있는데 다른 파일리스트]
def SU_MO_Dircmp(dir1, dir2):
    fd = filecmp.dircmp(dir1, dir2)
    listleft     = []
    listright    = []
    listnosame   = []

    for a in fd.left_only:
        listleft.append(a)

    for b in fd.right_only:
        listright.append(b)

    for x in fd.diff_files:
        listnosame.append(x)

    return listleft, listright, listnosame


############################################################# 간단하게 년월일시분초미리초까지 리턴
# 년-월-일 이런형식으로 정확히 밀리센컨드까지 정의
def SU_MO_TimeReturn2():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')


############################################################# 간단하게 년월일시분초미리초까지 리턴("-" 없음)
# 주로 유일한 파일명, 랜덤형식의 숫자를 얻기 위한 것
def SU_MO_TimeReturn3():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')


############################################################# 년월일시간분값을 리턴. gubun 값에 따라 리턴값 달리
# 초기에 사용했던 함수로 거의 사용할 일이 없음
def SU_MO_TimeReturn(gubun):
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

    sSec = str(datetime.datetime.now().second)
    if len(sSec) == 1:
        sSec = "0" + sSec

    if gubun == 1:
        sss = sYear
    elif gubun == 2:
        sss = sYear + sMon
    elif gubun == 3:
        sss = sYear + sMon + sDay
    elif gubun == 4:
        sss = sYear + sMon + sDay + sHour
    elif gubun == 5:
        sss = sYear + sMon + sDay + sHour + sMin
    else:
        sss = sYear + sMon + sDay + sHour + sMin + sSec
    return sss