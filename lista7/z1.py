import time

def fibonaci_recursive(n,lista,first=0,second=1):
    if (n==0):
        return lista
    if (len(lista) == 0):
        lista.append(first)
        lista.append(second)
    temp = first + second
    first = second
    second = temp
    lista.append(second)
    fibonaci_recursive(n-1,lista,first,second)
    return lista
    
def fibonaci_iterative(n,lista):
	tab = [0,1]
	if n==1:
		lista.extend((0,1))
	elif N==0:
		lista.append(0)
	else:
		lista.extend((0,1))
		for i in range(N):
			x = tab[0]+tab[1]   
			tab[0] = tab[1]
			tab[1] = x
			lista.append(x)
	return lista
    
fib = []
N = 10    
start_time=time.time()
fib_r = fibonaci_recursive(N,fib)
t_rec = time.time()-start_time
print('Rekursywnie: ', fib_r)
print('Czas: ', t_rec)

fib = []
start_time=time.time()
fib_i = fibonaci_iterative(N,fib)
t_it = time.time()-start_time
print('Iteracyjnie: ', fib_i)
print('Czas: ', t_it)


