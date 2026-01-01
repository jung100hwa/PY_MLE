"""_summary_
pdf 파일 중에서 테이블 형태를 읽어 내는 것.
테이블 형태가 자주 변하는 것은 안되는 듯

설치시에는 반드시 pip3 install tabula-py로 해야 함.
그냥 tabula-py로 하면 안됨 
"""
import tabula
import pandas as pd
from tabulate import tabulate


pdf_path = "lastsample/PDF_TABULA_SAMPLE02.pdf"
pdf_path2 = "lastsample/PDF_TABULA_SAMPLE01.pdf"
pdf_path3 = "lastsample/PDF_TABULA_SAMPLE03.pdf"
pdf_path_imsi = "lastsample/campaign_donors.pdf"
export_file = "lastsample/PDF_TABULA_SAMPLE01.xlsx"


"""
multiple_tables : 테이블이 한페이지 여러개 있을 때 2개의 테입블을 합니다.
False이면 각 테이블의 제목을 포함하고 True이면 제목을 포함하지 않고 합친다. 결국 제목 포함여부이고 합치는 것은 맞다.

lattice : 하나의 셀이 여러줄로 되어 있을 때 False이면 각 줄마다 하나의 행으로 처리. True이면 반대 보통은 True일때가 많음.
그런데 True로 하면 정말 이상하게 나옴..ㅎ

그리고 PDF 특정지역만 읽을 때에는 이미지로 변경을 하는데 반드시 JPG로 하자. PNG는 정확한 위치가 아님.
"""
# strList = tabula.read_pdf(pdf_path, pages=1, multiple_tables=True, stream=True, lattice=False)
# df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))


# 한페이지에 하나만 있는 테이블은 깔끔하게 나오네
# strList = tabula.read_pdf(pdf_path, pages=1, multiple_tables=True, stream=True, lattice=True)
# df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))


# 어떠한 언급이 없으면 첫페이지를 읽는다.
# strList = tabula.read_pdf(pdf_path, stream=True)
# df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))


# 모든 페이지의 테이블을 얻는다.-만약에 연속된 어떠한 테이블을 제외하고는 쓸일이 거의 없다.
# 포맷이 다른 경우 이상함.
# strList = tabula.read_pdf(pdf_path, pages="all", stream=True)
# print(strList)

# 한페이지에 2개의 페이지가 있는 경우--생락되는 컬럼이 있음음
# strList = tabula.read_pdf(pdf_path, pages=2, multiple_tables=True, stream=True, lattice=True) # 이렇게 하지 말자, lattice=True 조건이 들어가면 이상함...
# 공통된 컬럼 위주로 나오고 컬럼명이 없는 것은 뒤에 나오네....
# strList = tabula.read_pdf(pdf_path, pages=2, stream=True, multiple_tables=True)
# df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))


# 다음은 특정 영역만...
# todo 이렇게 하기위해서는 출력하고자 하는 페이지를 이미지로 내보내서 그 부분만 마우스로 이동하면서 x,y좌를 읽어 내야 한다. 난 주로 알씨로 함
# todo 완전 중요한 것 무조건 jpg로 해야 한다. png로 하면 정확한 좌표가 나오지 않음!!!
# todo multiple_tables=False 로 해야 한다네. [y1,x1,y2,x2]
# strList = tabula.read_pdf(pdf_path, pages=1, area=[126, 149, 212, 462])
# df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))


# 아래는 컬럼의 폭을 지정한다. 테이블에 컬럼 줄이 없는 경우 어디까지를 하나의 컬럼으로 볼것인지 정도
# 그리고 옵션에 따라 리스트, 데이터프레임으로 리턴하는데 아래는 columns 옵션이 있어서 그런지 데이터프레임으로 리턴한다.
# strList = tabula.read_pdf(pdf_path_imsi,guess=False, pages=1, columns=[47, 147, 256, 310, 375, 431, 504])
# df = strList[0].drop(["Unnamed: 0"], axis=1)
# print(type(df))
# print(tabulate(df, headers='keys', tablefmt='simple_outline'))

# 아래 부분은 거의 사용할 일이 없을 듯듯
strList = tabula.read_pdf(
    pdf_path3,
    pages="1",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)
df = pd.concat(strList, ignore_index=True) if strList else pd.DataFrame()
print(tabulate(df, headers='keys', tablefmt='simple_outline'))