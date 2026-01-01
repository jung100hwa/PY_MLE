
import tabula
import numpy as np
from SU_MO import SU_Init
from SU_MO import SU_Pandas_MO
from SU_MO import SU_Excel_MO
from SU_MO import SU_DirFile_MO

SU_Init.SU_MO_VarInit()
full_fname = SU_Init.G_SU_ExFilePosIn + "pdfreadersample.pdf"

keiti_xy = 0
keiti_001 = [10, 10, 500, 500]

# 좌측의 제품명, 제형, 상세제형, 제조국명을 구하기
strContent=tabula.read_pdf(full_fname, pages=1,area=keiti_001,
                           multiple_tables=False, stream=True)
df=strContent[0]
listStr001=df[df.columns[0]]
print(df)
