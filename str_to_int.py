def beseda_v_stevilko(beseda):
	stevilka = 0
	for crka in beseda:
		stevilka = stevilka*1000 + ord(crka)
	return stevilka

print("----------------------------------------------------------------------")
print("                 Pozdravljeni v programu OŠ Sostro                    ")
print("                  za pretvarjanje besed v števila                     ")
print("----------------------------------------------------------------------")

sporocilo = input("Vnesite sporočilo: ")
sporocilo_stevilka = beseda_v_stevilko(sporocilo)

print("---------------------------ZAČETEK SPOROČILA-------------------------")
print(sporocilo_stevilka);
print("----------------------------KONEC SPOROČILA--------------------------")
