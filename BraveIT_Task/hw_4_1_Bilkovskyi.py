#!/usr/bin/env python3
# Bilkovskyi Oleksandr


h, w = map(float, input("Введіть висоту і ширину дверей: ").split())
a, b, c = map(float, input("Введіть три розміри коробки: ").split())

door = sorted([h, w])
box = sorted([a, b, c])

if (box[0] <= door[0] and box[1] <= door[1]):
    print(" Коробка проходить через двері.")
else:
    print(" Коробка не проходить через двері.")