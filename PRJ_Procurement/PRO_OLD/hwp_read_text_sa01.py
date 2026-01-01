# 상단에 표시
import sys
sys.path.append("c:\\work\\PLangVim")

import PY_PKG.SU_Hwp_Read_MO as phwp
import os
import re
import openpyxl as op

hwpReader = phwp.HwpReader('c:\\temp\\hwp', '03.서약서.hwp')
hwpReader = hwpReader.bodyStream()

print(hwpReader)

for keyItem in hwpReader.keys():
    strVList = hwpReader.get(keyItem)
    strVList = strVList.splitlines()
