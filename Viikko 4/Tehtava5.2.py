luvut = []

syote = input("Anna luku tai lopeta painamalla Enter: ")

while syote != "":
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna luku tai lopeta painamalla Enter: ")

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")

for luku in luvut[:5]:
    print(luku)