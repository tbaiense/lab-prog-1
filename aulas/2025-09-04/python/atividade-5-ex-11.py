soma_notas = 0
qtd_notas = 3

for n in range(qtd_notas):
    soma_notas += float(input(f"Insira a {n + 1} nota: "))

media = soma_notas / qtd_notas

print(f"A média das {qtd_notas} foi: {media:.2f}")