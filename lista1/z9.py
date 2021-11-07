import numpy as np
import cmath

z = complex(input("Podaj liczbę zespoloną 'z': "))

print("|z| = ", np.abs(z))
print("arg(z) = ", np.degrees(cmath.phase(z)))
print('conjugate(z) = ', z.conjugate())
