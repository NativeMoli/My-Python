#!/usr/bin/env python3
# Bilkovskyi Oleksandr


from decimal import Decimal, ROUND_HALF_UP

salary = Decimal(input("Введіть суму:"))

#Податки
fizical = Decimal ('0.18')
war = Decimal ('0.015')

it_fizical = (salary * fizical).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
it_war = (salary * war).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f" Податок фізичних осьб(18%): {it_fizical}")
print(f" Військовий збір(1.5%):  {it_war}")