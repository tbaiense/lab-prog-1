'''
Exercício 19 - Cálculo de salário
'''

comissao = 0.15

nome = input("Nome do vendedor: ")

salario_fixo = float(input("Insira seu salário: R$ "))

vendas_mes = float(input("Montante de vendas mensal: R$ "))

salario_final = salario_fixo + vendas_mes * comissao

print(f"\nSalário final do vendedor {nome}: R$ {round(salario_final, 2)}")
