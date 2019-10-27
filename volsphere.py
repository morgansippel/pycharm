import math
from fractions import Fraction
radius = float(input("radius?"))
volume = Fraction(4, 3) * math.pi * radius * radius * radius
print(volume)