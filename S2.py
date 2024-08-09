from os import system
from json import dumps
system("cls")

file = open("languages.txt","r")

lst = []
datapeople = file.read().split('\n')
for odam in datapeople:
    odam = odam.split(",")
    dct ={
        'name':odam[0],
        'number':int(odam[1]),
        'millat':odam[2]
    }
    if dct['number'] >1000000:
        lst.append(dct)
print(dumps(lst,indent=4))