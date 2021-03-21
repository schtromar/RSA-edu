from random import randint

def prastevilo(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def najvecji_skupni_deljitelj(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def najmanjsi_skupni_veckratnik(x,y):
	if x > y:
		vecja = x
	else:
		vecja = y

	while(True):
		if((vecja % x == 0) and (vecja % y == 0)):
			lcm = vecja
			break
		vecja += 1
	return lcm

def tuji_stevili(x, y):
    return najvecji_skupni_deljitelj(x, y) == 1


print("----------------------------------------------------------------------")
print("               Pozdravljeni v programu RSA OŠ Sostro                  ")
print("                       za generiranje ključev                         ")
print("----------------------------------------------------------------------")

spodnja_meja = int(input("Vnesite spodnjo mejo: "))
zgornja_meja = int(input("Vnesite zgornjo mejo: "))

p = randint(spodnja_meja, zgornja_meja)
while not prastevilo(p):
	p = randint(spodnja_meja, zgornja_meja)


q = randint(spodnja_meja, zgornja_meja)
while not prastevilo(q):
	q = randint(spodnja_meja, zgornja_meja)


print("P: ", p)
print("Q: ", q)


n = p*q
m = najmanjsi_skupni_veckratnik((p-1),(q-1))

print("N: ", n)
print("M: ", m)

e = randint(1, m)
while not (tuji_stevili(e, m)):
	e = randint(1, m)

print("E: ", e)
d = 1
while not ((e * d) % m) == 1:
#	print((e*d)%m)
	d = d + 1


print("-----------------------ZAČETEK JAVNEGA KLJUČA-------------------------")
print("N: ", n)
print("E: ", e)
print("------------------------KONEC JAVNEGA KLJUČA--------------------------")
print("----------------------ZAČETEK ZASEBNEGA KLJUČA------------------------")
print("N: ", n)
print("D: ", d)
print("-----------------------KONEC ZASEBNEGA KLJUČA-------------------------")


