import random

def heita_noppaa(tahkot):
    silmaluku = random.randint(1, tahkot)
    return silmaluku

tahkot = int(input("Anna nopan tahkojen lukumäärä: "))
heitto = heita_noppaa(tahkot)

while heitto != tahkot:
    print("Sait silmäluvun " + str(heitto))
    heitto = heita_noppaa(tahkot)

print("Sait silmäluvun " + str(heitto))