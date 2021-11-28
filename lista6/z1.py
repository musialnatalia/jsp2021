import trojkat
import numpy as np

a = float(input("Podaj bok 'a' trójkąta: "))
b = float(input("Podaj bok 'b' trójkąta: "))
c = float(input("Podaj bok 'c' trójkąta: "))

l = [a,b,c]
ll = l.copy()
m = max(l)
ll.pop(np.argmax(l))

if m >= sum(ll):
	print("Trójkąt o podanych bokach nie istnieje")
	exit()

print("Obwód = ",trojkat.obwod(a,b,c))
print("Pole = ",trojkat.pole(a,b,c))
print(trojkat.bok(a,b,c))
print(trojkat.kat(a,b,c))
