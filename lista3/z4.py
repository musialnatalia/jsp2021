import numpy as np

row = 7
col = 28

tab2d = [[" " for i in range(col)] for j in range(row)]

#  LITERA 'L'
for l in range(row):
	tab2d[l][0] = '*'
for l in range(5):
	tab2d[row-1][l] = '*'


#  LITERA 'A'
atab = [8,9,10,11,11,12,13,14,15,15,16,17,18]
i=0
for a in reversed(range(row)):
	tab2d[a][atab[i]] = '*'
	i = i+1
for a in range(row):
	tab2d[a][atab[i-1]] = '*'
	i = i+1
for a in range(11,16):
	tab2d[3][a] = '*'


#  LITERA 'R'
rt = range(23,27)
rt1 = [22,27]
rt2 = [22,25]
rt3 = [22,26]
rt4 = [22,27]
for r in range(row):
	if r==0 or r==3:
		for rr in rt:
			tab2d[r][rr] = '*'
	elif r==1 or r==2:
		for rr in rt1:
			tab2d[r][rr] = '*'
	elif r==4:
		for rr in rt2:
			tab2d[r][rr] = '*'
	elif r==5:
		for rr in rt3:
			tab2d[r][rr] = '*'
	else:
		for rr in rt4:
			tab2d[r][rr] = '*'

#  WYPISANIE NA EKRAN
for i in range(row):
	for j in range(col):
		if j<27:
			print(tab2d[i][j],end='')
		else:
			print(tab2d[i][j],end='\n')
			
			
	

