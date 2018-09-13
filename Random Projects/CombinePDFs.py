"""
Project From Automate The Boring Stuff Chapter 13
Project: Combining Select Pages From Many PDFs
Github: MattDWe
"""

import os, PyPDF2

#Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir("C:\\Users\\Jon\Documents\\For Fun\\Python\\Projects\\Automate Projects\\PDFs To Combine"):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower) #Organizes list to alphabetical order

pdfWriter = PyPDF2.PdfFileWriter()

#Loop through all the PDF Files and open them.
for filename in pdfFiles:
    pdfFileObj = open("C:\\Users\\Jon\Documents\\For Fun\\Python\\Projects\\Automate Projects\\PDFs To Combine\\" + filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    #Loop through all the pages (Skips the first page) and adds them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#Save the resulting PDF to a file.
pdfOutput = open("C:\\Users\\Jon\Documents\\For Fun\\Python\\Projects\\Automate Projects\\CombinedPDF.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()
