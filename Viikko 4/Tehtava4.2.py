tuumat = float(input("Anna tuumat (negatiivinen lopettaa): "))
while tuumat >= 0:
    cm = tuumat * 2.54
    print(tuumat, "tuumaa =", cm, "cm")
    tuumat = float(input("Anna tuumat (negatiivinen lopettaa): "))
print("Toiminta lopetettu.")