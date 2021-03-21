print("----------------------------------------------------------------------")
print("               Pozdravljeni v programu RSA OŠ Sostro                  ")
print("                        za šifriranje sporočil                        ")
print("----------------------------------------------------------------------")
sporocilo = int(input("Vnesite sporočilo: "))
n = int(input("[ključ] vnesite n: "))
e = int(input("[ključ] vnesite e: "))

sifrirano_sporocilo = ((sporocilo)**e)%n

print("------------------ZAČETEK ŠIFRIRANEGA SPOROČILA-----------------------")
print(sifrirano_sporocilo);
print("-------------------KONEC ŠIFRIRANEGA SPOROČILA------------------------")
