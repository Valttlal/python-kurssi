def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = float(input("Anna bensiinin määrä nestegallonoina: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Määrä litroina on " + str(litrat))
    gallonat = float(input("Anna bensiinin määrä nestegallonoina: "))