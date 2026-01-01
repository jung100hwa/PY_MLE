import pandas as pd
import numpy as np
from SU_MO import SU_Init
from SU_MO import SU_Pandas_MO
from SU_MO import SU_Excel_MO
from SU_MO import SU_DirFile_MO


############################################################################################ 초기 세팅
SU_Init.SU_MO_VarInit()

# 엑셀파일 열기
df = SU_Pandas_MO.SU_MO_ReturnRead_excel(SU_Init.G_SU_ExFilePosIn + "chemp_gosi_review_pandas.xlsx", 0, False)

# 원본데이터를 가공
df['살생물물질명'] = df['살생물물질명'].str.replace("""'""","")
df['고유번호'] = df['고유번호'].str.replace(' ','')
df['살생물제품유형'] = df['살생물제품유형'].str.replace(' ','')

# 컬럼의 문자열 전체 치환, 국립환경과학원에서 자료를 제대로 정의할 필요가 있음
df.replace({'살생물제품생유형': {'4-선박·수중시설용오염방지제' : '4-가.선박·수중시설용오염방지제'}}, inplace=True)

# 2000-01-01 날짜 형태로 세팅
df['승인유예기간'] = df['승인유예기간'].str[:10]
df['승인유예기간'] = df['승인유예기간'].str.replace(".","-", regex=False)   #regex=False 정규식 표현이 아니라 문자로 취급하라

# 접수번호 세팅
df['접수번호'] = df['접수번호'].map('EAS-N-{}'.format)

# 제품유형 코드 담기
strSQL = """SELECT CODE, REPLACE(CODE_NM,' ','') CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID='BCC003'"""
df_US = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)

# 회원정보 중 일반회원과 기업회원 정보 담기
strSQL = """SELECT ENTRPRS_MBER_ID AS ID, BIZRNO, CMPNY_NM, '기업회원' AS GUBUN FROM COMTNENTRPRSMBER"""
df_ID1 = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)


strSQL = """SELECT TB.MBER_ID AS ID, TA.BIZRNO, TA.CMPNY_NM, '일반회원' AS GUBUN FROM COMTNENTRPRSMBER TA 
INNER JOIN COMTNGNRLMBER TB ON TA.ENTRPRS_MBER_ID = TB.ENTRPRS_MBER_ID"""
df_ID2 = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)

df_ID = pd.concat([df_ID1, df_ID2], axis=0, ignore_index=True)

# 물질승인신청계획서 테이블 담기
strSQL = """SELECT RCT_NO, CAS_NO, ITEM_CD, DEL_YN FROM TN_EBM_COMPANY_LIST"""
df_Company = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)
df_Company['DEL_YN'] = df_Company['DEL_YN'].str.replace(' ','')

# 공동협의체 메인 담기
strSQL = """SELECT MST_ID, CAS_NO, USE_CODE, STS FROM TN_EBM_COOPERATION_T WHERE CATEGORY = 'C'"""
df_MPT = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)

# 공동협의체 상세 담기
strSQL = """SELECT MST_ID, BIZ_NO, (SELECT CODE_NM FROM COMTCCMMNDETAILCODE WHERE CODE_ID='TEC001' AND CODE =GROUP_ROLE) AS GROUP_ROLE, 
CREATE_ID, AGENT_YN, AGENT_NAME FROM TN_EBM_COOPERATION_MAP_T"""
df_DPT = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)

# 공동협의체를 한곳에 담기, 물질협의체를 담지 않기 위해 메인을 중심으로 조인한다.
df_DPT = pd.merge(df_MPT, df_DPT, how='left', left_on='MST_ID', right_on='MST_ID')

# 기존 살생물물질 신고
strSQL ="""SELECT RCPTNO, WR_ID, BIZ_NO, CN_NM FROM TN_EBMMST"""
df_EBMMST = SU_Pandas_MO.SU_MO_ReturnRead_sql(strSQL, SU_Init.G_SU_Connection)
df_EBMMST['BIZ_NO'] = df_EBMMST['BIZ_NO'].str.replace('-','')



# ############################################ 분석1) 승인유예고시 중 이름을 코드 변경하고 사업자번호 등을 추가한 자료
# 코드 데이터프레임과 통합, 유형코드를 알기 위해
df = pd.merge(df, df_US, how='left', left_on='살생물제품유형', right_on='CODE_NM')

# 기존살생물물질 신고와 합하기. 신청인 아이디를 알기 위해
df = pd.merge(df, df_EBMMST, how='left', left_on='접수번호', right_on='RCPTNO')

df.rename(columns={'CODE':'유형코드','WR_ID':'신청인아이디'}, inplace=True)
df.drop(['CODE_NM','RCPTNO','BIZ_NO','CN_NM'], axis=1, inplace=True)

# 사용자 테이블과 통합, 사용자 정보를 알기 위해
df = pd.merge(df, df_ID, how='left', left_on='신청인아이디', right_on='ID')
df.rename(columns={'BIZRNO':'사업자등록번호','CMPNY_NM':'회사명', 'GUBUN':'회원구분' }, inplace=True)
df.drop(['ID'], axis=1, inplace=True)

# 물질승인신청계획서와 통합, 승인유예고시가 제대로 적용됬는지 알기 위해
df = pd.merge(df, df_Company, how='left', left_on=['접수번호','고유번호','유형코드'], right_on=['RCT_NO','CAS_NO','ITEM_CD'])
df.loc[df.DEL_YN == 'N', 'DEL_YN'] = '승인유예고시'
df.loc[df.DEL_YN == 'Y', 'DEL_YN'] = '자진취하'
df.rename(columns={'DEL_YN':'물질신청서제출가능여부'},inplace=True)
df.drop(['RCT_NO','CAS_NO','ITEM_CD'], axis=1, inplace=True)

# 공동협의체와 통합
df = pd.merge(df, df_DPT, how='left', left_on=['고유번호','유형코드','사업자등록번호','신청인아이디'], right_on=['CAS_NO','USE_CODE','BIZ_NO','CREATE_ID'])
df.drop(['BIZ_NO','CREATE_ID','CAS_NO','USE_CODE'], axis=1, inplace=True)
df.rename(columns={'MST_ID':'공동협의체ID', 'GROUP_ROLE':'협의체 역할', 'AGENT_YN' : '선임번호', 'AGENT_NAME':'국외제조자', 'STS' : '협의체 상태'},inplace=True)
df['협의체 상태'].replace({'001':'구성중', '002':'투표중', '003':'구성완료'}, inplace=True)


print('=' * 50 + "기본정보 내보내기")
SU_Pandas_MO.SU_MO_To_excel(df, SU_Init.G_SU_ExFilePosOut + "승인유예고시기본정보.xlsx")


# ############################################ 분석2) 물질과 제품 유형별 업체 개수 등
print('=' * 50 + "물질별 유형별 그룹핑")
ndf = df.copy()
dfgroup = ndf.groupby(['고유번호', '살생물제품유형'])
toList  = []
exList  = ['고유번호', '살생물제품유형', '참여업체수', '참여업체명', '선임자','협의체 상태', '대표자']
toList.append(exList)
exList = []

for key, group in dfgroup:
    exList.append(key[0])       # 고유번호
    exList.append(key[1])       # 제푸뮤형

    # 참여업체수
    group1 = group.copy()
    group1.drop_duplicates(subset=['사업자등록번호'], inplace=True)
    exList.append(len(group1))

    # 참여업체명
    itemgroup = group1.loc[:, ['회사명', '사업자등록번호']]

    # 두개의 컬럼을 합칠때도 사용하면 된다. 숫자형 합칠때는 eval 이것을 사용하면 편하다.
    itemgroup['사업자등록번호'] = "(" + itemgroup['사업자등록번호'].map(str) + ")"

    # 이렇게도 가능하고
    # itemgroup['FULL'] = itemgroup['CN_NM'].str.cat(itemgroup['BIZ_NO'], sep = '')
    itemgroup['참여업체명'] = itemgroup[['회사명','사업자등록번호']].apply(''.join, axis = 1)


    aColList    = itemgroup.columns.tolist()
    aIndexList  = itemgroup.index.tolist()
    aValList    = itemgroup.values.tolist()
    strItemGroup=''

    # 결국 itemgroup은 회사명, 사업자등록번호, 참여업체명으로 구성된 데이터프레임
    # 참여업체명은 회사명과 사업자등록번호를 합친 형태로 새로 만들어준 컬럼이다.
    # 참여업체를 하나의 셀에 넣기 위해 합치는 작업을 한다.
    for iRow in range(0, len(aValList)):
        if len(strItemGroup) == 0:
            # 참여업체명을 담는다[2]
            strItemGroup = aValList[iRow][2]
        else:
            # 아래와 같이 \n 이렇게 해서 엑셀에서 포맷을 설정해야 한다.
            # 코딩으로 뭘 다할려고 하지 말고 내용에 충실해야 한다.
            strItemGroup = strItemGroup + "\n" + aValList[iRow][2]

    exList.append(strItemGroup)

    # 선임자
    group1 = group.copy()
    group1=group1.loc[:, ['선임자', '국외제조자']]
    group1.dropna(subset=['선임자'], how='any', inplace=True, axis=0)      # 선임자가 아닌 것 제외

    # 선임번호가 다르다는 것은 결국 국외제조자가 다르다는 것으로 선임번호 중복만 없애면 됨
    group1.drop_duplicates(subset=['선임자','국외제조자'], inplace=True)
    group1['선임자전체'] = group1['선임자'] + '(' + group1['국외제조자']+ ')'

    aColList        = group1.columns.tolist()
    aIndexList      = group1.index.tolist()
    aValList        = group1.values.tolist()
    strItemGroup    =''

    # 하나의 셀에 선임자를 담기 위해 선임자를 합친다.
    for iRow in range(0, len(aValList)):
        if len(strItemGroup) == 0:
            # 참여업체명을 담는다[2]
            strItemGroup = aValList[iRow][2]
        else:
            # 아래와 같이 \n 이렇게 해서 엑셀에서 포맷을 설정해야 한다.
            # 코딩으로 뭘 다할려고 하지 말고 내용에 충실해야 한다.
            strItemGroup = strItemGroup + "\n" + aValList[iRow][2]

    exList.append(strItemGroup)

    # 유형별 협의체 상태
    group1 = group.copy()
    strSts = group1['협의체 상태']

    # 유형별 상태는 동일하기 때문에 하나만 집어 넣어도 된다.
    if len(strSts) > 0:
        exList.append(strSts.iloc[0])
    else:
        print('-')
        exList.append('-')

    # 구성완료 인경우 대표자 추출
    group1 = group.copy()
    itemgroup=group1.loc[:, ['회사명', '신청인아이디', '사업자등록번호','협의체 역할']]
    aValList = itemgroup.values.tolist()

    strR = ''
    for iRow in range(0, len(aValList)):
        strR = aValList[iRow][3]
        if strR == '대표자':
            strR = aValList[iRow][0] +'(' + aValList[iRow][1] +',' + aValList[iRow][2] + ')'
            exList.append(strR)
            break

    toList.append(exList)
    exList = []

SU_Excel_MO.List_To_Excel(SU_Init.G_SU_ExFilePosOut + "승인유예고시통계.xlsx", "data", toList)