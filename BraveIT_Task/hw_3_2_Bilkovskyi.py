#!/usr/bin/env python3
# Bilkovskyi Oleksandr

import math

x = float(input("йсне число x:"))
u = float(input("Дійсне число u:"))
q = float(input("Дійсне число q:"))

resultat = (1 / (q * math.sqrt(2 * math.pi))) * math.exp(-((x - u) ** 2) / (2 * q ** 2))
print(f"Результат обчислення формули : {resultat}")

