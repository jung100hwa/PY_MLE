from pypdf import PdfReader

# 파이참은 원래 프로젝트 경로, 하위 폴더에 있는 파일 경로를 PATH로 자동 등록하는데 아래 함수는 조금 다르네.
# 원노트 참조. 함수마다 다른가 보네
# reader = PdfReader('./E_FILE/sample.pdf')
reader = PdfReader('sample.pdf')

pagecontext = []
pagecount = len(reader.pages)

for i in range(pagecount):
    page = reader.pages[i]
    pagecontext.append(page.extract_text(0, 90))

print(pagecontext)