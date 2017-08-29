import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_341772.json'
data = urllib.urlopen(url).read()
info = json.loads(data)
comments = info['comments']
l = list()

for item in comments:
    l.append(int(item['count']))

print "Total number of comments are:" + str(sum(l))