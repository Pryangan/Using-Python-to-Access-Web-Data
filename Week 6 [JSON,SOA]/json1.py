import json

data = '''{
        "name" : "Pryangan",
        "phone" : {
            "type" : "intl",
            "number" : "9876543210"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info['email']['hide'])
