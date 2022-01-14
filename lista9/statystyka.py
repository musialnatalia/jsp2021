import sys
import numpy as np

# z linii komend
if len(sys.argv) > 1:
	dane = [float(s) for s in sys.argv[1].split(",")]
else:
	# z przekierowania do pliku
	for s in sys.stdin:
		s = s.strip()
		dane = [float(d) for d in s.split(',')]

av = np.mean(dane)
war = np.var(dane)
sd = np.std(dane)
print('Dane: ',dane)
print('Średnia: ',av,'\nWariancja: ',war,'\nOdchylenie standardowe: ',sd)
