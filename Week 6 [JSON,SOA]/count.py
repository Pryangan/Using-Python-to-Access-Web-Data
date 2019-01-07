import urllib.request, urllib.parse, urllib.error
import json

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_141288.json')
data = fhand.read()
val = data.decode()
print(val)
stuff = json.loads(val)
count = 0
for item in stuff['comments']:
    count += int(item['count'])

print('Sum is :',count)
