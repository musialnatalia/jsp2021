import math

a = int(input("Podaj długość boku 'a' dla trójkąta: "))
b = int(input("Podaj długość boku 'b' dla trójkąta: "))
alfa = int(input("Podaj kąt 'alpha' pomiędzy 'a' i 'b': "))

pole = 0.5 * a * b * math.sin(math.radians(alfa))

print("Pole trójkąta: ", pole)

