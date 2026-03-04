syote = input("Anna luku (tyhjä lopettaa): ")

if syote == "":
    print("Et antanut yhtään lukua.")
else:
    luku = float(syote)
    pienin = luku
    suurin = luku

    syote = input("Anna luku (tyhjä lopettaa): ")
    while syote != "":
        luku = float(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
        syote = input("Anna luku (tyhjä lopettaa): ")

    print(f"Pienin: {pienin:g}")
    print(f"Suurin: {suurin:g}")