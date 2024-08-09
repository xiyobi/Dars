from os import system
from json import dumps
system("cls")

file = open("people_count.txt","r")

lst = []
datapeople = file.read().split('\n')
for odam in datapeople:
    odam = odam.split(",")
    dct = {
        'name':odam[0],
        'fname':odam[1],
        'gener':odam[2],
        'age':int(odam[3]),
        'country':odam[4]
    }
    if dct['gener'] == 'Male':
        lst.append(dct)
print(dumps(lst,indent=4))