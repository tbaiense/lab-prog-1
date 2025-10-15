while True:
    senha = input("Digite sua senha: ")
    if len(senha) < 8:
        print("Senha deve ter 8 ou mais caracteres. Tente novamente...")
    else:
        break
print("Senha definida com sucesso!")