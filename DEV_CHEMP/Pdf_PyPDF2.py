import PyPDF2
import SU_Init as SU_Init
import pikepdf

SU_Init.SU_MO_VarInit(1)

pdfFileObj = open(SU_Init.G_SU_ExFilePosIn + "testpdf.pdf", 'rb')

# # create a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracte text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()

