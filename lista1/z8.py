
a = float(input("Wprowadź liczbę 'a': "))
b = float(input("Wprowadź liczbę 'b', która jest mniejsza od liczby 'a': "))

z = a%b

print("Reszta z dzielenia a/b: ", z)
z*=3+z
print("Wynik działania z*(z+3): ", z)
