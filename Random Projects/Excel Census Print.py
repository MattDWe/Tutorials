"""
Project from Automate The Boring Stuff Chapter 12
Project: Reading Data From a Speadsheet
Github: MattDWe

Program is to read the data from the census spreadsheet. Count the number of census tracts in each
county. Counts total population of each county. Print results.
"""

import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("C:\\Users\\Jon\Documents\\For Fun\\Python\\Projects\\Automate Projects\\censuspopdata.xlsx")

sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData = {}

print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    #Make sure the key for the state exists.
    countyData.setdefault(state, {})
    #Make sure the key for this country in this state exists.
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    #Each row represents one census tract, so increment by one.
    countyData[state][county]["tracts"] += 1
    #Increase the country pop by the pop in this census tract.
    countyData[state][county]["pop"] += int(pop)

#Open a new text file and write the contents of the countyData to it.
print("Writing results...")
resultFile = open(".\\Census\\census2010.py", "w")
resultFile.write("allData = " + pprint.pformat(countyData))
resultFile.close()
print("Done.")
