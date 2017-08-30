from bs4 import BeautifulSoup
import urllib

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

l = list()
for tag in tags:
    l.append(int(tag.contents[0]))

print sum(l)