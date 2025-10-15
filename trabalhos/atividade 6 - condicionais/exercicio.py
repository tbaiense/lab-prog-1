# 19

qtd_calcados = int(input("Quantos calçados você está comprando? "))

valor_calcado = 49.90
total_parcial = valor_calcado * qtd_calcados

if qtd_calcados < 3:
    desconto = 0.05 
else:
    desconto = 0.15

total_final = total_parcial - (total_parcial * desconto)

print(f"""
\nValor sem desconto: R$ {total_parcial:.2f}    
Valor com desconto: R$ {total_final:.2f}
""")
