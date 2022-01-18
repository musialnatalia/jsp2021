from itertools import combinations

class Listy:
	def __init__(self,lista):
		self.lista = lista
	
	def podlisty(self):
		podlist = []
		for i in range(len(self.lista)+1):
			com = combinations(self.lista, i)
			tmp = []
			for c in com:
				tmp.append(list(c))
			podlist.extend(tmp)
		return podlist
	
def main():
	arr = [1,2,3]
	klasa_list = Listy(arr)
	wyn = klasa_list.podlisty()
	print('Wszystkie podlisty listy {} : {}'.format(arr,wyn))
	
if __name__ == "__main__":
    main()
	

		
