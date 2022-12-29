from openpyxl import Workbook
from openpyxl.styles import Font

# ワークブックオブジェクトを作成
wb = Workbook()
# ワークシートオブジェクトを作成
ws = wb.active
ws['A4'] = 10
cel = ws['A4']
# セルのフォントを設定
cel.font = Font(size=12, bold=True, color='FF0000')
# ファイルを保存
wb.save('excels/new.xlsx')