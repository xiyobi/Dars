from os import system
from json import dumps
system("cls")

users=[]

fail = open('languages.txt',"r")

malumot = fail.read().split("\n")

for odam in malumot:
    odam=odam.split(",")

    user={
    'name': odam[0],
    'number': int(odam[1]),
    'language': odam[2],
    }
    if user['number']>=1000000:
        users.append(user)


print(dumps(users, indent=4))

fail.close()
