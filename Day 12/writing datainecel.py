import openpyxl
# writing same data
file = "D:\Book1.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet1"]

for r in range(1,8):
    for c in range(1,5):
        sheet.cell(r,c).value="welcome"
workbook.save(file)
