import win32com.client

def Excel2PDF(excelPath, pdfPath):
    xl = win32com.client.Dispatch("Excel.Application")
    wb = xl.Workbooks.Open(Filename=excelPath,ReadOnly=1)
    print pdfPath
    wb.ExportAsFixedFormat(0, str(pdfPath))
    xl.Application.Quit()
    del xl