def suurin_arvo(a, b, c):
    return max(a, b, c)


# kysytään käyttäjältä
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# tulostetaan tulos
print("Suurin arvo on:", suurin_arvo(luku1, luku2, luku3))