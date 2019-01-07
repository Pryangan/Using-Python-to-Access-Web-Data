import xml.etree.ElementTree as ET

data = '''
            <person>
                <firstname>Pryangan</firstname>
                <lastname>Chowdhury</lastname>
                <phone type="intl">
                    9876543210
                </phone>
                <email hide="yes"/>
            </person>'''

tree = ET.fromstring(data)
print('Name: ',tree.find('firstname').text+' '+tree.find('lastname').text)
print('Phone: ',tree.find('phone').text.strip())
print('Email: ',tree.find('email').get('hide'))
