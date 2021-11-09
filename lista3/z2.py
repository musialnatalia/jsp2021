## ----- CZĘŚĆ 1 ------ ##

a = int(input("Podaj liczbę całkowitą: "))

if (a % 2) == 0:  
   print(a, "jest liczbą parzystą")  
else:  
   print(a, "jest liczbą nieparzystą") 
   

## ----- CZĘŚĆ 2 ------ ##
while ((a % 2) == 0):
	print(a, "jest liczbą parzystą")
	exit() 
else:  
	print(a, "jest liczbą nieparzystą")
	exit()
