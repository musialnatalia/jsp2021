import numpy as np

n = int(input("Podaj liczbę całkowitą n: "))
m = int(input("Podaj liczbę całkowitą m: "))
tab2d = np.zeros((n,m))

for i in range(n):
	for j in range(m):
		tab2d[i,j] = (i+1)*(j+1)

print(tab2d)
