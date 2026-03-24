import random

def heita_noppaa():
    silmaluku = random.randint(1, 6)
    return silmaluku

heitto = heita_noppaa()

while heitto != 6:
    print("Sait silmäluvun " + str(heitto))
    heitto = heita_noppaa()

print("Sait silmäluvun " + str(heitto))