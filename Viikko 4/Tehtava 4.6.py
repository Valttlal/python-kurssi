import random

N = int(input("Anna arvottavien pisteiden määrä: "))

osumia = 0
tehdyt = 0

while tehdyt < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        osumia = osumia + 1

    tehdyt = tehdyt + 1

piin_likiarvo = 4 * osumia / N
print("Piin likiarvo:", piin_likiarvo)