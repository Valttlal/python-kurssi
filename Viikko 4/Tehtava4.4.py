import random

salainen = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1..10: "))

while arvaus != salainen:
    if arvaus > salainen:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein")