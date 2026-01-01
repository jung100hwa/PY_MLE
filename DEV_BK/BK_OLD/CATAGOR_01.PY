import openpyxl as op

# wb = op.load_workbook('CA_01.xlsx')
# ws = wb.worksheets[0]

# # 전치 카테고리 리스트
# cdlist = []


# # BK3.0에 있는 전시카테고리
# for rowitem in range(2, ws.max_row + 1):
#     strca  = str(ws.cell(row=rowitem, column=9).value).strip()
#     if strca != "None":
#         cdlist.append(strca)
#     print(str(rowitem) + '-------->' + strca)
    
# wb.save('CA_01.xlsx')
# wb.close()
    
# wb = op.load_workbook('CA_02.xlsx')
# ws = wb.worksheets[0]

# # 맵핑테이블에만 있는 것
# for rowitem in range(2, ws.max_row + 1):
#     strca  = str(ws.cell(row=rowitem, column=2).value).strip()
    
#     if strca != "None":
#         cacount = cdlist.count(strca)
#         if cacount >= 1:
#             ws.cell(row=rowitem, column=1, value='0')
#         else:
#             ws.cell(row=rowitem, column=1, value='1')
#     else:
#         ws.cell(row=rowitem, column=1, value='0')
        
#     print(str(rowitem) + '-------->' + strca)
    
# wb.save('CA_02.xlsx')
# wb.close()


#########################################################################

# wb = op.load_workbook('CA_02.xlsx')
# ws = wb.worksheets[0]
# # 전치 카테고리 리스트
# cdlist = []

# # 맵핑테이블에 있는 전시카테고리
# for rowitem in range(2, ws.max_row + 1):
#     strca  = str(ws.cell(row=rowitem, column=2).value).strip()
#     if strca != "None":
#         cdlist.append(strca)
#     print(str(rowitem) + '-------->' + strca)
    
# wb.save('CA_02.xlsx')
# wb.close()


# wb = op.load_workbook('CA_01.xlsx')
# ws = wb.worksheets[0]

# # bk3.0에만 있는 것
# for rowitem in range(2, ws.max_row + 1):
#     strca  = str(ws.cell(row=rowitem, column=9).value).strip()
    
#     if strca != "None":
#         cacount = cdlist.count(strca)
#         if cacount >= 1:
#             ws.cell(row=rowitem, column=10, value='0')
#         else:
#             ws.cell(row=rowitem, column=10, value='1')
#     else:
#         ws.cell(row=rowitem, column=10, value='0')
        
#     print(str(rowitem) + '-------->' + strca)
    
# wb.save('CA_01.xlsx')
# wb.close()


#########################################################################
# bk3.0과 맵핑테이블에 동시에 전시카테고리 번호가 있으면서 hscode가 다른것
wb = op.load_workbook('CA_02.xlsx')
ws = wb.worksheets[0]

cdlist = []

for rowitem in range(2, ws.max_row + 1):
    strca  = str(ws.cell(row=rowitem, column=2).value).strip()
    strhs  = str(ws.cell(row=rowitem, column=15).value).strip()
    if strca != "None" and strhs != "None":
        hsList = strhs.split(",")
        
        for item in range(0,len(hsList)):
            strhs = str(hsList[item]).strip()
            cdlist.append(strca + strhs)
            print(str(rowitem) + '-------->' + strca + strhs)
    
wb.save('CA_02.xlsx')
wb.close()



wb = op.load_workbook('CA_01.xlsx')
ws = wb.worksheets[0]


# bk3.0에만 있는 것
for rowitem in range(2, ws.max_row + 1):
    strca  = str(ws.cell(row=rowitem, column=9).value).strip()
    strhs  = str(ws.cell(row=rowitem, column=8).value).strip()
    
    if strca != "None" and strhs != "None":
        strca = strca + strhs
        cacount = cdlist.count(strca)
        if cacount >= 1:
            ws.cell(row=rowitem, column=11, value='0')
        else:
            ws.cell(row=rowitem, column=11, value='1')
    else:
        ws.cell(row=rowitem, column=11, value='0')
        
    print(str(rowitem) + '-------->' + strca)
    
    
wb.save('CA_01.xlsx')
wb.close()