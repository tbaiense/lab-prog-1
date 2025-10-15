total_aprovados = 0
total_reprovados = 0
soma_total_das_medias = 0

for a in range(50):
    matricula = input("Matrícula: ")
    nota_1 = float(input("1º nota: "))
    nota_2 = float(input("2º nota: "))

    media = (nota_1 + nota_2) / 2
    soma_total_das_medias += media

    print(f"O aluno com matrícula {matricula} obteve a média {media:.1f} e está ", end="")

    if media > 5.0:
        print("APROVADO!\n")
        total_aprovados += 1
    else:
        print("REPROVADO!\n")
        total_reprovados += 1
    
media_turma = soma_total_das_medias / (total_aprovados + total_reprovados)

print(f"\n----- Resumo da turma  -----\nMédia de nota da turma: {media_turma}\nAprovados: {total_aprovados}\nReprovados: {total_reprovados}")