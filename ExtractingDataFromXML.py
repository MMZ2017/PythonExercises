import xml.etree.ElementTree as ET
import urllib

serviceurl = 'http://python-data.dr-chuck.net/comments_341768.xml'
data = urllib.urlopen(serviceurl).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
l = list()

for count in counts:
    l.append(int(count.text))

print sum(l)