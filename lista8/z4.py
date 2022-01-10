import numpy as np

def rok(a,b,c):
	print(c)
	if c == 8 or c == 9:
		year = '18'+str(a)+str(b)
	if c == 0 or c == 1:
		year = '19'+str(a)+str(b)
	if c == 2 or c == 3:
		year = '20'+str(a)+str(b)
	if c == 4 or c == 5:
		year = '21'+str(a)+str(b)
	if c == 6 or c == 7:
		year = '22'+str(a)+str(b)
	return year

def mies(a,b):
	if a == 1 or a == 0:
		month = str(a)+str(b)
	elif a%2 == 0:
		month = '0'+str(b)
	else:
		month = '1'+str(b)
	return month

try:
	pesel = np.loadtxt('PESEL.txt',dtype=str)
except OSError:
	print("Nie znaleziono pliku PESEL.txt ...")
	exit()
	
f = open('PESEL-wyniki.txt','w')
for p in pesel:
	
	tab = list(p)
	v = [int(x) for x in tab]
	
	#poprawność
	val = 1*v[0] + 3*v[1] + 7*v[2] + 9*v[3] + 1*v[4] + 3*v[5] + 7*v[6] + 9*v[7] + 1*v[8] + 3*v[9]
	val = str(val)
	lval = list(val)
	if (10 - int(lval[-1])) != v[10]:
		print("Nr PESEL "+p+" jest niepoprawny")
		continue
	else:
		print("Nr PESEL "+p+" jest poprawny")
    
    # data urodzenia	
	r = rok(v[0],v[1],v[2])
	m = mies(v[2],v[3])
	d = str(v[4])+str(v[5])
	bdat = "Data urodzenia: {}.{}.{}".format(d,m,r)
	print(bdat)
	
	#płeć
	if v[9]%2 == 0:
		s = 'kobieta'
	else:
		s = 'mężczyzna'
	print("Płeć: "+s)
	
	#zapis
	f.write("nr PESEL: {}\n data urodzenia {}-{}-{};\t płeć: {}\n".format(p,d,m,r,s))
	
f.close()
print("Zapisano wyniki do pliku "+f.name)
	
	
	
	
	
	
	
