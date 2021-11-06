wiel3 = list(range(3,100,3))
print("Wielokrotności 3: ", wiel3)
del wiel3[4::3]
print(wiel3)
artm = sum(wiel3)/len(wiel3)
print("Średnia arytmetyczna listy: ", artm)
