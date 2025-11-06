#!/usr/bin/env python3
# Bilkovskyi Oleksandr

# C = 0 -> 100 ;
# Fa = -32 -> 218 ;  218 - 32 = 180 ;  100/180= 5/9;

Fa = float (input ( "Температура в Fa: "))

Ce =(5/9) * (Fa -32)

print (f"Температура в Ce: {Ce:.2f}")