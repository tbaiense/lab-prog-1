idade = int(input("Digite sua idade: "))

if idade < 12:
    classificacao = "crianca"
elif idade < 18:
    classificacao = "adolescente" 
elif idade < 60:
    classificacao = "adulto"
else:
    classificacao = "idoso"

print(f"Você é {classificacao}") 
