# 한국환경산업기술원 프로젝트 행공센 연계 파일 읽기

from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
import xml.etree.ElementTree as ET
from SU_MO import SU_Init
from SU_MO import SU_Pandas_MO
from SU_MO import SU_Excel_MO

SU_Init.SU_MO_VarInit()

# 이 함수는 보기 좋게 정렬한다.
def Indent(elem, level = 0):
    i = "\n" + level* " "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            Indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# 파일에서 읽어오기
XMLTree = ET.parse(SU_Init.G_SU_ExFilePosIn + 'M2021010119400410003250.xml')
XMLRoot= XMLTree.getroot()


# 태크명을 구할 수 있다.
# print(XMLRoot.tag)

# Indent(root)
# dump(root)

#
# print("========xml 속성값 읽어 오기=========")
# # title
# title = root.find("header")
# print(title.findtext("title"))
# print(title.findtext("G4BSequenceM"))
#
# items = root.find("items")
# item  = items.find("item")
# print(item.findtext("G4BSequenceS"))
# print(item.findtext("productDocumentClassificationCode"))
# print(item.findtext("institutionCode"))
# print(item.findtext("certificationKindCode"))
# print(item.findtext("certificationName"))
# print(item.findtext("sploreNm"))
# print(item.findtext("insttNm"))
# print(item.findtext("productDocumentConditionCode"))
# print(item.findtext("productDocumentConditionDetailContents"))
# print(item.findtext("publicationDate"))
# print(item.findtext("validityStartDate"))
# print(item.findtext("validityEndDate"))
# print(item.findtext("bizrnoNo"))
# print(item.findtext("jurirnoNo"))
# print(item.findtext("entprsNm"))
# print(item.findtext("rprsntvNm"))
# print(item.findtext("fcltsKndCode"))
# print(item.findtext("testGradCode"))
# print(item.findtext("mxmmMdfcDstnc"))
# print(item.findtext("brdngColsnVe"))
# print(item.findtext("brdngAc"))
# print(item.findtext("linkConditionCode"))
# print(item.findtext("linkConditionDetailContents"))
# print(item.findtext("pblicteNo"))
# print(item.findtext("reisuPblicteNo"))
# print(item.findtext("testRceptNo"))

# attachFiles  = item.find("attachFiles")
#
# # 동일하게 반복될때는 아래와 같이
# fileInfo  = attachFiles.find("fileInfo")
# for file in fileInfo:
#     print(fileInfo.findtext("G4BSequenceF"))
#     print(fileInfo.findtext("orginalFileName"))
#     print(fileInfo.findtext("convertedFileName"))

