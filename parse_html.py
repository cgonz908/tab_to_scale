from html.parser import HTMLParser
from bs4 import BeautifulSoup

file_path = "/Users/christiangonzalez-capizzi/Desktop/tab_to_scale/webpage.txt"

#load html file
f = open(file_path, 'r')
html = f.read()

soup = BeautifulSoup(html)

 