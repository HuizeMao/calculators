import cmath
from math import sqrt
a = float(input("enter a of the quadratic function: "))
b = float(input("enter b of the quadratic function: "))
c = float(input("enter c of the quadratic function: "))

firstTerm = -b/(2*a)
DiscriminantTerm = cmath.sqrt(b**2 - 4*a*c)/(2*a)
x1 = firstTerm + DiscriminantTerm
x2 = firstTerm - DiscriminantTerm
x1 = round(x1.real,3) + round(x1.imag,5) * 1j
x2 = round(x2.real,3) + round(x2.imag,5) * 1j

print("Rounded results: x1: {} x2: {}".format(x1,x2))
