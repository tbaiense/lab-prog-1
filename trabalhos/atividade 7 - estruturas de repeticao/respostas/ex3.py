soma_resto = 0

for n in range(1, 201):
    num_entrada = int(input(f"{n}º Número a somar: "))
    resto = num_entrada % 3 
    soma_resto += resto

print("Resultado da soma:", soma_resto)