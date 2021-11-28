""" Moduł 'trojkat' zawierający cztery funkcje, które na podstawie boków trójkąta zwracają:
	obwód trójkąta - trojkat.obwod(bok1,bok2,bok3)
	pole trójkąta - trojkat.pole(bok1,bok2,bok3)
	informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny - trojkat.bok(bok1,bok2,bok3)
	informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny - trojkat.kat(bok1,bok2,bok3) """

def obwod(a,b,c):
	return a+b+c


def pole(a,b,c):
	p = (a+b+c)/2.
	return (p*(p-a)*(p-b)*(p-c))**0.5


def bok(a,b,c):
	if a == b and b == c:
		t = 'trójkąt równoboczny'
	if (a == b and a != c) or (b == c and b != a) or (a == c and c != b):
		t = 'trójkąt równoramienny'
	if a != b and b != c and c != a:
		t = 'trójkąt różnoboczny'
	return t
	
	
def kat(a,b,c):
	if (a**2 + b**2) == c**2:
		k = 'trójkąt prostokątny'
	if (a**2 + b**2) < c**2:
		k = 'trójkąt rozwartokątny'
	if (a**2 + b**2) > c**2:
		k = 'trójkąt ostrokątny'
	return k
	

if __name__ == '__main__':
	a = 1 ; b = 1 ; c = 3
	print("obwód ",obwod(a,b,c))
	print("pole ",pole(a,b,c))
	print(bok(a,b,c))
	print(kat(a,b,c))
