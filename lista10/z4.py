import xml.etree.ElementTree as ET


class Kursy:
	def __init__(self,sciezka):
		self.sciezka = sciezka
		
	def czytaj(self,sciezka):
		root = ET.parse(self.sciezka).getroot()
		return root
		
	def nam(self):
		root = self.czytaj(self.sciezka)
		nazwa = [n.text for n in root.findall('.//nazwa_waluty')]
		return nazwa
		
	def cod(self):
		root = self.czytaj(self.sciezka)
		kod = [k.text for k in root.findall('.//kod_waluty')]
		return kod
		
	def curse(self):
		root = self.czytaj(self.sciezka)
		kurs = [float(kk.text.replace(',','.')) for kk in root.findall('.//kurs_sredni')]
		return kurs 
		
	def dict(self):
		dic1 = {}
		dic2 = {}
		keys1 = self.nam()
		keys2 = self.cod()
		values = self.curse()
		k = 0
		for i in keys1:
			dic1[i] = values[k]
			k += 1
		k = 0
		for i in keys2:
			dic2[i] = values[k]
			k += 1
		return dic1,dic2
			
	def pln(self,v1,wal1,wal2):
		dic1,dic2 = self.dict()
		if wal1 == 'PLN':
			v2 = v1/dic2[wal2]
		else:
			v2 = v1*dic2[wal1]
		return v2
		
	def change(self,v1,wal1,wal2):
		dic1,dic2 = self.dict()
		wal1_pln = v1*dic2[wal1]
		pln_wal2 = wal1_pln/dic2[wal2]
		return pln_wal2
					
				
		
def main(): 
	path = '/home/natalia/2nd/jsp2021/lista10/waluty.xml'
	waluta = Kursy(path)
	lista1 = waluta.nam()
	lista2 = waluta.cod()
	print('Lista dostępnych walut:\n')
	for n,c in zip(lista1,lista2):
		print('{} ({})'.format(n,c))
		
	#	PLN <-> inna waluta	
	w = 'EUR'
	p = 100
	w_pln = waluta.pln(p,'PLN',w)
	print('\nKonwersja {} PLN na {}: {} {}'.format(p,w,w_pln,w))
	
	w = 'EUR'
	p = 100
	w_pln = waluta.pln(p,w,'PLN')
	print('Konwersja {} {} na PLN: {} PLN'.format(p,w,w_pln))
	
	#		waluta <-> waluta
	w1 = 'EUR'
	w2 = 'RUB'
	p = 100
	w_w = waluta.change(p,w1,w2)
	print('Konwersja {} {} na {}: {} {}'.format(p,w1,w2,w_w,w2))
	
	
if __name__ == "__main__":
    main()
	
