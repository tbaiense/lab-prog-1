total_folha = 0
num_empregados = 0

while True:
    matricula = int(input("---- Funcionário ----\nMatrícula (0 para finalizar): "))
    
    if matricula == 0:
        break

    salario_dia = float(input("Salário dia: R$ "))
    dias_trabalhados = int(input("Dias trabalhadoos: "))
    salario_mensal = salario_dia * dias_trabalhados

    print(f"\nSalário mensal do funcionário {matricula}: R$ {salario_mensal:.2f}\n")

    total_folha += salario_mensal
    num_empregados += 1

print(f"\n----- Estatísticas -----")
print(f"Média da folha: R$ {(total_folha / num_empregados):.2f}")
print(f"Total da folha de pagamento: R$ {total_folha:.2f}")
