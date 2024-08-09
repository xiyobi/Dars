from os import system
from json import dumps

system("cls")
umumiy = []
m = []
d_t = []
a_t = []
ut = []
qonish = []
n = []
n2 = []

file = open("homework.txt","r")

travel = file.read().split("\n")

p = float(input("Pulizni kiriting: "))
for person in travel:
    person = person.split(",")
    dc = {
        'Id': int(person[0]),
        'Departure': person[1],
        'd_time':person[2],
        'arrive_D': person[3],
        'a_time':person[4],
        'cost': person[5]
    }
    umumiy.append(dc)
    m.append(dc['cost'])
    d_t.append(dc['arrive_D'])
    qonish.append(dc["a_time"])
    a_t.append(dc['d_time'])

for i in range(1,len(m)):
    if float(m[i][1:]) > p - 50 and float(m[i][1:]) < p+100:
        print(m[i])

joungle = input("Qaysi davlatga bormoqchisiz: ")

for j in range(1,len(d_t)):
    natija = str(a_t[j])
    natija= natija.split(":")
    n.append(natija)
    natija2 = str(qonish[j])
    natija2 = natija2.split(":")
    n2.append(natija2)
for  l in range(len(n2)):
    if d_t[l] == joungle and int(n[l][0]) <= 12 and int(n2[l][0] )>= 21:
        print(dumps(umumiy[l],indent=4))
for h in range(len(umumiy)):
    if d_t[h] == 'US' and int(n2[h][0])<=20:
        print(dumps(umumiy[h],indent=4)) 
