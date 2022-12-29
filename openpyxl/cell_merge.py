from openpyxl import load_workbook

wb = load_workbook(filename='excels/cells.xlsx')
sheet_name = wb.sheetnames[0]

ws1 = wb[sheet_name]
ws1.merge_cells('A5:B7')
ws1['A5'] = 'test'

wb.save('excels/cells.xlsx')