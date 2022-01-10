""" Moduł 'SzyfrCezara' zawierający dwie funkcje:
	szyfrowania - SzyfrCezara.szyfr(tekst, klucz)
	deszyfrowania - SzyfrCezara.deszyfr(tekst, klucz) 
	Moduł nie obsługuje polskich znaków. """

def szyfr(tekst,klucz):
	s = ''
	tekst = list(tekst)
	for i in tekst:
		if ord(i) > 122 or ord(i) < 97:
			s += chr(ord(i))
		elif ord(i) > 122 - klucz:
			s += chr(ord(i) + klucz - 26)
		else:
			s += chr(ord(i) + klucz)
	return s
	
def deszyfr(tekst,klucz):
	ds = ""
	tekst = list(tekst)
	kluczm = klucz % 26
	for i in tekst:
		if ord(i) > 122 or ord(i) < 97:
			ds += chr(ord(i))
		elif (ord(i) - kluczm < 97):
			ds += chr(ord(i) - kluczm + 26)
		else:
			ds += chr(ord(i) - kluczm)
	return ds

			
if __name__ == '__main__':
	tekst = 'abrakadabra'
	klucz = 2
	t = szyfr(tekst,klucz)
	print(tekst)
	print(t)
	print(deszyfr(t,klucz))
