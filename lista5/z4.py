def szyfrowanie(mess):
	klucz = {'a' : 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y' : 'e'}
	szyfr = ''.join([klucz.get(l,l) for l in mess])
	return szyfr
	
def odszyfrowanie(szyfr):
	klucz = {'a' : 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y' : 'e'}
	deszyfr = []
	for s in list(szyfr):
		l = klucz.get(s,s)
		if l == s:
			deszyfr.append(s)
		else:
			for i,v in klucz.items():
				if s == v:
					deszyfr.append(i)
	deszyfr = ''.join(deszyfr)
	return deszyfr

letters = 'to jest moj tekst'
x = szyfrowanie(letters)
print(x)
print(odszyfrowanie(x))

letters = 'ala ma kota'
x = szyfrowanie(letters)
print(x)
print(odszyfrowanie(x))
