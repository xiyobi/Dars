import os,json
from json import dumps

os.system("cls")

lst = []

fayl = open('people_count.txt',"r")

datapeople = fayl.read().split('\n')
for i in range(len(datapeople)):
    datapeople[i] = datapeople[i].split(",")
print(datapeople)
for person in datapeople:
    if person[2] == "Male":
        dtc = {
            "ismi" = person[0],
            "Familiyasi" = person[1],
            "mamlakati" = person[4]
        }
        lst.append(dtc)
        
print(dumps(lst,indent = 4))
fayl.close()