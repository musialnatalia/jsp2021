import random
import numpy as np

def last(tab):
	val = 1*tab[0] + 3*tab[1] + 7*tab[2] + 9*tab[3] + 1*tab[4] + 3*tab[5] + 7*tab[6] + 9*tab[7] + 1*tab[8] + 3*tab[9]
	val = str(val)
	lval = list(val)
	l = 10 - int(lval[-1])
	if l == 10:
		l = 0
	return l
	
f = open('PESEL.txt','w')	
for n in range(10):
	#rok,miesiąc
	pesel = []
	t = 0
	for x in range(3):
		p = random.randint(0,9)
		pesel.append(p)
	if pesel[2]%2 == 0:
		p = random.randint(1,9)
	else:
		p = random.randint(0,2)
	pesel.append(p)
	#dzień
	p = random.randint(1,31)
	if p <10:
		pesel.extend((0,p))
	else:
		p = str(p)
		lp = list(p)
		pesel.extend((int(p[0]),int(p[1])))
	#reszta
	lastp = []
	for y in range(4):
		pesel.append(random.randint(0,9))
	pesel.append(last(pesel))
	pesel = [str(x) for x in pesel]
	#print(''.join(pesel))
	f.write(''.join(pesel)+'\n')

f.close()
