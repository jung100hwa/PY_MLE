import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import PY_PKG.SU_ALLMO_Init_MO as psai
import PY_PKG.SU_DirFile_MO as pFile
import PY_PKG.SU_File_Convert as pConvert
import PY_PKG.SU_Mail_Send_Mo as pMail
import openpyxl as op
import datetime
import platform
import time
import cx_Oracle


psai.SU_MO_VarInit(psai.G_SU_INIT_LIST,"DV_PROCUREMENT")

# 파일에서 읽어오기
pFile.SU_MO_HwpRead_Hwpx("c:\\temp\\","test.hwpx" )
