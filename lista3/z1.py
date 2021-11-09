litera = input("Podaj literę: ")

litera = litera.lower()

if litera in ('a', 'e', 'i', 'o', 'u', 'y'):
	print(litera, "to samogłoska.")
else:
	print(litera, "to spółgłoska.") 
	
