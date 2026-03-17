import random

kuutioiden_maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(kuutioiden_maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print("Silmälukujen summa on " + str(summa))