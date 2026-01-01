"""
특정디렉토리에 있는 한글 파일을 pdf로 전환한다.
프로젝트 산출물 PDF로 변환시 활용
한글파일과 ppt파일만을 pdf로 변환하고 나머지 파일들은 복사만 함
아래에 소스폴더와 타켓폴더를 적어준다. 타멧폴더만 만들고 서브폴더는 자동으로 만들어 줌.
소스폴더는 서브폴더가 많이 있어도 상관없음
그리고 참고로 glob의 동작방식에 유의해야 함. 1.먼저 폴더를 읽은 다음. 2.폴더별 파일을 처리하는 방식
"""
import os
import glob
import shutil
import win32com.client as win32     # pywin32
import time

Source = "c:\\work\\05.관리문서\\"
Target = "c:\\work\\관리산출물\\"

                     
def sfc_ppttopdf(Sourcefile, Targetfile):
    """
    PPT를 PDF로 변환
    :param Sourcefile: PPT, PPTX 파일
    :param Targetfile: PDF 파일명
    """
    try:
        ext = str(os.path.splitext(Sourcefile)[-1]).replace('.', '')
        if ext.upper() == "PPT" or ext.upper() == "PPTX":
            powerpoint = win32.Dispatch("Powerpoint.Application")
            # powerpoint.Visible = 0 # 백그라운드에서 수행. 먹지 않는다. 아래와 같이  WithWindow=False 해야 함
            deck = powerpoint.Presentations.Open(Sourcefile, WithWindow=False)
            deck.SaveAs(Targetfile, 32)                 # 32번이 PDF
            # deck.PrintOut(PrintToFile=Targetfile)     # 프린터가 직접함. 약간 시간이 빠른듯
            time.sleep(2)  # Enough time to ensure the print operation is complete
            deck.Close()
            powerpoint.Quit()
    except ZeroDivisionError as e:
        print(e)

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")

def hwptopdf_f(Source,Target):
    try:
        for file in glob.iglob(Source + "**/*", recursive=True):    
            Source_f = file
            Target_f = Target + Source_f.replace(Source, '')  # 이코드가 신의 한수 였다.
            if os.path.isdir(Source_f):
                if not os.path.exists(Target_f):
                    os.mkdir(Target_f)

            if not os.path.isdir(Source_f):
                bfname = os.path.basename(Source_f)
                
                # 아래는 ppt파일을 pdf로 변환시 임시파일 자체도 읽어와서 제외시키는 함수
                if bfname[0] == "~":
                    continue
                
                ext = str(os.path.splitext(file)[-1]).replace('.', '')
                if ext.upper() == "HWP" or ext.upper() == "HWPX":
                    hwp.Open(Source_f)

                    Target_f = str(Target_f).replace(ext, 'pdf')

                    # pdf로 저장할 때는 이 방법이 조금 나은듯
                    hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)
                    hwp.HParameterSet.HFileOpenSave.filename = Target_f
                    hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
                    hwp.HAction.Execute("FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)

                    print("==========> " + file + " : 변환완료")
                else:
                    if ext.upper() == "PPT" or ext.upper() == "PPTX":
                        Target_f = str(Target_f).replace(ext, 'pdf')                    
                        sfc_ppttopdf(Source_f,Target_f)
                        print("==========> " + file + " : 변환완료")
                    else:
                        shutil.copyfile(Source_f, Target_f)
                        print("==========> " + file + " : 복사완료")
    except:
        pass

        
hwptopdf_f(Source,Target)
hwp.Quit()