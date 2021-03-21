def stevilka_v_besedo(stevilka):
	beseda = ""
	while stevilka>0:
		beseda = chr(stevilka%1000) + beseda
		stevilka = stevilka//1000
	return beseda

print("----------------------------------------------------------------------")
print("               Pozdravljeni v programu RSA OŠ Sostro                  ")
print("                        za šifriranje sporočil                        ")
print("----------------------------------------------------------------------")
sporocilo = int(input("Vnesite sporočilo: "))
n = int(input("[ključ] vnesite n: "))
e = int(input("[ključ] vnesite e: "))

sifrirano_sporocilo = ((sporocilo)**e)%n

sifrirano_sporocilo_beseda = stevilka_v_besedo(sifrirano_sporocilo)

print("------------------ZAČETEK ŠIFRIRANEGA SPOROČILA-----------------------")
print(sifrirano_sporocilo_beseda);
print("-------------------KONEC ŠIFRIRANEGA SPOROČILA------------------------")
