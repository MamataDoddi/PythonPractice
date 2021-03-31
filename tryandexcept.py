import re
f=open("simple.txt",'r')
text=f.read()
pat=['s']
for i in pat:
    print(re.findall(i,text))