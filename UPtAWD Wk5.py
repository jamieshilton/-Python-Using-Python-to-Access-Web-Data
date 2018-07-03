import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_189550.xml'

uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

stuff = tree.findall('.//count')

counted = list()
for item in stuff:
    counted.append(int(item.text))
    
print len(counted)
print sum(counted)