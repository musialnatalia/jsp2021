from itertools import chain
lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(lista)
lista1 = list(chain.from_iterable(lista))

print(lista1)
