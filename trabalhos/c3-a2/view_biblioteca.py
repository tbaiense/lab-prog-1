from model_biblioteca import (
    obter_nome_biblioteca,
    obter_nome_livro,
    obter_qtd_bibliotecas,
    obter_qtd_livros,
    obter_emprestimos,
    obter_estoque,
    atualizar_estoque,
    atualizar_emprestimo,
    print_estoques,
    pesquisar_disponibilidade_livro
)


def menu_principal():
    STR_MENU = """1. Gerenciar bibliotecas
2. Gerar relatórios

>>> """

    while True:
        acao_recebida = int(input(STR_MENU))

        match acao_recebida:
            case 1:
                menu_selecionar_biblioteca()
            case 2:
                menu_gerar_relatorios()

def menu_selecionar_biblioteca():
    STR_MENU = "Escolha uma biblioteca para gerenciar:\n"

    for index_biblioteca in range(obter_qtd_bibliotecas()):
        STR_MENU += f" {index_biblioteca + 1}. {obter_nome_biblioteca(index_biblioteca)}\n"

    STR_MENU += "\n0. Voltar\n"
    STR_MENU += "\n>>> "

    while True:
        biblioteca_selecionada = int(input(STR_MENU))

        if biblioteca_selecionada == 0:
            return

        # TODO: validar biblioteca
        menu_gerenciar_biblioteca(biblioteca_selecionada - 1)
   

def menu_gerenciar_biblioteca(index_biblioteca):

    STR_MENU = """\nEstoque de livros:
  1. Acrescentar  
  2. Reduzir 

Empréstimos:
  3. Acrescentar
  4. Reduzir 

0. Voltar

>>> """

    while True:
        print_estoques(index_biblioteca, '-')

        acao = int(input(STR_MENU))

        match acao:
            case 1:
                menu_acrescentar_estoque(index_biblioteca)
            case 2:
                menu_reduzir_estoque(index_biblioteca)
            #case 3:
            #    menu_acrescentar_emprestimos(index_biblioteca)
            #case 4:
            #    menu_reduzir_emprestimos(index_biblioteca)
            case 0:
                return

    
def menu_acrescentar_estoque(index_biblioteca):
    while True:
        print("selecione um dos livros para acrescentar o estoque:\n")
        print_estoques(index_biblioteca)

        str_menu = """\n0. voltar
\n>>> """

        opcao_escolhida = int(input(str_menu))

        if opcao_escolhida == 0:
            return

        index_livro = opcao_escolhida - 1 

        valor_acrescentar = int(input("Qual a quantidade a ser acrescentada (número inteiro)?\n>>> "))

        novo_estoque = valor_acrescentar + obter_estoque(index_biblioteca, index_livro)

        if (not atualizar_estoque(novo_estoque, index_biblioteca, index_livro)):
            print("falha ao atualizar estoque.")
        else:
            print("estoque acrescentado com sucesso!")

    
def menu_reduzir_estoque(index_biblioteca):
    while True:
        print("selecione um dos livros para reduzir o estoque:\n")
        print_estoques(index_biblioteca)

        str_menu = """\n0. voltar
\n>>> """

        opcao_escolhida = int(input(str_menu))

        if opcao_escolhida == 0:
            return

        index_livro = opcao_escolhida - 1 

        valor_reduzir = int(input("Qual a quantidade a ser reduzida (número inteiro)?\n>>> "))

        novo_estoque = obter_estoque(index_biblioteca, index_livro) - valor_reduzir

        if (not atualizar_estoque(novo_estoque, index_biblioteca, index_livro)):
            print("Falha ao atualizar estoque.")
        else:
            print("Estoque reduzido com sucesso!")


def menu_gerar_relatorios():
    print("TODO")

menu_principal()
