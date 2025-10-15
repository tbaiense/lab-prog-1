qtd_alturas = 1000 

soma_alturas = 0
acima_160 = 0
abaixo_130 = 0


for p in range(qtd_alturas):
    altura = float(input(f"{p + 1}º Altura: "))

    soma_alturas += altura

    if p == 0:
        menor_altura = altura
        maior_altura = altura
    else: 
        if altura > maior_altura:
            maior_altura = altura
        elif altura < menor_altura:
            menor_altura = altura

    if altura > 1.60:
        acima_160 += 1
    elif altura < 1.30:
        abaixo_130 += 1
    
print("\n----- Estatísticas -----") 
print(f"Maior altura: {maior_altura}")
print(f"Menor altura: {menor_altura}")
print(f"Média de altura: {(soma_alturas / qtd_alturas):.2f}")
print(f"Alturas > 1.60m: {acima_160}")
print(f"Alturas < 1.30m: {abaixo_130}")

 