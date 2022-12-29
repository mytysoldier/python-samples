from openpyxl import load_workbook

wb = load_workbook('excels/row_col.xlsx')

sheet_name = wb.sheetnames[0]
ws1 = wb[sheet_name]
ws1.insert_cols(2, 3)
ws1.delete_rows(5)
wb.save('excels/row_col.xlsx')