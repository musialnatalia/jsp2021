a = float(input("Podaj współczynnik a: "))
while a == 0:
	print("Współczynnik 'a' = 0, podaj ponownie... ")
	a = float(input("Podaj współczynnik a: "))
	
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b**2 - 4*a*c
x1 = (-b+delta**(1/2))/(2*a)
x2 = (-b-delta**(1/2))/(2*a)

eq = str(a)+"x^2 + "+str(b)+"x + "+str(c)
print("Pierwiastki równania kwadratowego", eq)
if delta > 0:
	print("x1 = ",x1, ", x2 = ",x2)
elif delta == 0:
	print("x1 = ",x1)
else:
	print("Brak rozwiązań")

