from os import system
from json import dumps
system("cls")
son = int(input("son kiriting: "))
str(son)
fayl = open("cinema.txt",'r')
cinemamalumot = fayl.read().split("\n")
lst= []
for kino in cinemamalumot:
    kino = kino.split(",")
    dct =  {
        "Id":int(kino[0]),
        "cname":kino[1],
        "genre":kino[2],
        "year": int(kino[3]),
        "cinema":kino[4],
        "start_at":kino[5]

    }

    if dct["year"]>2000 and dct["genre"]=='Comedy' or dct["genre"]=='Drama' or dct["genre"]=='Romance' and dct["start_at"]>='17:00' and dct["start_at"]>='son':
        lst.append(dct)
print(dumps(lst,indent=4))
fayl.close()