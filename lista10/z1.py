import numpy as np

class Koło:
	def __init__(self,promien):
		self.promien = promien
	
	def pole(self):
		pole_kola = np.pi * self.promien**2
		return pole_kola
	
	def obwod(self):
		obwod_kola = 2 * np.pi * self.promien
		return obwod_kola

def main():
	r = 5.
	kolo1 = Koło(r)
	ob = kolo1.obwod()
	pol = kolo1.pole()
	print('Pole koła o promieniu {} : {}'.format(r,pol))
	print('Obwód koła o promieniu {} : {}'.format(r,ob))
	
if __name__ == "__main__":
    main()
	
