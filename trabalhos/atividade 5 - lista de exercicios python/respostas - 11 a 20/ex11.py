'''
Exercício 11 - Cálculo de média de notas
'''
print("Bem-vindo(a)!\nInsira as notas a seguir no formato '10.0'.", end="\n\n")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Agora, a segunda nota: "))
nota_3 = float(input("Por fim, a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"\nA média calculada foi {round(media, 2)}")
