print("----------------------------------------------------------------------")
print("               Pozdravljeni v programu RSA OŠ Sostro                  ")
print("                        za šifriranje sporočil                        ")
print("----------------------------------------------------------------------")
sporocilo = input("Vnesite sporočilo: ")
n = int(input("[ključ] vnesite n: "))
e = int(input("[ključ] vnesite e: "))

sporocilo_stevilka = ""
for crka in sporocilo:
	sporocilo_stevilka = sporocilo_stevilka + str(ord(crka))
sporocilo = int(sporocilo_stevilka)

sifrirano_sporocilo = ((sporocilo)**e)%n

print("------------------ZAČETEK ŠIFRIRANEGA SPOROČILA-----------------------")
print(sifrirano_sporocilo);
print("-------------------KONEC ŠIFRIRANEGA SPOROČILA------------------------")
