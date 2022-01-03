import random
import time

def bubble_sort(tab):
	print("Nieposortowana lista: "+str(len(tab))+" elementów: ", tab)
	start_time=time.time()
	for j in range(len(tab)-1, 0, -1):
		for i in range(j):
			if tab[i] > tab[i + 1]:
				tab[i], tab[i + 1] = tab[i + 1], tab[i]
	
	tim = time.time()-start_time
	print("Sortowanie bąbelkowe "+str(len(tab))+" elementów: ", tim)
	print("Posortowana lista: "+str(len(tab))+" elementów: ", tab,'\n')
	
lista1 = [random.randint(0,20) for x in range(100)]
lista2 = [random.randint(0,20) for x in range(200)]
lista3 = [random.randint(0,20) for x in range(300)]

lista =  [lista1,lista2,lista3]

for l in lista:
	bubble_sort(l)
