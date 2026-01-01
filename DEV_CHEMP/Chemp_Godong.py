# 승인고시된 항목 전체 검사

import cx_Oracle
import openpyxl as op
import time, os

strTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 오라클 연결
# 다이퀘스트
# os.putenv('NLS_LANG', '.UTF8')
# connection = cx_Oracle.connect('chemp/chemp@133.186.171.48:42521/orcl')
# cursor = connection.cursor()

# 기술원 개발서버
os.putenv('NLS_LANG', '.UTF8')
connection = cx_Oracle.connect('chemp/chemp@192.168.50.60:1521/orcl')
cursor = connection.cursor()

# 기술원 운영서버
# os.putenv('NLS_LANG', '.UTF8')
# connection = cx_Oracle.connect('chemp/chemp!1299@10.10.20.10:1521/chemp')
# cursor = connection.cursor()

chdirpath = os.getcwd()
os.chdir(chdirpath)


# 1. 물질협의체가 없는 것 조회해서 무조건 하나는 만든다.
notExistMn = {}
cursor.execute("""SELECT DISTINCT CAS_NO, MATERIAL_NM FROM TN_EBM_COOPERATION_T WHERE CAS_NO 
NOT IN(SELECT CAS_NO FROM TN_EBM_COOPERATION_T WHERE CATEGORY = 'M' AND CAS_NO IS NOT NULL)""")

for name in cursor:
    notExistMn[str(name[0])] = str(name[1])

for item in notExistMn.keys():
    strCasno = item
    strMaterial = notExistMn[strCasno]

    # 여기서 한번 찍어 본다.
    print(strCasno, strMaterial)

    strMaterial = strMaterial.replace("'","' || chr(39) || '")

    strSeq = """'TEC_' || LPAD(SEQ_EBM_COOPERATION_01.NEXTVAL,7,'0')"""

    cursor.execute("""INSERT INTO TN_EBM_COOPERATION_T(MST_ID, CAS_NO, MATERIAL_NM, USE_CODE, PARTICIPANT_COUNT, STS, CATEGORY,CREATE_DATE,
    CREATE_ID, UPDATE_DATE, UPDATE_ID) VALUES(%s,'%s','%s','%s','%s','%s','%s',to_date('%s','YYYY-MM-DD'),'%s',to_date('%s','YYYY-MM-DD'),'%s')"""
                   % (strSeq, strCasno, strMaterial, '000', '0', '001', 'M', strTime, 'SYSTEM', strTime, 'SYSTEM'))
    connection.commit()
print("물질협의체가 존재하지 않는 것 생성 완료")


# 2. 구성원수 업데이트 
cursor.execute("""UPDATE TN_EBM_COOPERATION_T TA SET PARTICIPANT_COUNT =(SELECT COUNT(*) FROM TN_EBM_COOPERATION_MAP_T WHERE 
	((GROUP_ROLE, APPROVE_YN) NOT IN (('008', 'Y'))) AND MST_ID = TA.MST_ID)""")
connection.commit()
print("탈퇴한 업체를 제외한 구성원수가 업데이트 완료")



# 3. 구성원수가 0인것 삭제
cursor.execute("""DELETE FROM TN_EBM_COOPERATION_T WHERE PARTICIPANT_COUNT=0""")
connection.commit()
print("물질협의체 구성원수가 0인것 삭제")
