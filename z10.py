import cmath

z = 0+1j


s = cmath.sin(z)
c = cmath.cos(z)
print(type(c))

print("Część rzeczywista sin(z): ", s.real)
print("Część urojona sin(z): ", s.imag)
print("Część rzeczywista cos(z): ", c.real)
print("Część urojona cos(z): ", c.imag)

a = s**2 + c**2
print("sin^2(z)+cos^2(z) = ", a)
