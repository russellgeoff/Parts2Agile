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

merger = PdfFileMerger()

dir = "D:\\Desktop\\ECO80476 - Tip and Shaft"
#dir = raw_input("What is the directory?") #Assumes both part drawings and inspection standards are in the same directory
startPart = raw_input("What is the first part number (ex P24608)? ")
numParts = int(raw_input("What is the total number of parts? "))
#startPage = int(raw_input("Which page should the inspection standard start on? "))

for filename in os.listdir(dir):
    root, ext = os.path.splitext(filename)
    if root.startswith("P2461") and ext == ".pdf":
        print filename
        #merge the pdfs here
        #Assume that all the files are paired together and combine


# for name in range(int(startPart[-5:]), int(startPart[-5:]) + numParts):
#     fileLoc = dir + "P" + name
#     part = open()
