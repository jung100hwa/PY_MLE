import sys
sys.path.append("c:\\work\\PLangVim")

import pandas as pd
import seaborn as sns
import os
import platform
import numpy as np
import PY_PKG.SU_ALLMO_Init_MO as SU_ALLMO_Init_MO

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width',True)

############################################ 2개의 데이터프레임을 비교해서 없는 것만 다시 데이터프레임으로 반환
# df_01 : 기준이 되는 데이터프레임
# df_02 : 기준이 되는 데이터프레임에서 마이너스를 할 데이터프레임
# df_01 - df_02에서 남은 값만 데이터프레임으로 바꾸어서 리턴
def SU_MO_ReturnDfSubDf(df_1, df_2):
    
    # 정확한 비교를 위해 데이터 정제를 한다. np.nan 즉 널값끼리는 비교가 되지 않는다.
    # 빈값을 널처리후 적당한 값으로 치환한다. in, not in 이런 함수는 널값(nan)끼리는 비교되지 않는다.
    df_1 = df_1.replace('',np.nan)
    df_1 = df_1.fillna('###')
    df_2 = df_2.replace('',np.nan)
    df_2 = df_2.fillna('###')
    
    df1_list = df_1.values.tolist()
    df2_list = df_2.values.tolist()

    df_list = []

    for item in df1_list:
        if item not in df2_list:
            df_list.append(item)
            
    df = SU_MO_ReturnFromListToDF(df_list, None, list(df_1.columns))
    df = df.replace("###",'')
    
    return df


############################################ 디셔너리 데이터와 좌측 인덱스를 받아서 데이터프레임을 생성
# vindex : 좌측 열인덱스로 사용할 리스트
def SU_MO_ReturnFromColletionToDF(vdir, vindex):
    df = pd.DataFrame(vdir, index = vindex)
    return df

############################################ 리스트를 좌측 인덱스를 받아서 데이터프레임을 생성
# vindex : 좌측 열인덱스로 사용할 리스트
# vcolumn : 컬럼명으로 사용할 리스트
def SU_MO_ReturnFromListToDF(vdir, vindex, vcolumn):
    df = pd.DataFrame(vdir, index = vindex, columns=vcolumn)
    return df


############################################ 튜플를 좌측 인덱스를 받아서 데이터프레임을 생성
# vindex : 좌측 열인덱스로 사용할 리스트
# vcolumn : 컬럼명으로 사용할 리스트
def SU_MO_ReturnFromTupleToDF(vdir, vindex,vcolumn):
    df = pd.DataFrame(vdir, index = vindex, columns=vcolumn)
    return df


############################################ csv파일을 데이터프레임으로 변환
# vfilename : csv 파일명
# vheader : 헤더로 사용할 행번호(0부터 시작)
# vindex_col : 행인덱스로 사용할 열번호(false부터네. 짜증)
def SU_MO_ReturnRead_csv(vfilename, vheader, vindex_col):
    if vindex_col == 0:
        vindex_col = False

    df = pd.read_csv(vfilename, header=vheader, index_col=vindex_col)
    return df


############################################ 엑셀파일을 데이터프레임으로 변환
# vfilename : 엑셀 파일명
# vheader : 헤더로 사용할 행번호(0부터 시작)
# vindex_col : 행인덱스로 사용할 열번호(false부터네. 짜증)
def SU_MO_ReturnRead_excel(vfilename, vheader=0, vindex_col=False):
    df = pd.read_excel(vfilename, header=vheader, index_col=vindex_col)
    return df

############################################ 엑셀파일을 데이터프레임으로 변환하되 모두 문자열 형식으로 가져오기
# vfilename   : 엑셀 파일명
# vheader     : 헤더로 사용할 행번호(0부터 시작)
# vindex_col  : 행인덱스로 사용할 열번호(false부터네.). 0이면 첫번째 컬럼을 인덱스로 사용한다는 의미, false이면 인덱스 컬럼을 만든다.
# strSelect    : 엑셀의 모든 값을 문자로 취급해서 불러올지 결정(0-엑셀자체, 1-엑셀의 모든 값을 문자열로 불러온다.
# 만약에 엑셀에 00값이 있는데 그냥 변경하면 0으로 자동 변환된다.
def SU_MO_ReturnRead_excel2(vfilename, vheader=0, vindex_col=False, strSelect=0):
    
    if strSelect == 1:
        column_list = []
        df_column = pd.read_excel(vfilename).columns
        for i in df_column:
            column_list.append(i)
        converter = {col: str for col in column_list} 
        df = pd.read_excel(vfilename, header=vheader, index_col=vindex_col, converters=converter)
        return df
    else:
        df = pd.read_excel(vfilename, header=vheader, index_col=vindex_col)
        return df


############################################ 오라클 쿼리 결과를 데이터프레임으로 변환
# vsql : 쿼리명
# vconn : connection 객체
def SU_MO_ReturnRead_sql(vsql, vconn):
    df = pd.read_sql(vsql, vconn)
    return df


############################################ 오라클 쿼리 결과를 데이터프레임으로 변환
# vsql : 쿼리명
# vconn : connection 객체
def SU_MO_ReturnRead_sql2(vsql, vengine):
    df = pd.read_sql_query(vsql, vengine)
    return df


############################################ 데이터 프레임을 csv 파일로 내보내기
# vdf       : 데이터프레임
# vfileanme : 내보낼 파일명(완전한 경로)
def SU_MO_To_csv(vdf, vfilename):
    vdf.to_csv(vfilename)

############################################ 데이터 프레임을 excel로 내보내기
# vdf       : 데이터프레임
# vfileanme : 내보낼 파일명(완전한 경로)
def SU_MO_To_excel(vdf, vfilename):
    vdf.to_excel(vfilename)


############################################ 하나의 엑셀 파일에 여러 시트로 만들기
# vfilename     : 엑셀파일명
# vList         : 엑셀 시트로 추가하고자 하는 데이터프페임 리스트
def SU_MO_TO_excelMuli(vfilename, vList):
    count = 1
    strDf = "DataFrame" + str(count)
    writer = pd.ExcelWriter(vfilename)

    for key in range(0, len(vList)):
        vList[key].to_excel(writer, sheet_name = strDf)
        count = count + 1
        strDf = "DataFrame" + str(count)
    writer.save()


############################################ 오라클에 데이터프레임을 통째로 넣기
# 일반적으로 이렇게 하는 것보다 전문 툴을 이용하는게 낫다.
# vdf       : 데이터프레임
# vtable    : 테이블명
# vengine   : 엔진명 cx_Oracle은 오류가 남. 그래서 sqlalchemy를 임포트애서 넘겨줌
# 데이터 프레임에 인덱스를 사용하지 않기 때문에 즉 데이터베이스에 있는 컬럼만 사용하기 위해 index : False 
# voption : 1-테이블이 있으면 데이터를삭제하고 시작, 2-테이블 추가만
def SU_MO_To_Sql(vdf, vtable, vengine, voption, vconn):
    # 기존 데이터를 삭제하고
    if voption == 1:
        cursor = vconn.cursor()
        cursor.execute("DELETE FROM " + vtable)
        vconn.commit()

    voption = "append"
    
    vdf.to_sql(vtable,con=vengine, index= False, if_exists=voption)


############################################ 데이터프레임을 받아서 조건에 맞게 정렬한 후 리턴
# vdf : 데이터프레임 원본
# vsortlist : 정렬기준 리스트. 순차적으로
# vascending : 오름차순 True, 내림차순 False
def SU_MO_DataframeSort(vdf, vsortlist, vascending):
    df = vdf.sort_values(vsortlist, ascending=vascending)
    return df


############################################ 데이터프레임을 오라클 테이블에 직접 넣기
# vdf       : 데이터프레임
# vconn     : 커넥션 객체
# vtable    : 인서트 대상 테입블
# vView     : 0-진행사항 보지 않음, 1-진행사항을 봄
# 모든 컬럼이 varchar2를 가정해서 만듬
def SU_MO_DfOracleInsert(vdf, vconn, vtable, vView):
    rowList = vdf.shape[0]
    colList = vdf.shape[1]

    strSql = "INSERT INTO " + vtable + " values("
    for irow in range(0, rowList):
        for icol in range(0, colList):

            # 값처리를 한다.
            strv = str(vdf.iloc[irow, icol])
            strv = strv.replace("'", "' || chr(39) || '")
            if len(strv) > 0:
                if strv.upper() == 'NAN':
                    strv = ''

            strSql = strSql + "'" + strv + "',"

        strSql = strSql[0:-1] + ")"
        cursor=vconn.cursor()
        cursor.execute(strSql)
        strSql="INSERT INTO " + vtable + " values("

        if vView == 1:
            print(str(irow+1) + " row insert")

    vconn.commit()