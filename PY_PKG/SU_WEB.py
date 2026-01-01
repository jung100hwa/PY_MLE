import sys
import os
import platform
import time
from urllib import request
from requests import get
from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi
import PY_PKG.SU_DirFile_MO as SD
import datetime


############################################################# url 주소 중 http -> https 변경
# http 일경우 파일 다운로드가 안됨
def SU_Http_Https_Find(url):
    strurl = url
    ex = url[0:5].upper()
    if ex == 'HTTP:':
        strurl = strurl.replace('http','https').replace('HTTP','HTTPS')
    return strurl


############################################################# 첨부파일 다운로드
# soruceFolder : 첨부파일 다운로더 저장 폴더
# url : 첨부파일 url
# 한계 : 첨부된 파일이름이 한글명일때 깨짐
def SU_Http_File_Download(sourceFolder, url, num):
    try:
        # 시작시간
        start_time = datetime.datetime.now()

        remotefile = urlopen(url)
        blah = remotefile.info()['Content-Disposition']
        value, params = cgi.parse_header(blah)
        filename = params["filename"]
        fext = str(os.path.splitext(filename)[1])

        # 끝시간
        end_time = datetime.datetime.now()

        # 파일명 생성을 위한 시간차
        elapsed_time = end_time - start_time
        imsi = str(elapsed_time).replace(':', '').replace('.','')
        filename = SD.SU_MO_TimeReturn3() + imsi + str(num) + fext

        filename = sourceFolder+filename
        urlretrieve(url, filename)
    except:
        pass
