import requests
from bs4 import BeautifulSoup

# Use the requests module to make a GET request to the URL of the webpage
response = requests.get("https://portal.ez.na.rme.logistics.a2z.com/login")

# Use the beautifulsoup module to parse the HTML of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find the element on the webpage that you want to click
element = soup.find("button", {"class": "mdc-button mdc-button--raised"})

# Use the click method to simulate a click on the element
element = element.get()
if element is not None:
    element.click()