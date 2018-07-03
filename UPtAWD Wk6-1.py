import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_189554.json'

uh = urllib.urlopen(url)
data = uh.read()
counter = list()
info = json.loads(data)

for c in info["comments"]:
    counter.append(int(c.get("count")))
print sum(counter)
