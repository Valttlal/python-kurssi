def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def jako(a, b):
    return a / b


# kysytään luvut
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

# käytetään funktioita
print("Summa:", summa(luku1, luku2))
print("Erotus:", erotus(luku1, luku2))
print("Tulo:", tulo(luku1, luku2))
print("Jako:", jako(luku1, luku2))