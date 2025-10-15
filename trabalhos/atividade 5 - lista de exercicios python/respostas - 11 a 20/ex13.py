'''
Exercício 13 - Cálculo inteiro
'''

print("A seguir, insira dois números inteiros...", end="\n\n")

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor


print(f"\nQuociente: {quociente}\nResto: {resto}")
