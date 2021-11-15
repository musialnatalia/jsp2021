n = 24
m = 18

n_div=[]
m_div=[]

for i in range(1,n+1):
	if n%i == 0:
		n_div.append(i)

for i in range(1,m+1):
	if m%i == 0:
		m_div.append(i)

common = set(m_div).intersection(set(n_div))

print("Największy wspolny dzielnik liczb "+str(n)+', '+str(m)+' : ', max(common))
