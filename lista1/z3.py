import math

a = float(input("Podaj długość boku 'a' dla trójkąta: "))
b = float(input("Podaj długość boku 'b' dla trójkąta: "))
alfa = float(input("Podaj kąt 'alpha' pomiędzy 'a' i 'b': "))

pole = 0.5 * a * b * math.sin(math.radians(alfa))

print("Pole trójkąta: ", pole)

