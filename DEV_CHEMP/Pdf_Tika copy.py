# tika는 아파치 재단에서 하는 것으로 별도 웹서버가 가동되어야 함
# 개인적으로 환경이 제대로만 갖춰진다면 표를 제외학 이게 최고 인듯

from tika import parser
import SU_Init as SU_Init

SU_Init.SU_MO_VarInit(1)

raw_pdf = parser.from_file(SU_Init.G_SU_ExFilePosIn + "20210914_승인대상.pdf")
strContent = raw_pdf['content']

print(strContent)
