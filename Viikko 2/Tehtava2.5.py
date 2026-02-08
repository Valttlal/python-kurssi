leiviska_str = input("Anna leiviskät: ")
naula_str = input("Anna naulat: ")
luoti_str = input("Anna luodit: ")
leiviska = int(leiviska_str)
naula = int(naula_str)
luoti = int(luoti_str)
# Muunnetaan kaikki luodeiksi
luodit_yhteensa = leiviska * 20 * 32 + naula * 32 + luoti
# Muunnetaan grammoiksi
grammat = luodit_yhteensa * 13.3
kilot = int(grammat // 1000)
grammat_jaljella = grammat - kilot * 1000
print("Massa on " + str(kilot) + " kg ja " + str(grammat_jaljella) + " g")