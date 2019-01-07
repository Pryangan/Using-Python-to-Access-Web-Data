import xml.etree.ElementTree as ET

data = '''
            <stuff>
                <users>
                    <user x="1">
                        <id>001</id>
                        <name>Pryangan Chowdhury</name>
                    </user>
                    <user x="2">
                        <id>002</id>
                        <name>Pran</name>
                    </user>
                </users>
            </stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('User Count: ',len(lst),'\n')

for item in lst:
    print('Id: ',item.find('id').text)
    print('Name: ',item.find('name').text)
    print('Attribute: ',item.get('x'),'\n')
