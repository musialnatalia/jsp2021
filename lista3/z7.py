N = int(input("Podaj liczbę całkowitą: "))
tab = [0,1]
fib = []

print("Ilość wyrazów ciągu: ",N)
print("Wyrazy ciągu:")
if N==1:
	fib.extend((0,1))
elif N==0:
	fib.append(0)
else:
	fib.extend((0,1))
	for i in range(N-1):
		x = tab[0]+tab[1]   
		tab[0] = tab[1]
		tab[1] = x
		fib.append(x)
		
print(fib)
