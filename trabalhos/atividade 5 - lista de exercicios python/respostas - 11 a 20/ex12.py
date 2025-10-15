'''
Exercício 12 - Cálculo de consumo médio
'''

distancia = float(input("Insira a distância percorrida em km: \n>>> "))
combustivel_gasto = float(input("Agora, quantos litros de combustível foram consumidos: \n>>> "))

consumo = distancia / combustivel_gasto

print(f"\nConsumo médio: {round(consumo,2)} km/l")
