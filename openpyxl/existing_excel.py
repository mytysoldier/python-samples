from openpyxl import load_workbook

wb = load_workbook(filename='excels/existing.xlsx')
# そのワークブックのシート名のリストを取得
sheet_names = wb.sheetnames
print(sheet_names)

sheet_name = sheet_names[0]
ws1 = wb[sheet_name]
x = ws1['A4'].value

ws2 = wb.create_sheet('new sheet')
ws2['A1'] = x
wb.save('excels/existing.xlsx')