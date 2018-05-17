import openpyxl
wb = openpyxl.Workbook()
#print(type(wb))
print(len(wb.worksheets))
print(list(wb.worksheets))
sheet = wb.worksheets[0]
print(sheet['a1'].value == None)

#Assign value
sheet['a1'] = 42
sheet['a2'] = "Anurag"

#os.chdir(r"C:\Users\anura\Documents")  change current working directory
wb.save(r"G:\Pycode\Automate\example2.xlsx")
sheet2 = wb.create_sheet(title="StudentRecords",index=0)
print(list(wb.worksheets))
#print(wb.get_sheet_names())
sheet2.title = "TeacherRecords"
wb.save(r"G:\Pycode\Automate\example2.xlsx")
