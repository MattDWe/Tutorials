#Table Formatting Program
#Project suggested by Automate The Boring Stuff Ch 6

tableData = [["Apples", "Cheese" , "Waffles", "Grapes"],
             ["Hello", "Nope", "Yogurt", "Jello"],
             ["Jips", "Jops", "Japs", "Jups"]]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in colWidths:
        colWidths = max(tableData[i], key = len) #Find longest string
    y = len(colWidths)
        
    for x in range(len(tableData[0])):
        print(str(tableData[0][x]).rjust(y) + str(tableData[1][x]).rjust(y) + str(tableData[2][x]).rjust(y))

printTable(tableData)
