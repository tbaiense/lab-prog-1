media = 0
soma = 0
qtd_total = 0
qtd_pos = 0
qtd_neg =  0
perc_neg = 0

while True:
    num_inserido = float(input(f"{qtd_total + 1}º número (0 para finalizar): "))

    if num_inserido == 0:
        break

    soma += num_inserido

    if num_inserido < 0:
        qtd_neg += 1
    else:
        qtd_pos += 1

    qtd_total += 1

if qtd_total != 0:
    media = soma / qtd_total
    perc_neg = qtd_neg / qtd_total

print(f"""
Valor médio: {media:.2f}      
Qtd. positivos: {qtd_pos}
Porcentagem de negativos: {(perc_neg * 100):.2f} %
""")