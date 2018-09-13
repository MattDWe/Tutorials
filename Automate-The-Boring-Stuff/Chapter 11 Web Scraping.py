"""
Automate The Boring Stuff Chapter 11
Web Scraping
Github: MattDWe
"""

"""
Modules that will be used this chapter:
webbrowser - Opens a browser to a specific page.
Requests - Downloads files and web pages from the internet.
Beautiful Soup - Parses HTML the format that web pages are written in.
Selenium - launches and controls a web browser. Fills in forms and simulates mouse clicks.
"""

import webbrowser
#webbrowser.open("http://inventwithpython.com/")
#This is the only thing this module can do, open browsers.

import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(res)
print(res.status_code == requests.codes.ok) #Checks if download was successful
print(len(res.text))
print(res.text[:250])

res = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

#Saving downloaded files to hard drive

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playFile = open("C:\\Users\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff\\Chapter 11\\RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

"""
How to download a file
1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.
"""

"""
Right click on a browser and click view source to see source for html.
Or press f12 to mouse over something to find it's html.
Usually when web scraping you will be going by html tags.
"""

#beautifulsoup4 is used to extract data from an html page.
import bs4, requests
res = requests.get("http://nostarch.com")
print(res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

exampleFile = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff\\Chapter 11\\example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))

"""
After you have a soup object you can use these to find information
Selector passed to the select() method
soup.select('div') - All elements named <div>
soup.select('#author') - The element with an id attribute of author
soup.select('.notice') - All elements that use a CSS class attribute named notice
soup.select('div span') - All elements named <span> that are within an element named <div>
soup.select('div > span') - All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]') - All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]') - All elements named <input> that have an attribute named type with value button
"""
import bs4
exampleFile = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff\\Chapter 11\\example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))
print(elems[0].attrs)
print(elems)

soup = bs4.BeautifulSoup(open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff\\Chapter 11\\example.html"))
spanElem = soup.select("span")[0]
print(str(spanElem))

#This requires firefox in order to use - Which I do not use
#from selenium import webdriver
#browser = webdriver.Firefox()
#print(type(browser))
#browser.get("http://inventwithpython.com")

"""
Methods for finding elements
browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)           Elements that use the CSS class name

browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)     Elements that match the CSS selector

browser.find_element_by_id(id)
browser.find_elements_by_id(id)                     Elements with a matching id attribute value

browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)            <a> elements that completely match the text provided

browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)    <a> elements that contain the text provided

browser.find_element_by_name(name)
browser.find_elements_by_name(name)                  Elements with a matching name attribute value

browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)              Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')
"""

"""
WebElement Attributes and Methods
tag_name                                             The tag name, such as 'a' for an <a> element

get_attribute(name)                                  The value for the element’s name attribute

text                                                 The text within the element, such as 'hello' in <span>hello</span>

clear()                                              For text field or text area elements, clears the text typed into it

is_displayed()                                       Returns True if the element is visible; otherwise returns False

is_enabled()                                         For input elements, returns True if the element is enabled; otherwise returns False

is_selected()                                        For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

location                                             A dictionary with keys 'x' and 'y' for the position of the element in the page
"""

#To click after finding it .click()
"""
Example of filling out a form using selenium
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
"""

"""
Practice Questions
1. webbrowser module is used to open a browser, requests is to download a page, beautifulSoup is to search through css to find something, and selenium interacts directly with a FireFox browser.
2. It returns a string of the websites downloaded text
3. name.raise_for_status()
4. The res.status_code == requests.codes.ok attriute has http status code
5. Open the new file in "wb" or wriute binary mode use a for loop that goes over the object iter_content() to write chunks to the file.
Example
saveFile = open("filename.html", "wb")
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
6. F12
7. Right click inspect element
8. "#main"
9. ".hightlight"
10. "div div"
11. "button[value="favorite"]"
12. spam.getText()
13. linkElem.attrs
14. from selenium import webdriver
15. element returns the first found element. elements return all found elements
16. click() and send_keys()
17. submit()
18. forward() back() and refresh()
"""
