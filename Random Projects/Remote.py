"""
Python Site Remote
This program allows the user to save and open sites.
Github: MattDWe
"""

import webbrowser, pyperclip

savedSites = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Projects\\Random\\sites.txt")
sites = savedSites.readlines()

saveOrOpen = input("Would you like to open or save a site? ").upper()

def openSite(sites):
    i = 1
    for site in sites:
        print(str(i) + ". " + site)
        i += 1
    chosenSite = input("Please enter the number you would like to open... ")
    try:
        webbrowser.open(sites[int(chosenSite) - 1])
    except:
        print("Not a valid site.")

def saveSite(sites):
    input("Please copy your site to your clipboard and press enter to continue.")
    savedSites = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Projects\\Random\\sites.txt", "a")
    savedSites.write("\n" + pyperclip.paste())
    print(pyperclip.paste() + "... saved successfully.")
    
if saveOrOpen == "OPEN":
    openSite(sites)
elif saveOrOpen == "SAVE":
    saveSite(sites)
else:
    print("Error")

savedSites.close()
