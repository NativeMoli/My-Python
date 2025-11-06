#!/usr/bin/env python3

import sys

if len(sys.argv)  != 4:
    print ("Використання: python3 Bilkovskyi.py  <lastname> <name> <patronymic>")
    sys.exit(1)

lastname = sys.argv[1]
name = sys.argv[2]
patronymic = sys.argv[3]
print(f"Вітаю, {lastname} {name} { patronymic }!")
