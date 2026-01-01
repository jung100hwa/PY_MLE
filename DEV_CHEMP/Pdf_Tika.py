# tika는 아파치 재단에서 하는 것으로 별도 웹서버가 가동되어야 함
# 개인적으로 환경이 제대로만 갖춰진다면 표를 제외학 이게 최고 인듯

from tika import parser
import os, shutil
import platform
import time
import schedule

strFirst = os.getcwd()
strSplitDef =''

# 현재의 플랫폼을 정보 구하기
strPlatform = platform.system()

if strPlatform == 'Windows':
    strOrg = strFirst + '\\IDT\\PDF\\'              # 최초 PDF 저장되는 장소
    strExt = 'PDF'                                  # 확장자(PDF만 가능)
    strRead = strFirst + '\\IDT\\PDF_READ\\'        # PDF 성공적으로 읽은 파일 이동
    strError = strFirst + '\\IDT\\PDF_ERROR\\'      # PDF 오류 항목
    strSplitDef = '\\'
else:
    strOrg = strFirst + '/PDF/'
    strExt = 'PDF'
    strRead = strFirst + '/PDF_READ/'
    strError = strFirst + '/PDF_ERROR/'
    strSplitDef = '/'

# 년도 맞추기
def YMD(strImsi):

    strImsi = strImsi.replace(' ','')

    iY = strImsi.find('년')
    strY = strImsi[:iY]

    iM = strImsi.find('월')
    strM = strImsi[iY + 1:iM]
    if len(strM) == 1:
        strM = '0' + strM

    iD = strImsi.find('일')
    strD = strImsi[iM + 1:iD]
    if len(strD) == 1:
        strD = '0' + strD

    return strY + '-' + strM + '-' + strD

# 법인등록번호와 사업자등록번호 구분
def RawBusNum(strImsi):
    strRaw = '' # 법인등록번호
    strBus = '' # 사업자등록번호
    strImsi = strImsi.replace(' ','')
    strI = strImsi.find('(')

    if strI > 0:
        strI2 = strImsi.find(')')
        strImsi2 = strImsi[strI + 1 : strI2]
        strImsi = strImsi[:strI]
        strImsi = strImsi.replace('-','')
        strImsi2 = strImsi2.replace('-','')

        if len(strImsi) == 10:
            strRaw = strImsi
            strBus = strImsi2

    else:
        strImsi = strImsi.replace('-','')
        if len(strImsi) == 10:
            strRaw = ''
            strBus = strImsi
        else:
            strRaw = strImsi
            strBus = ''

    return strRaw, strBus




# 키에 해당하는 값을 찾는다.
def findnextkey(strList, strTitle, count):
    cnt = 0
    strList2 = strList[:]
    returnList = []
    strTitle = strTitle.replace(' ','')

    for item in strList2[count:]:
        item2 = item.replace(' ','')

        if strTitle not in item2:
            if cnt == 0:
                returnList.append(item)
            else:
                returnList.append('\n' + item)
            cnt += 1
        else:
            break

    return ''.join(returnList).strip()


def dirsearch(strOrgdir, strExt):
    try:
        dirname = os.listdir(strOrgdir) # 리스트 형식으로 리턴
        if len(dirname) >= 1 :
            for fname in dirname:

                full_fname = os.path.join(strOrgdir, fname)

                # 만약에 디렉토리이면 자기참조
                if os.path.isdir(full_fname):

                    # 디렉토리 안에 파일이 존재하면
                    for root, dirs, files in os.walk(full_fname):
                        if files:
                            dirsearch(full_fname, strExt)
                        else:
                            shutil.rmtree(full_fname)

                else:
                    if len(full_fname) > 0:

                        # 확장자를 검색해서 PDF 이면 수행
                        if (os.path.splitext((full_fname))[-1]).upper() == "." + strExt:

                            raw_pdf = parser.from_file(full_fname)
                            strContent = raw_pdf['content']

                            strContentImsi = strContent.replace('\n','')

                            # PDF 콘텐츠가 있으면 수행. 없으면 오류(일반적으로 오류는 확장자만 PDF인 경우가 많다.)
                            if strContent and len(strContentImsi) > 200: # pdf read

                                strContent = strContent.strip()

                                # DB에 인서트, 전체 내용을 읽는다.
                                print(strContent)

                                aValueD = {} # PDF 값을 딕셔너리에 담는다.
                                strContent = strContent.replace('\n\n','\n')
                                strContent = strContent.split('\n')
                                count = 0

                                for valueItem in strContent:
                                    valueItem = valueItem.strip()
                                    count = count + 1

                                    if valueItem.replace(' ', '') == '발행번호':
                                        strImsi = strContent[count]
                                        aValueD['발행번호'] = strImsi.replace('-', '').replace(' ', '')

                                    if valueItem.replace(' ', '') == '접수번호':
                                        strImsi = strContent[count]
                                        aValueD['접수번호'] = strImsi.replace('-', '').replace(' ', '')

                                    if valueItem.replace(' ', '') == '확인완료일':
                                        strImsi = strContent[count]
                                        aValueD['확인완료일'] = YMD(strImsi)

                                    if valueItem.replace(' ', '') == '접수연월일':
                                        strImsi = strContent[count]
                                        aValueD['접수연월일'] = YMD(strImsi)

                                    if valueItem.replace(' ','') =='상호(명칭)':
                                        strImsi = findnextkey(strContent, '법인등록번호(사업자등록번호)', count)
                                        aValueD['상호(명칭)'] = strImsi.strip()

                                    if valueItem == '법인등록번호(사업자등록번호)':
                                        strImsi = strContent[count]
                                        strRaw, strBus = RawBusNum(strImsi)

                                        if len(strRaw)  == 13:
                                            aValueD['법인등록번호'] = strRaw

                                        if len(strBus) == 10:
                                            aValueD['사업자등록번호'] = strBus

                                    if valueItem.replace(' ', '') == '성명(대표자)':
                                        strImsi = findnextkey(strContent, '담당자성명및연락처', count)
                                        aValueD['성명(대표자)'] = strImsi.replace('-', '')

                                    if valueItem.replace(' ','') =='담당자성명및연락처':
                                        strImsi = strContent[count]
                                        strImsiindex = strImsi.find('전화번호:')
                                        strImsiname = strImsi[0:int(strImsiindex)].replace('담당자:', '').replace(' ', '')
                                        strImsitel = strImsi.replace('담당자:', '').replace('전화번호:', '').replace(strImsiname, '').replace(' ', '')
                                        aValueD['담당자'] = strImsiname
                                        aValueD['담당자전화번호'] = strImsitel

                                    if '(전자우편:' in valueItem.replace(' ',''):
                                        strImsi = valueItem.replace('(전자우편:','').replace(')','').replace(' ','')
                                        aValueD['전자우편'] = strImsi

                                    if valueItem.replace(' ', '') =='소재지(사업장)':
                                        strImsi = strContent[count]

                                        if '(전화번호:' in strImsi:
                                            strImsiindex = strImsi.find('(전화번호:')
                                            strImsijuso = strImsi[0:int(strImsiindex)].strip()
                                            strImsitel = strImsi[strImsiindex:].strip()
                                            strImsitel = strImsitel.replace('(전화번호:','').replace(')','').replace(' ','')
                                            aValueD['소재지(사업장)'] = strImsijuso.strip()
                                            aValueD['사업장전화번호'] = strImsitel
                                        else:
                                            aValueD['소재지(사업장)'] = strImsi.strip()

                                    if '(팩스번호:' in valueItem.replace(' ',''):
                                        strImsi = valueItem.replace('(팩스번호:', '').replace(')','').replace(' ','')
                                        aValueD['팩스번호'] = strImsi

                                    if '제조ㆍ수입' in valueItem.replace(' ', ''):
                                        if '제조ㆍ수입[○]제조[ ]수입' in valueItem.replace(' ',''):
                                            aValueD['제조수입'] = '제조'
                                        else:
                                            aValueD['제조수입'] = '수입'

                                    if valueItem.replace(' ','') == '품목':
                                        strImsi = findnextkey(strContent, '제품명', count)
                                        aValueD['품목'] = strImsi.strip()

                                    if valueItem.replace(' ','') == '제품명':
                                        strImsi = findnextkey(strContent, '용도', count)
                                        aValueD['제품명'] = strImsi.strip()

                                    if valueItem.replace(' ','') == '용도':
                                        strImsi = findnextkey(strContent, '제형', count)
                                        aValueD['용도'] = strImsi.replace('\n','')

                                    if valueItem.replace(' ', '') == '제형':
                                        strImsi = findnextkey(strContent, '중량ㆍ용량ㆍ매수', count)
                                        aValueD['제형'] = strImsi.strip()

                                    if valueItem.replace(' ', '')== '중량ㆍ용량ㆍ매수':
                                        strImsi = findnextkey(strContent, '제조국명', count)
                                        aValueD['중량ㆍ용량ㆍ매수'] = strImsi.strip()

                                    if valueItem.replace(' ', '') == '제조국명':
                                        strImsi = strContent[count]
                                        aValueD['제조국명'] = strImsi.strip()

                                    if valueItem.replace(' ', '') == '제조회사명':
                                        strImsi = findnextkey(strContent, '확인결과', count)
                                        aValueD['제조회사명'] = strImsi.replace('\n', '')

                                    if '[○]적합' in valueItem.replace(' ', ''):
                                        aValueD['확인결과'] = '적합'
                                        
                                    if '[]적합' in valueItem.replace(' ', ''):
                                        aValueD['확인결과'] = '부적합'

                                    if '확인성적서 유효기간:' in valueItem:
                                        strImsi = valueItem.replace('확인성적서 유효기간:','').replace(' ','')
                                        strindex = strImsi.find('~')
                                        strbdate = strImsi[0:int(strindex)].strip()
                                        stredate = strImsi[int(strindex)+1:].strip()

                                        aValueD['확인성적서유효기간 시작일'] = YMD(strbdate)
                                        aValueD['확인성적서유효기간 종료일'] = YMD(stredate)

                                    if valueItem == '한 국 환 경 산 업 기 술 원 장':
                                        strImsi = strContent[count-2]
                                        strImsi = strImsi.replace(' ','')
                                        aValueD['발급일자'] = YMD(strImsi)

                                        
                                print(aValueD)


                            #     # create directory
                            #     strSplitFilename = os.path.basename(full_fname)

                            #     # 디렉토리가 존재하지 않으면 만들고
                            #     if not (os.path.isdir(strRead)):
                            #         os.makedirs(strRead)

                            #     # strSplitDef 이것은 OS에 따른 분리자
                            #     strCreateRead = strRead + strSplitDef + strSplitFilename
                            #     # shutil.move(full_fname, strCreateRead)

                            # else:
                            #     # create directory
                            #     strSplitFilenameError = os.path.basename(full_fname)

                            #     # 디렉토리가 존재하지 않으면 만들고
                            #     if not (os.path.isdir(strError)):
                            #         os.makedirs(strError)

                            #     # strSplitDef 이것은 OS에 따른 분리자
                            #     strCreateRead = strError + strSplitDef + strSplitFilenameError
                            #     shutil.move(full_fname, strCreateRead)
        else:
            print("==========> not file exist")
    except PermissionError:
        print("==========> file error")
        pass

# # schedule.every().monday.at("00:10").do(dirsearch) #월요일 00:10분에 실행
# # schedule.every().day.at("10:30").do(dirsearch) #매일 10시30분에
# # schedule.every().day.at("10:30").do(dirsearch) #매일 10시30분에
# schedule.every(10).seconds.do(dirsearch,strOrg, strExt) # 10초에 한번씩
# # schedule.every(10).minutes.do(dirsearch) # 10분에 한번씩



# 스케줄러에 등록(10초에 한번씩)
# schedule.every(10).seconds.do(dirsearch,strOrg, strExt)
#
# if __name__ == "__main__":
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

dirsearch(strOrg, strExt)

