"""Script to merge a range of inspection standards
Input:
    First part in series
    How many parts there are total
    Which page the inspection standard should start on
Output
    Each part drawing is merged with the corresponding inspection standard
    Assumes that all the parts are sequential
"""

from PyPDF2 import PdfFileMerger
import os
import re
import sys

dir = "D:\\Desktop\\ECO80476 - Tip and Shaft\\"
#dir = raw_input("What is the directory?") #Assumes both part drawings and inspection standards are in the same directory
startPage = 1
#startPage = int(raw_input("Which page should the inspection standard start after? "))

partFilename = []
inspFilename = []

expression = 'P\d+_\D'
#Matches only part numbers at the beginning of the string
#'P' Must start with P
#'\d' Matches 1 or more decimal digits
#'_' Matches underscore
#'\D' Matches any nondigit character

for filename in os.listdir(dir):
    root, ext = os.path.splitext(filename)

    if re.match(expression, root) and ext == ".pdf": #Checks to see that it starts with the expected part number and rev and is a PDF
        if ("Inspection Standard" in root):
#             print "This is an inspection standard %s" %filename
            inspFilename.append(filename)
        else:
#             print "This is a drawing %s" %filename
            partFilename.append(filename)

for part in partFilename:
    for insp in inspFilename:
        if part[:8] == insp[:8]: #Matches part and rev to merge
            merger = PdfFileMerger()
            partPath = dir + part
            inspPath = dir + insp

            partPDF = open(partPath, "rb")
            inspPDF = open(inspPath, "rb")

            merger.append(fileobj=partPDF, pages=(0,startPage))
            merger.append(fileobj=inspPDF)

            output = open("D:\\Desktop\\Test\\%s.pdf" %part[:8], "wb")
            merger.write(output)
            print "Merged %s and %s" %(part, insp)
            partPDF.close()
            inspPDF.close()
            output.close()




