import os
import glob
import shutil
import win32com.client as win32
import win32gui
from docx import Document
from docxcompose.composer import Composer
import docx2pdf
import pdf2docx								# 상당히 많은 종속성 패키지가 설치됨
from PyPDF2 import PdfFileMerger
# poppler라고 검색해서 다운로드 받고 환결설정에 bin 폴더를 잡아줘야 함
from pdf2image import convert_from_path
import winreg
import re
from PIL import Image
import time


############################################################# 한장의 이미지를 하나의 pdf로 변환
# Sourcefile : 원본 이미지
# Targetfile : pdf 파일
def sfc_imagetopdf(Sourcefile, Targetfile):
    try:
        image1 = Image.open(Sourcefile)
        im1 = image1.convert('RGB')
        im1.save(Targetfile)
    except:
        return


############################################################# 여러장의 이미지를 하나의 pdf로 변환
# Sourcefilelist : 원본 이미지 리스트
# Targetfile : pdf 파일
def sfc_imagestopdf(Sourcefilelist, Targetfile):
    try:
        imagelist = []
        for index, imagefile in enumerate(Sourcefilelist):
            image = Image.open(imagefile)
            im = image.convert('RGB')
            imagelist.append(im)
        imagelist[0].save(Targetfile,save_all=True, append_images=imagelist)
    except:
        return


############################################################# 변환시 선택박스 차단
# 가끔 윈도우 선택박스가 떠서 뭔가를 선택해야 하는 경우가 발생하는데
# 이 것을 방지하는 코드라고 함. 실행은 해보지 않음
def sfc_windowselect_stop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Console', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "QuickEdit", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(key, "InsertMode", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)



#############################################################
# 한글 파일을 pdf로 변환
# 한글파일을 pdf변환, 윈도우에서만 사용가능 함. 리눅스에 한글이 깔려 있을리 없지 않은가
# 아래 사이트를 방문 또는 검색 "한/글 오토메이션용 보안승인모듈"
# https://www.hancom.com/board/devdataView.do?board_seq=47&artcl_seq=4085&pageInfo.page=&search_text=
# 이유는 pdf 변환시 보안허용 창이 뜨는 것 방지
# 이문서에 보면 레지스트리도 설정해야 함.
# Source : 한글파일 디렉토리
# Target : pdf 저장 디렉토리
# 기본은 하위디렉토리에 한글 파일이 있으면 동일 구조로 만들고 hwp -> pdf로 변환
def sfc_hwptopdf(Source, Target):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
       
    for file in glob.iglob(Source + "**/*", recursive=True):
        Source_f    = file
        Target_f    = Target + Source_f.replace(Source,'')      # 이코드가 신의 한수 였다.
        
        if os.path.isdir(Source_f):
            if not os.path.isdir(Target_f):
                os.mkdir(Target_f)
        
        if not os.path.isdir(Source_f):
            filename = os.path.basename(file)
            filename = os.path.splitext(filename)
            
            pre = filename[0] # 파일명
            ext = filename[1] # 확장자
            ext2 = ext[1:4]   # 한글파일 버전에 따라 hwpx도 있음

            if ext2.upper() == "HWP":
                hwp.Open(Source_f)
                Target_f = str(Target_f).replace(ext, ".pdf")
                hwp.SaveAs(Target_f, "PDF")
                
                # 이 부분은 무조건 적어 주자. 안그러면 큰 파일 같은 경우 저장 팝업이 뜨고 프로세스가 죽지 않는다.
                # 역시 한글은 워드 등 따라 갈려면 멀었다.....
                hwp.Save()
                
                print("hwp->pdf : " + Target_f)
    hwp.Quit()
    
 
#############################################################
# 한글 파일을 pdf로 변환
# 이 함수는 단지 hwp 버전 때문에 만들어진 함수라고 생각하면 됨
# 최신 한글은 hwpx 등 확장자가 여러가지 임. 또한 버젼이 업그레드 될 수록 파일 포맷이 달라질 수 있음
# 때문에 일관되게 파일 포맷을 가져 가기 위해 작성됨. 또한 한글 직접 읽을 수 있는 모듈 때문에도 필요함
# 단점 : 한글이 있어야 함. 아래 파일(dll)이 경로에 있어야 함
def sfc_hwptopdf3(Source, Target):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
       
    for file in glob.iglob(Source + "**/*", recursive=True):
        Source_f    = file
        Target_f    = Target + Source_f.replace(Source,'')      # 이코드가 신의 한수 였다.
        
        if os.path.isdir(Source_f):
            if not os.path.isdir(Target_f):
                os.mkdir(Target_f)
        
        if not os.path.isdir(Source_f):
            filename = os.path.basename(file)
            filename = os.path.splitext(filename)
            
            pre = filename[0] # 파일명
            ext = filename[1] # 확장자
            ext2 = ext[1:4]   # 한글파일 버전에 따라 hwpx도 있음

            if ext2.upper() == "HWP" or ext2.upper() == "HWPX":
                hwp.Open(Source_f)
                Target_f = str(Target_f).replace(ext, ".hwp")
                hwp.SaveAs(Target_f, "HWP")                
                print(pre + " : 변환완료")
                
                # 이 부분은 무조건 적어 주자. 안그러면 큰 파일 같은 경우 저장 팝업이 뜨고 프로세스가 죽지 않는다.
                # 역시 한글은 워드 등 따라 갈려면 멀었다.....
                hwp.Save()
    hwp.Quit()
    


#############################################################
# 한글파일을 pdf변환 파일을 직접
def sfc_hwptopdf2(Sourcefile, Targetfile):
    try:
        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
        hwp.Open(Sourcefile)
        hwp.SaveAs(Targetfile, "PDF")
        hwp.Save()
        hwp.Quit()
    except:
        hwp.Save()
        hwp.Quit()
        

#############################################################
# ms word파일을 pdf로 변환
# source : 워드파일(완전한 경로)
# target : 변환해서 저장할 pdf 파일(완전한 경로)
def sfc_wordtopdf(source, target):
    try:
        docx2pdf.convert(source, target)
    except:
        print("pdf 변환 오류")
        
        
#############################################################
# excel pdf변환 파일을 직접
def sfc_exceltopdf(Sourcefile, Targetfile):
    try:
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = False # 백그라운드에서 수행
        wb = excel.Workbooks.Open(Sourcefile)
        wb.ActiveSheet.ExportAsFixedFormat(0, Targetfile)
        wb.Close(False)
        excel.Quit()
    except:
        excel.Quit()
        
        
#############################################################
# ppt pdf변환 파일을 직접
def sfc_ppttopdf(Sourcefile, Targetfile):
    try:
        powerpoint = win32.Dispatch("Powerpoint.Application")
        # powerpoint.Visible = 0 # 백그라운드에서 수행. 먹지 않는다. 아래와 같이  WithWindow=False 해야 함
        deck = powerpoint.Presentations.Open(Sourcefile, WithWindow=False)
        deck.SaveAs(Targetfile, 32)                 # 32번이 PDF
        # deck.PrintOut(PrintToFile=Targetfile)     # 프린터가 직접함. 약간 시간이 빠른듯
        time.sleep(2)  # Enough time to ensure the print operation is complete
        deck.Close()
        powerpoint.Quit()
    except:
        powerpoint.Quit()


#############################################################
# pdf 파일을 이미지로 변환
# pdf가 3페이지 라면 3개의 이미지가 만들어짐
# sourcefile : 이미지로 변환하고자 하는 pdf 파일
# targetdir  :  이미지 저장 폴더
def sfc_pdftoimage(sourcefile, targetdir):
    try:
        pages = convert_from_path(sourcefile)
        fname = os.path.basename(sourcefile)
        fname = fname[:-4]  # .pdf를 제외한 파일명만
        for i, page in enumerate(pages):
            page.save(targetdir + fname + "_" + str(i+1) + ".jpg", "JPEG")
    except:
        print("이미지 변환 오류")


#############################################################
# 워드 파일 합치기
# filename_master  : 기준이 되는 파일. 이 마스터 파일에 다른 파일을 추가
# files_list       : 기준 파일에 합칠 파일 리스트
# savefilename     : 합쳐서 저장할 파일 명
def sfc_combine_all_docx(filename_master, files_list, savefilename):
    try:
        number_of_sections = len(files_list)
        master = Document(filename_master)
        composer = Composer(master)
        for i in range(0, number_of_sections):
            doc_temp = Document(files_list[i])
            composer.append(doc_temp)
        composer.save(savefilename)
    except:
        print("파일 병합 오류")


#############################################################
# pdf파일을 ms_word로 변환
# source : pdf 파일(완전한 경로)
# target : 변환해서 저장할 word 파일(완전한 경로)
def sfc_pdftoword(source, target):
    try:
        cv = pdf2docx.Converter(source)
        cv.convert(target, start=0, end=None)
        cv.close()
    except:
        print("pdf 변환 오류")


#############################################################
# 여러개의 pdf 파일을 하나로 합치기
# source   : 합칠 pdf가 존재하는 디렉토리
# filelist : 디렉토리안에 존재하면서 합칠 pdf 리스트
# target   : 합쳐진 pdf 저장될 디렉토리
# savepdfname : 하나로 합쳐진 pdf 파일명
def sfc_pdfmerge(source, filelist, target, savepdfname):
    try:
        if len(filelist) > 0:
            merger = PdfFileMerger()
            for pdfitem in filelist:
                pdfitem = source + pdfitem
                merger.append(pdfitem)
            merger.write(target + savepdfname)
            merger.close()
    except:
        return ""