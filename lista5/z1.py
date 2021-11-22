def zmiana(liczba):
	tab0_9 = ['jed','dwa','trz','czt','pię','sze','sie','osi','dzi']
	tab11_19 = 'naście'
	tab_0 = ['dziesięć','dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt']
	
	liczba = liczba.split()
	length = len(liczba)
	if length == 1:
		liczba_d = ''.join(list(str(liczba[0]))[-6:])
		liczba_j = ''.join(list(str(liczba[0]))[:3])
		if liczba_d == tab11_19:
			nr = '1'
			for idx,val in enumerate(tab0_9):
				if liczba_j == val:
					nr = nr+str(idx+1)
		else:
			for idx,val in enumerate(tab0_9):
				if liczba_j == val:
					nr = str(idx+1)
		for idx,val in enumerate(tab_0):
			if str(liczba[0]) == val:
				nr = str(idx+1)+'0'
	if length == 2:
		liczba_d = ''.join(list(str(liczba[0]))[:3])
		liczba_j = ''.join(list(str(liczba[1]))[:3])
		for idx,val in enumerate(tab0_9):
			if liczba_d == val:
				nr = str(idx+1)
		for idx,val in enumerate(tab0_9):
			if liczba_j == val:
				nr = nr+str(idx+1)
	return nr
				
l = input("Podaj słownie liczbę z zakresu od 1 do 59: ")
print(zmiana(l))
