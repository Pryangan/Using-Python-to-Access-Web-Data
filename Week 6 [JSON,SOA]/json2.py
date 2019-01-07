import json

data = '''[
        {
            "id" : "001",
            "x" : "2",
            "name" : "Pryangan"
        },
        {
            "id" : "007",
            "x" : "3",
            "name" : "Pran"
        }
    ]'''

info = json.loads(data)
print('User Count :',len(info),'\n')
for item in info:
    print('Name:',item['name'])
    print('Id:',item['id'])
    print('x:',item['x'],'\n')
        
