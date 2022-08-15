# http://py4e-data.dr-chuck.net/comments_42.html is the url
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urlopen(url)
soup = BeautifulSoup(html,"html.parser")
# sampurl=""
# for i in range(7):
#     sampurl = soup("a")[17].get("href",None)
#     html = urlopen(sampurl)
#     soup = BeautifulSoup(html,"html.parser")
# print(sampurl)

# all operations
#print(soup('span'))

# ---------------------
# tags = soup('span')
# for tag in tags:
#     print(tag.contents[0],end=' ')
# ---------------------

# tags = soup('span')
# for tag in tags:
#     print(tag.attrs)