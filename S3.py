from os import system
from json import dumps
system("cls")

fayl = open("product_material.txt","r")

natija =  fayl.read().split("\n")
lst = []
for d in natija:
    d = d.split(",")
    dtc = {
        "id":int(d[0]),
        "product":d[1],
        "material":d[2],
        'price':d[3],
        "is_available":d[4]
    }
    if dtc["price"]>'$500' or dtc["price"]<'$1000.0':
        lst.append(dtc)
  
print(dumps(lst,indent=4))
fayl.close()
