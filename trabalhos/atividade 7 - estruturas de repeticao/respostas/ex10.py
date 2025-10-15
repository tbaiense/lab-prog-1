eleitores = 0
votos_cand_1 = 0
votos_cand_2 = 0
votos_cand_3 = 0
votos_nulo = 0
votos_branco = 0

while True:
    voto = int(input(f"""
Candidatos disponíveis:
- 1
- 2
- 3

Em branco = 0 | Nulo = 4
Finalizar votação = -1
>>> Seu voto: """))

    match voto:
        case -1:
            print("\nVotação finalizada!\n===============================================\n")
            break
        case 0:
            votos_branco += 1
        case 1:
            votos_cand_1 += 1
        case 2:
            votos_cand_2 += 1
        case 3:
            votos_cand_3 += 1
        case 4:
            votos_nulo += 1
        case _:
            print("Candidato inválido. Tente novamente...\n")
            continue
    
    eleitores += 1
    print("\nVoto registrado com sucesso!\n===============================================\n")

if eleitores != 0 :
    if votos_cand_1 > votos_cand_2 and votos_cand_1 > votos_cand_3:
        cand_vencedor = 1
    elif votos_cand_2 > votos_cand_1 and votos_cand_2 > votos_cand_3:
        cand_vencedor = 2
    elif votos_cand_3 > votos_cand_2 and votos_cand_3 > votos_cand_1:
        cand_vencedor = 3
    else:
        cand_vencedor = "nenhum"
    
    print("\n\nCandidato vencedor: " + str(cand_vencedor))
    print("Votos nulos: " + str(votos_nulo))
    print("Votos em branco: " + str(votos_branco))
    print("Eleitores: " + str(eleitores))
else:
    print("Nenhum voto foi registrado.") 