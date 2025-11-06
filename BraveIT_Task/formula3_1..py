#!/usr/bin/env python3
# Bilkovskyi Oleksandr

import math

a = float(input ("а невідємне : "))
b = float(input ("b невідємне та не дорівнює 0 : "))

if  a < 0 and b < 0 :
    print ("Числа повинні бути невідємними")
elif b == 0 :
    print ("Число b не може бути 0")
else :
    sqrt = math.sqrt(a * b)
    exp =  math.exp(a)
    exp_lo = exp * b
    half1 = sqrt / exp_lo
    part1 = (2 * a) / b
    part2 = math.exp(part1)
    part3 = a * part2
    half2 = half1 + part3
    print( f"Результат : {half2}")


