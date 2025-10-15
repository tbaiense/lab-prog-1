maior_altura = 0
mulheres_altas = 0
soma_altura_mulheres30 = 0
cont_mulheres30 = 0

for m in range(100):
    altura = float(input(f"----- {m + 1}ª Pessoa -----\nAltura (em metros): "))
    
    while True:
        sexo = input("Sexo (M ou F): ").upper()

        if sexo != "F" and sexo != "M":
            print("Valor não reconhecido para sexo. Tente novamente...")
        else:
            break

    idade = int(input("Idade: "))
    
    if altura > maior_altura:
        maior_altura = altura

    if sexo == "F":
        if altura >= 1.70:
            mulheres_altas += 1 
        
        if idade > 30:
            soma_altura_mulheres30 += altura
            cont_mulheres30 += 1
        
print(f"\n----- Estatísticas -----\nMaior altura: {maior_altura:.2f}\nMulheres altas: {mulheres_altas}\nMédia de altura de mulheres com mais de 30 anos: {(soma_altura_mulheres30 / 100):.2f}")
    
    
