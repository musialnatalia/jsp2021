napis = input("Podaj napis: ")

nlist=list(napis)

nlist.insert(int(len(nlist)/2),'Python')

print("".join(nlist))
