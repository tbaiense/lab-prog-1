num_final = int(input("Somar até: "))

num_somar = 1
soma = 0

qtd_somar = abs(num_final - num_somar) + 1

if num_final > 0: 
    incremento = 1
else:
    incremento = -1

while qtd_somar > 0:
    soma += num_somar
    num_somar += incremento
    qtd_somar -= 1


print("A soma calculada foi:", soma)