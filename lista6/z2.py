import SzyfrCezara as sc

tekst = input("Wprowadź tekst do szyfrowania (bez polskich znaków): ")
klucz = 2

szyfrowanie = sc.szyfr(tekst,klucz)
deszyfrowanie = sc.deszyfr(szyfrowanie,klucz)

print("Zaszyfrowanie: ",szyfrowanie)
print("Odszyfrowanie: ",deszyfrowanie)
	
