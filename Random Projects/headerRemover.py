"""
Project From Automate The Boring Stuff Chapter 14
Project: Removing The Header From CSV Files
Github: MattDWe
Program is to remove headers from CSV files in the directory.
"""

import csv, os

os.makedirs("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Projects\\Automate Projects\\headerRemoved", exist_ok = True)

#Loop through every file in the current working directory.
for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue

    print("Removing header from " + csvFilename + "...")

    csvRows = []
    csvFileObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # Skip first row
        csvRows.append(row)
    csvFileObj.close()

    #Write out the CSV file.
    csvFileObj = open(os.path.join("..\\Projects\\Automate Projects\\headerRemoved", csvFilename), "w", newline="")
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
