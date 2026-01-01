import os
import shutil
import xml.etree.ElementTree as ET
import zipfile
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
import pandas as pd
import re
import urllib.error
from urllib import request
from requests import get
from urllib.parse import urlparse

# f = open('/home/jung100hwa/temp/test.xml','r', encoding='utf-8')
# fs = f.read()

# com = re.compile("<hp:t>.+?</hp:t>",re.MULTILINE) # 모니카 대화만
# ml = com.findall(fs)
# print(ml)

# def download_file(url, dst_path):
#     try:
#         with urllib.request.urlopen(url) as web_file:
#             data = web_file.read()
#             with open(dst_path, mode='wb') as local_file:
#                 local_file.write(data)
#     except urllib.error.URLError as e:
#         print(e)
        
# url = 'http://www.g2b.go.kr:8081/ep/co/fileDownload.do?fileTask=NOTIFY&fileSeq=20221247090::00::1::1'
# # url = 'https://www.python.org/static/img/python-logo.png'
# dst_path = "c:\\temp\\aa.hwp"
# download_file(url, dst_path)


def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url, stream=True)  # get request
        file.write(response.content)      # write to file

url = "https://www.g2b.go.kr:8081/ep/co/fileDownload.do?fileTask=NOTIFY&fileSeq=20221247090::00::1::1"
download(url,"c:\\temp\\aa.hwp")


# url = "http://www.g2b.go.kr:8081/ep/co/fileDownload.do?fileTask=NOTIFY&fileSeq=20221247090::00::1::1"
# savename = "abc.hwp"

# request.urlretrieve(url,savename)
# print("저장되었습니다.")


# url = "https://www.g2b.go.kr:8081/ep/co/fileDownload.do?fileTask=NOTIFY&fileSeq=20221247090::00::1::1"

# parsed_file = urlparse(url)
# file_name = os.path.basename(parsed_file.path)
# file_name = "c:\\temp\\" + file_name
# req = get(url)
# url_content = req.content
# csv_file = open(file_name,'wb')
# csv_file.write(url_content)
# csv_file.close()


# def download(url, file_name = None):
# 	if not file_name:
# 		file_name = url.split('/')[-1]

# 	with open(file_name, "wb") as file:
#      response = get(url)
#      file.write(response.content)      
         
# url = "https://me.go.kr/home/file/readDownloadFile.do?fileId=246384&fileSeq=1"
# download(url)
