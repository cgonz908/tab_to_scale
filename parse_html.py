from html.parser import HTMLParser
from bs4 import BeautifulSoup
import pull_url

url = "https://tabs.ultimate-guitar.com/tab/stevie-ray-vaughan-double-trouble/pride-and-joy-tabs-30829"
html = pull_url.pull_url(url)

soup = BeautifulSoup(html, features='lxml')
soup2 = BeautifulSoup(html, features='html.parser')

parent = soup.find("div", class_="js-page js-global-wrapper")
parent2 = soup2.find("div", class_="js-page js-global-wrapper")

for child in soup.body.div.children:
    print("CHILD:" + child)