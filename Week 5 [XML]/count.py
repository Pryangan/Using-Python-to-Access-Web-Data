import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_141287.xml')
data = fhand.read()
val = data.decode()
print(val)
stuff = ET.fromstring(val)
lst = stuff.findall('comments/comment')
print('User Count: ',len(lst),'\n')
count = 0
for item in lst:
    count += int(item.find('count').text)

print('Sum: ',count)
