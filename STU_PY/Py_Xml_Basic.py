from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
import xml.etree.ElementTree as ET

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

# 루트 엘리먼트 생성
# note = Element("note")
# note.attrib["date"] = "20200930"

# 이렇게 해도 됨
note = Element("note", date = "20201107")

# 서브 엘리먼트 추가
SubElement(note, "to").text = "Tove"
SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!!"

# 생성하여 append 해도 됨
app = Element("append")
app.text = "byby"
note.append(app)


# 정렬
Indent(note)

# 화면에 표시
dump(note)

# 파일로 쓰기
ElementTree(note).write("note.xml")

# 속성값 읽기
print(note.get("date"))
print(note.keys())
print(note.items())

# 파일에서 읽어오기
print("========파일로 부터 읽기=========")
tree = ET.parse('note.xml')
root = tree.getroot()
Indent(root)
dump(root)
