def rom_arab(roman):
	ra = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	ar = [ra[r] for r in roman]
	
	i = 0
	arabic=0
	while i < len(ar):
	    if i < len(ar) - 1 and ar[i] < ar[i+1]:
	        arabic = arabic + ar[i+1] - ar[i];
	        i = i + 2
	    else:
	        arabic = arabic + ar[i]
	        i = i + 1
	return arabic
	
liczba = input("Podaj cyfrę rzymską: ")
print("Cyfra arabska: ",rom_arab(liczba))
