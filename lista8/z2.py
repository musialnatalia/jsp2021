import SzyfrCezara as sc
import numpy as np
import datetime
import os
import glob

def key(filename):
	head,tail = os.path.split(filename)
	base=os.path.splitext(tail)
	tab = list(tail)
	k = int(tab[17])
	return k

try:
	path = input("Ścieżka do plików: ")
	if path == '':
		path = os.getcwd()
except FileNotFoundError:
	print("Nie znaleziono folderu...\n Spróbuj jeszcze raz ")
	
try:
	filenames = glob.glob(path+'/plik_zaszyfrowany*')
except FileNotFoundError:
	print("Nie znaleziono plików do odszyfrowania...\n Spróbuj jeszcze raz ")
	
for fi in filenames:
	
	klucz = key(fi)
	f = open(fi,"r+")
	tekst = f.read()
	f.close()
	
	deszyfrowanie = sc.deszyfr(tekst,klucz)
	
	t0 = datetime.datetime.now()
	y = t0.year
	m = t0.month
	d = t0.day
	nowy_plik = os.path.join(path, "plik_deszyfrowany{}_{}{}{}.txt".format(str(klucz),y,m,d))
	fil = open(nowy_plik,"w")
	fil.write(deszyfrowanie)
	fil.close()
	print("Zapisano plik: {}".format(nowy_plik))

