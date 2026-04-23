kirjasto = {
    "Seitsemän veljestä": ["Aleksis Kivi", 1870, "Romaani"],
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Sotaromaani"],
    "Harry Potter": ["J. K. Rowling", 1997, "Fantasia"]
}
print("Seitsemän veljeksen kirjoittaja:", kirjasto["Seitsemän veljestä"][0])
print("Harry Potterin genre:", kirjasto["Harry Potter"][2])

kirjasto["Tuntematon sotilas"][2] = "Sota"
kirjasto["Pieni prinssi"] = ["Antoine de Saint-Exupéry", 1943, "Satu"]

del kirjasto["Harry Potter"]

print("Päivitetty kirjasto:")
print(kirjasto)