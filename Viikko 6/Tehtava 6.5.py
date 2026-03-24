def karsi_parittomat(lista):
    karsittu_lista = []

    for luku in lista:
        if luku % 2 == 0:
            karsittu_lista.append(luku)

    return karsittu_lista

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
karsittu_lista = karsi_parittomat(alkuperainen_lista)

print("Alkuperäinen lista: " + str(alkuperainen_lista))
print("Karsittu lista: " + str(karsittu_lista))