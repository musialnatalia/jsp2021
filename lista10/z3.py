from itertools import combinations

class Nliczb:
	def __init__(self,lista):
		self.lista = lista
	
	def podlisty(self):
		podlist = []
		com = combinations(self.lista, 3)
		tmp = []
		for c in com:
			tmp.append(list(c))
		podlist.extend(tmp)
		pp = []
		for p in podlist:
			s = sum(p)
			if s == 0:
				pp.append(p)
		return pp
		
	
	
def main():
	arr = [1,-1,-2,2,3,-3,4,-4,5,-5,6,-6,7,-7,-8,8,-9,9,0]
	klasa_list = Nliczb(arr)
	wyn = klasa_list.podlisty()
	print('Lista {}'.format(arr))
	print('Wszystkie podlisty, których suma to 0:\n {}'.format(wyn))
	
if __name__ == "__main__":
    main()
	

		

