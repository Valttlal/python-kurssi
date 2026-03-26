def kuusi(koko):
    print("Tämä on kuusi!")

    # Yläosa
    for i in range(koko):
        tahdet = 2 * i + 1
        valit = koko - i - 1
        print(" " * valit + "*" * tahdet)

    # Runko
    print(" " * (koko - 1) + "*")

kuusi(5)