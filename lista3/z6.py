i = int(input("Podaj liczbę: "))
j = list(range(1,11))

print('Tablica mnożenia:')
for x in j:
	wynik = i*x
	print(str(i)+' * '+str(x)+' = '+str(wynik))
