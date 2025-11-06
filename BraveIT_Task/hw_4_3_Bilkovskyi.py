#!/usr/bin/env python3
# Bilkovskyi Oleksandr


import math

a, b, c = map(float, input("Enter a, b, c: ").split())
D = b**2 -4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
elif D == 0:
    print(f"x = {-b / (2*a)}")
else:
    print("Without real roots")