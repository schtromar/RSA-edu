def beseda_v_stevilko(beseda):
	stevilka = 0
	for crka in beseda:
		stevilka = stevilka*1000 + ord(crka)
	return stevilka

print("----------------------------------------------------------------------")
print("               Pozdravljeni v programu RSA OŠ Sostro                  ")
print("                        za šifriranje sporočil                        ")
print("----------------------------------------------------------------------")
sporocilo = input("Vnesite sporočilo: ")
n = int(input("[ključ] vnesite n: "))
e = int(input("[ključ] vnesite e: "))

sporocilo_stevilka = beseda_v_stevilko(sporocilo)
sifrirano_sporocilo = ((sporocilo_stevilka)**e)%n

print("------------------ZAČETEK ŠIFRIRANEGA SPOROČILA-----------------------")
print(sifrirano_sporocilo);
print("-------------------KONEC ŠIFRIRANEGA SPOROČILA------------------------")
