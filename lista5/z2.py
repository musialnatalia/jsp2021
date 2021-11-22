def zmiana(liczba):
	l = len(liczba)
	
	tab_tys = ['','tysiąc']
	tab_set = ['','sto','dwieście','trzysta','czterysta','pięćset','sześćset',
				'siedemset','osiemset','dziewięćset']
	tab_dz = ['','','dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt',
				'sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt']
	tab_jed = ['','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
	tab_10 = ['jedenaście','dwanaście','trzynaście','czternaście','piętnaście',
				'szesnaście','siedemnaście','osiemnaście','dziewiętnaście']
				
	if l == 3:
		liczba = '0'+liczba
	if l == 2:
		liczba = '00'+liczba
	if l == 1 :
		liczba = '000'+liczba
		
	liczba_t = liczba[0]
	liczba_s = liczba[1]
	liczba_d = liczba[2]
	liczba_j = liczba[3]
	
	nr_t = tab_tys[int(liczba_t)]
	nr_s = tab_set[int(liczba_s)]
	nr_j = tab_jed[int(liczba_j)]
	
	if liczba_d == '1':
		if liczba_j == '0':
			nr_d = 'dziesięć'
		else:
			nr_d = tab_10[int(liczba_j)-1]
			nr_j = ''
	else:
		nr_d = tab_dz[int(liczba_d)]
	
	nr = [nr_t,nr_s,nr_d,nr_j]
	nr = ' '.join(nr)
	return nr

l = input("Podaj liczbę od 1 do 1999: ")
print(zmiana(l))
