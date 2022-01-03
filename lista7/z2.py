import random
import time

def insert_sort(tab):
	print("Nieposortowana lista: "+str(len(tab))+" elementów: ", tab)
	start_time=time.time()
	for i in range(1,len(tab)):
		k = tab[i]
		j = i - 1
		while j >= 0 and k < tab[j]:
			tab[j + 1] = tab[j]
			j = j - 1
            
		tab[j + 1] = k
     
		tim = time.time()-start_time
	
	print("Sortowanie przez wstawianie "+str(len(tab))+" elementów: ", tim)
	print("Posortowana lista: "+str(len(tab))+" elementów: ", tab,'\n')
     



lista1 = [random.randint(0,20) for x in range(100)]
lista2 = [random.randint(0,20) for x in range(200)]
lista3 = [random.randint(0,20) for x in range(300)]

lista =  [lista1,lista2,lista3]

for l in lista:
	insert_sort(l)
