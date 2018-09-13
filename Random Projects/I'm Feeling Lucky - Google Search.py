"""
Project From Automate The Boring Stuff Chapter 11
Project: I'm Feeling Lucky Google Search
Github: MattDWe
Program is to open the top search results automatically for the user
"""

import requests, sys, webbrowser, bs4

googleSearch = input("What are you googling? ")
print("Googling...")
res = requests.get("http://google.com/search?q=" + googleSearch)
try:
    res.raise_for_status()
except:
    print("Failed.")

#Retrieve top search results.
soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result.
linkElems = soup.select(".r a")
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("http://google.com" + linkElems[i].get("href"))
