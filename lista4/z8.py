def suma(n):
    k = 1
    s = 0
    for k in range(1, n+1):
        s = s + 1/k;
    return s;
 

n = 5
print("Suma "+str(n)+" pierwszych elementów szeregu harmonicznego: ", suma(n))
