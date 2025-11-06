#!/usr/bin/env python3
# Bilkovskyi Oleksandr

growth = float (input ( "Підскажіть ваш ріст в метрах : "))

weight = float (input ( "Зазначте свою вагу в к.г : "))

bmi = weight / ( growth ** 2)

print(f"Індекс маси тіла становить: { bmi } ")