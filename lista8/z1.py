import SzyfrCezara as sc
import numpy as np
import datetime
import os

try:
	
	plik = input("Ścieżka do pliku: ")
	klucz = int(input("Podaj przesunięcie (1-10): "))
	if klucz < 1 or klucz > 10:
		print("Podany klucz musi być z zakresu 1-10... \n Spróbuj jeszcze raz")
		exit()
except FileNotFoundError:
	print("Nie znaleziono pliku do szyfrownia...\n Spróbuj jeszcze raz ")
except ValueError:
	print("Podany klucz musi być liczbą całkowitą... \n Spróbuj jeszcze raz")
	
try:
	path = input("Podaj ścieżkę do zapisu pliku: ")
	l = os.listdir(path)
except FileNotFoundError:
	try:
		os.mkdir(path)
	except FileNotFoundError:
		path = ''

f = open(plik,"r+")
tekst = f.read()
f.close()

szyfrowanie = sc.szyfr(tekst,klucz)

t0 = datetime.datetime.now()
y = t0.year
m = t0.month
d = t0.day
nowy_plik = os.path.join(path, "plik_zaszyfrowany{}_{}{}{}.txt".format(str(klucz),y,m,d))
fil = open(nowy_plik,"w")
fil.write(szyfrowanie)
fil.close()
print("Zapisano plik: {}".format(nowy_plik))
