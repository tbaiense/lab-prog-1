'''
Exercício 18 - Câmbio real-dólar
'''

cotacao = float(input("Cotação atual do dólar: "))
reais = float(input("Reais a converter: R$ "))

dolares = reais / cotacao

print(f"\nDólares: US$ {round(dolares,2)}")
