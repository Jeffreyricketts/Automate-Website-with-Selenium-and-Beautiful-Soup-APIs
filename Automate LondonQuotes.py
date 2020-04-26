from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import docx

browser = webdriver.Chrome('chromedriver')
browser.get("https://jeffreyricketts.github.io/LondonQuotes/")

source = requests.get('https://jeffreyricketts.github.io/LondonQuotes/').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

doc = docx.Document()

for p in soup.find_all('p'):
    quote = p.text
    print(quote)
    doc.add_paragraph(quote)

doc.save('London Quotes Automation.docx')

