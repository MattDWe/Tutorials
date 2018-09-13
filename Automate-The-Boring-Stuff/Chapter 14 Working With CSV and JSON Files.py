"""
Automate The Boring Stuff Chapter 14
Working With CSV Files and JSON Data
Github: MattDWe
"""

import csv

#CSV
#Reading
exampleFile = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff\\Chapter 14\\example.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

for data in exampleData:
    print("Date: " + data[0] + " Food: " + data[1] + " Amount: " + data[2])

print(exampleData[0][0])

#Writing
outputFile = open(".\\Chapter 14\\output.csv", "w", newline="")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(["spam", "eggs", "bacon", "ham"])
outputWriter.writerow(["Helloe, world!", "eggs", "bacon", "ham"])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

csvFile = open(".\\Chapter 14\\example.tsv", "w", newline="")
csvWriter = csv.writer(csvFile, delimiter="\t", lineterminator="\n\n")
csvWriter.writerow(["apples", "oranges", "grapes"])
csvWriter.writerow(["eggs", "bacon", "ham"])
csvWriter.writerow(["spam", "spam", "spam", "spam"])
csvFile.close()

#JSON and APIs
import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData) #.loads means load string
print(jsonDataAsPythonValue)

pythonValue = {"isCat": True, "miceCaught": 0, "name": "Zophie", "felineIQ": None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

"""
Practice Questions
1. changing width and height font colors charts and images
2. The opened file
3. Files "rb" writer is "wb"
4. writerow()
5. delimiter arugment changes the string used to seperate cells in a row. lineterminator changes the string used to seperate rows
6. json.loads()
7. json.dumps()
"""
