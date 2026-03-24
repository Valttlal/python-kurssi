def lukujen_summa(lista):
    summa = 0

    for luku in lista:
        summa = summa + luku

    return summa

luvut = [3, 7, 2, 8, 4]
tulos = lukujen_summa(luvut)
print("Listan lukujen summa on " + str(tulos))