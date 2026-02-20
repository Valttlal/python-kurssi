sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hb_str = input("Anna hemoglobiiniarvo (g/l): ")
hb = int(hb_str)

# Normalisoidaan syöte helpompaa vertailua varten
sukupuoli = sukupuoli.lower()

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli")