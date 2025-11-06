#!/usr/bin/env python3
# Bilkovskyi Oleksandr

import sys

if len(sys.argv) != 4:
    print("Використання: python3 calc.py <op> <Number1> <Number2>")
    sys.exit(1)

op = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("ERROR")