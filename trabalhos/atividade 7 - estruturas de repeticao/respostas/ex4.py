soma = 0
qtd_inseridos = 0

print("Para interromper a soma, digite '-1'.\n")
while True:
    num_inserido = float(input(f"Insira o {qtd_inseridos + 1}º número: "))

    if num_inserido == -1:
        break
    else:
        soma += num_inserido
        qtd_inseridos += 1

if qtd_inseridos != 0:
    media = soma / qtd_inseridos
    print(f"Média calculada: {media:.2f}")