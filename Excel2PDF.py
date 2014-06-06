import win32com.client

def Excel2PDF(excelPath, pdfPath):
    xl = win32com.client.Dispatch("Excel.Application")
    wb = xl.Workbooks.Open(Filename=excelPath,ReadOnly=1)
    wb.ExportAsFixedFormat(0, pdfPath)
    xl.Application.Quit()
    del xl

excelPath = "D:\Desktop\P24612_E Inspection Standard.xlsx"
pdfPath = "D:\Desktop\Test.pdf"

Excel2PDF(excelPath, pdfPath)