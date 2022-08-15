# convert url into xml string
# http://py4e-data.dr-chuck.net/comments_1622080.xml is the url
import xml.etree.ElementTree as ET
from urllib.request import urlopen

from bs4 import BeautifulSoup

# using beautiful soup

url = input("Enter the url ")
xml = urlopen(url)

soup = BeautifulSoup(xml,'xml')
counts = soup('count')
s=0
for var in counts:
    val = var.contents[0]
    s+=int(val)
print("The sum is",s)