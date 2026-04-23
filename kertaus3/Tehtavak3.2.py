oppilaat = {
    "Aino": ["Aino", 7, "Matematiikka"],
    "Matti": ["Matti", 8, "Historia"],
    "Liisa": ["Liisa", 9, "Biologia"]
}
print("Ainon vuosiluokka:", oppilaat["Aino"][1])
print("Matin lempiaine:", oppilaat["Matti"][2])

oppilaat["Liisa"][2] = "Kemia"
oppilaat["Pekka"] = ["Pekka", 7, "Liikunta"]

del oppilaat["Matti"]

print("Päivitetty sanakirja:")
print(oppilaat)