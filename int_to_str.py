def stevilka_v_besedo(stevilka):
	beseda = ""
	while stevilka>0:
		beseda = chr(stevilka%1000) + beseda
		stevilka = stevilka//1000
	return beseda

print("----------------------------------------------------------------------")
print("                 Pozdravljeni v programu OŠ Sostro                    ")
print("                  za pretvarjanje števil v besede                     ")
print("----------------------------------------------------------------------")

sporocilo = int(input("Vnesite sporočilo: "))
sporocilo_beseda = stevilka_v_besedo(sporocilo)

print("---------------------------ZAČETEK SPOROČILA-------------------------")
print(sporocilo_beseda);
print("----------------------------KONEC SPOROČILA--------------------------")
