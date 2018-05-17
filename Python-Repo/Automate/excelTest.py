import openpyxl

workbook = openpyxl.load_workbook(r'G:\Pycode\Automate\example.xlsx')
print(type(workbook))
print(workbook.get_sheet_names())
sheet = workbook.get_sheet_by_name("Sheet1")
print(type(sheet))
cell = sheet['A1']
print(cell.value)
print(sheet['b4'].value)

print(sheet.cell(row=1, column = 2))
print(sheet['b1'].value)