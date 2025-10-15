while True:
    num_inserido = int(input("Insira um número inteiro maior que 0: "))
    if num_inserido > 0:
        break
    else:
        print("Erro: número deve ser maior que 0.")

fat = 1
multiplicar_por = 1
while multiplicar_por <= num_inserido:
    fat *= multiplicar_por
    multiplicar_por += 1

print("Fatorial calculada:", fat)



