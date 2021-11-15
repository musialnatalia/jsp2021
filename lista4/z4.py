def ciag(n,a1=1,q=2):
	an = a1 * q**(n-1)
	return an
	
n = 5
print(str(n), "element ciągu geometrycznego: ", ciag(n))
