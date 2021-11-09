liczby = []
for i in range(100,401):
	lista = list(str(i))
	llen = len(lista)
	ll = 0
	for l in lista:
		if (int(l) % 2) == 0:
			ll = ll+1
		else:
			ll = ll
	if ll==llen:
		liczby.append(i)
		
print("Liczby z parzystymi cyframi: ", liczby)
