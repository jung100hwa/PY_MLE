# 폴더를 모니터링 하면서 파일을 PDF로 변환 함
import sys
import os
import time
import shutil
import glob
import PY_PKG.SU_File_Convert as sfc
import PY_PKG.SU_ALLMO_Init_MO as psai
import PY_PKG.SU_FILE_WRITE_READ as sfw
import PY_PKG.SU_DL_NLTP as sdn
import datetime
import zipfile

# 설정파일 초기화
psai.SU_MO_VarInit(psai.G_SU_INIT_LIST,"")

# 아래변수는 공고파일이 ZIP 파일일 경우를 고려해서 만듬
RETURNFILEPATH = []

######################################################## PDF로 변환
# 하나의 폴더를 감시해서 정의한 파일이 들어오면 PDF로 변환한다.
# sourceFolder : 원본 파일
# destFolder   : PDF로 변환해서 저장할 폴더
# bakFolder    : 원본 파일 백업
def SU_FOLD_MONITORING(sourceFolder,destFolder,bakFolder):
    imageExtList = ['.png','.jpg', '.jpeg']

    while True:
        for file in glob.iglob(sourceFolder + "/**/*", recursive=True):
            if os.path.isfile(file):
                filename = os.path.basename(file)
                fext = str(os.path.splitext(filename)[-1])
                dfilename = filename.replace(fext,".pdf")

                fextname = str(fext).upper()[1:]
                dfilename = destFolder + "\\" + dfilename

                if fextname == "HWP":
                    sfc.sfc_hwptopdf2(file,dfilename)
                    
                if fextname == "HWPX":
                    sfc.sfc_hwptopdf3(sourceFolder,sourceFolder)

                if fextname == "DOC":
                    sfc.sfc_wordtopdf(file,dfilename)

                if fextname == "XLS" or fextname == "XLSX":
                    sfc.sfc_exceltopdf(file,dfilename)
                    
                if fextname == "PPT" or fextname == "PPTX":
                    sfc.sfc_ppttopdf(file,dfilename)

                if fextname == "PDF":
                    shutil.move(file, dfilename)
                    print(file + " =======>>" + dfilename)
                    continue

                if fextname.lower() in imageExtList:
                    sfc.sfc_imagetopdf(file, dfilename)

                bakfile = bakFolder + "\\" + filename
                shutil.move(file, bakfile)

                print(file + " =======>>" + dfilename)

        print("waiting....")
        time.sleep(2)
    

######################################################## 파일을 텍스트 추출 및 파일 저장, 전처리 작업(딥러닝)
# sourceFolder : 원본 폴더명
# targetFolder : 과업지침서에서 읽은 본문내용을 txt 파일로 저장할 폴더
# gCursor      : db 커서
# gsplit       : 디렉토리 구분자
# dbInserYN   : DB에 넣을지 여부
# 내용
#   - clob으로 폴더를 해도 되지 않음(4000 이상)
#   - DB에 저장된 파일명을 읽어서 수행
# 주의          : 사실 하나의 파일만 하면 소스 폴더가 필요 없으나, hwpx 은 풀어 해지면 여러개의 폴더 여러개의 파일 존재 함. 즉 원본 폴더를 지정하는게 나음

def SU_FOLD_MONITORING2(sourceFolder, targetFolder, gCursor, gCon, gsplit, dbInserYN = 0):
    strCon = ""
    strDate = datetime.datetime.now().strftime('%Y-%m-%d')

    filepath = ""
    # 하나의 폴더에 하나의 파일만 있으니 사실 하위폴더까지 조회하는 기능은 필요 없음
    # zip 파일경우는 2개 이상의 파일이 존재할 수 있으나 역시 하위 폴더는 없는 것으로 가정
    try:
        for file in glob.iglob(sourceFolder + "/**/*", recursive=True):
            strRefile = file
            if os.path.isfile(file):
                filename = os.path.basename(file)
                fext = str(os.path.splitext(filename)[-1])
                fextname = str(fext).upper()[1:]

                if fextname == "HWP":
                    strCon = sfw.SU_MO_HwpRead_Extract(file)

                if fextname == "HWPX":
                    strCon = sfw.SU_MO_HwpRead_Hwpx(sourceFolder, filename)
                    fileimsi = str(file).replace(fext, ".zip")
                    strRefile = fileimsi

                # 왠만하면 java -jar '설치경로\\tika -server' 실행시켜 놓고 해라. 그렇치 않으면 첫번째 파일은 읽어오지 못할때가 많다.
                # 첫번째 파일 읽으면서 실행되기 때문인것 같은데 잘 모르겠음 
                if fextname == "PDF":
                    strCon = sfw.SU_MO_PdfRead_Extract(file)
                    
                if fextname == "XLS" or fextname == "XLSX":
                    strCon = sfw.SU_MO_ExcelRead_Extract(file)

                if fextname == "ZIP":
                    output_unzip = zipfile.ZipFile(strRefile, "r")
                    output_unzip.extractall(sourceFolder)
                    output_unzip.close()
                    os.remove(strRefile)
                    
                    # zip된 파일들의 파일명을 일관되게 바꾸기 위해
                    zipfileindex = 1
                    for zf in glob.iglob(sourceFolder + "/**/*", recursive=True):
                        zipfilename = str(os.path.splitext(strRefile)[0][0:-1] + str(zipfileindex))
                        zipfilenamefext = str(os.path.splitext(zf)[-1])
                        modzipfilename = zipfilename + zipfilenamefext
                        os.rename(zf, modzipfilename)
                        zipfileindex = zipfileindex + 1
                        
                    SU_FOLD_MONITORING2(sourceFolder, targetFolder, gCursor, gCon, gsplit, 1)

                # 받은 파일은 삭제함
                if fextname != "ZIP":
                    os.remove(strRefile)

            if len(strCon) > 0:
                filepath = targetFolder + strDate.replace('-', '') + gsplit + str(filename).replace(fext, '') + ".txt"
                RETURNFILEPATH.append(filepath)
            
                # todo 전처리 작업을 수행 !! 핵심
                strCon = sdn.SU_DL_PREPROCELLING(1, strCon)
            
                # 파일경로에 파일내용 TXT 파일 만들기
                filenm = str(filename).replace(fext, '') + ".txt"     # 파일명만 필요함
                sfw.SU_MO_FileWrite4(targetFolder, filenm, strCon, gsplit)

        return RETURNFILEPATH
    except:
        os.remove(strRefile)
        pass
    return ""