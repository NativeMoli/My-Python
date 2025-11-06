#!/usr/bin/env python3
# Bilkovskyi Oleksandr


n = int(input("Enter a positive number:"))

if n < 2:
    print("The number is not simple")
else:
    for i in  range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("The number is not simple")
            break
    else:
        print("The number is simple")
