people = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}
print("Johnin nimi:", people["John"][0])
print("Johnin ikä:", people["John"][1])
print("Emilyn ammatti:", people["Emily"][2])

people["Anna"][2] = "Teacher"
people["James"] = ["James", 28, "Writer"]
people["Sophia"] = ["Sophia", 35, "Lääkäri"]

del people["Emily"]

print("Lopullinen sanakirja:")
print(people)