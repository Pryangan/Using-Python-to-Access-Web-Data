import re

fp = open("text.txt","r")
s = 0
for line in fp:
    y = re.findall('[0-9]+',line)
    if len(y)>0:
        for num in y:
            s = int(num) + s

print("Sum:",s)



