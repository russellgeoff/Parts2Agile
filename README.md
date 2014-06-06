Parts2Agile
===========
Application takes all files required for part release in Agile PLM and merges them into one zip file.

#Inputs#
    Directory containing part drawing PDFs, excel inspection standards, and IGES part files
    Page specifying where part drawing ends in the drawing PDF. Used to determine where the inspection standard should start
#Processing:#
    Creates PDFs of all excel inspection standards
    Matches part drawing PDFs to inspection standard PDFs
    Merges part drawing PDFs & inspection standard PDFs
    Matches part PDFs, excel inspection standards, & IGES files
    Combines matched PDFs, excel inspection standards, & IGES files into a ZIP file
#Output:#
    Zip file named after the part drawing PDF containing all files required for routing on Agile PLM
