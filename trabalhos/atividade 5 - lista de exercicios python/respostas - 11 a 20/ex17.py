'''
Exercício 17 - Cálculo de volume
'''

import math

raio = float(input("Raio da base: "))
altura = float(input("Altura: "))

volume = math.pi * math.pow(raio, 2) * altura

print(f"Volume: {volume}")
