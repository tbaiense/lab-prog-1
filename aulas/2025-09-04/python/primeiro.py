# entrada de dados
nome = input("Insira seu nome: ")
ano = int(input("Digite o ano do seu nascimento: "))

'''
comentário em multilinha
'''
altura = float(input("Qual sua altura: "))

# processamento
idade = 2025 - ano

# saída de dados 
print(f"Seu nome é {nome} e sua idade é {idade}")
print("Sua altura é ", altura, sep=" --> ", end="")
print(" e nasceu em " + str(ano) )