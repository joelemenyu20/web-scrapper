#importing Libraries
from bs4 import BeautifulSoup
import requests
import re
import json

#function to extract html document from given url
def getHTMLdocument(url):
    response = requests.get(url)

    return response.text
# website to scrape
url_to_scrape = 'https://incafrica.com/article/bill-murphy-jr-51-elon-musk-quotes-ranked-in-order-of-pure-elon-muskiness'

html_document = getHTMLdocument(url_to_scrape)
content = BeautifulSoup(html_document, "html.parser")

#Accessing the content of the website and saving it in a JSON file called myContent.json
datas = content.find("div").text.encode('utf-8')
# html_document.append(datas)
with open('myContent.json', 'w') as outfile:json.dump(html_document, outfile)

