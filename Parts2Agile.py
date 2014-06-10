"""Script to merge a range of inspection standards
Input:
    Directory of parts and inspection standards
    Page where inspection standards should start
Output
    Each part drawing is merged with the corresponding inspection standard
"""

from PyPDF2 import PdfFileMerger
import os
import re
import sys
import zipfile
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#Runs Program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QFileDialog()
    dialog.exec_()

inputPath = "D:\\Desktop\\Test ECO\\"
#inputPath = raw_input("What is the inputPathectory?") #Assumes both part drawings and inspection standards are in the same directory
startPage = 1
#startPage = int(raw_input("Which page should the inspection standard start after? "))

outputPath = "%sOutput\\" % inputPath #Directory to place all the processed files (defaults to an output folder inside the input path

if not os.path.exists(outputPath): #Checks to see if output directory exists and makes it if it does not
    os.makedirs(outputPath)

partPdfFilenameArray = [] #Storage for the part filenames
inspPdfFilenameArray = [] #Storage for the inspection standard pdf file names
inspExlFilenameArray = [] #Storage for the inspection standard excel file names
partIgsFilenameArray = [] #Storage for the part IGES file names
outPdfFilenameArray = [] #Location of output for combined Pdfs

expression = 'P\d+_\D'
#Matches only part numbers at the beginning of the string
#'P' Must start with P
#'\d' Matches 1 or more decimal digits
#'_' Matches underscore
#'\D' Matches any nondigit character

for filename in os.listdir(inputPath):
    root, ext = os.path.splitext(filename)

    if re.match(expression, root):  #Checks to see that it starts with the expected part number and rev
        if ext == ".pdf": #Collects all PDFs
            if ("Inspection Standard" in root): #Picks inspection standard out of file names
                inspPdfFilenameArray.append(inputPath + filename)
            else:   #Picks part out of file names
                partPdfFilenameArray.append(inputPath + filename)
        elif ext == ".xlsx" or ext == ".xls":
            inspExlFilenameArray.append(inputPath + filename)
        elif ext == ".igs" or ext == ".iges":
            partIgsFilenameArray.append(inputPath + filename)

#Cycles through the both the inspection standards and parts to find a match
for partPath in partPdfFilenameArray:
    for inspPath in inspPdfFilenameArray:
        part = os.path.split(partPath)[1]
        insp = os.path.split(inspPath)[1]
        if part[:8] == insp[:8]: #Matches part and rev to merge
            merger = PdfFileMerger()

            partPDF = open(partPath, "rb")
            inspPDF = open(inspPath, "rb")

            merger.append(fileobj=partPDF, pages=(0,startPage))
            merger.append(fileobj=inspPDF)

            outPdfFilename = "%s%s.pdf" %(outputPath, part[:8])

            outPdfFilenameArray.append(outPdfFilename)

            output = open(outPdfFilename, "wb")
            merger.write(output)
            print "Merged %s and %s" %(part, insp)

#Finds the matching part drawing, inspection standard, and IGES file and merges together in a zip file
for partPath in outPdfFilenameArray:
    for excelPath in inspExlFilenameArray:
        for igsPath in partIgsFilenameArray:
            part = os.path.split(partPath)[1]
            igs = os.path.split(igsPath)[1]
            excel = os.path.split(excelPath)[1]
            if part[:8] == excel [:8] == igs[:8]:
                print "Made zip of Part: %s Excel: %s IGES: %s" %(part, excel, igs)

                zf = zipfile.ZipFile("%s%s.zip" %(outputPath, part[:8]), mode="w")
                try:
                    zf.write(outputPath + part, part)
                    zf.write(excelPath, excel)
                    zf.write(igsPath, igs)
                finally:
                    zf.close()

