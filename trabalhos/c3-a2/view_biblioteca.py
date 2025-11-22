#!/usr/bin/python3
import os

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

def clear():
    os.system('cls||clear')

def menu_principal():
    STR_MENU = """1. Gerenciar bibliotecas
2. Gerar relatórios

0. Sair do programa (╥﹏╥)
>>> """

    while True:
        clear()
        acao_recebida = int(input(STR_MENU))

        match acao_recebida:
            case 1:
                menu_selecionar_biblioteca()
            case 2:
                menu_escolher_relatorio()
            case 0:
                exit(0)

def menu_selecionar_biblioteca():
    STR_MENU = "Escolha uma biblioteca para gerenciar:\n"

    for index_biblioteca in range(obter_qtd_bibliotecas()):
        STR_MENU += f" {index_biblioteca + 1}. {obter_nome_biblioteca(index_biblioteca)}\n"

    STR_MENU += "\n0. Voltar\n"
    STR_MENU += "\n>>> "

    while True:
        clear()
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
        clear()
        print_estoques(index_biblioteca, '-')

        acao = int(input(STR_MENU))

        match acao:
            case 1:
                menu_acrescentar_estoque(index_biblioteca)
            case 2:
                menu_reduzir_estoque(index_biblioteca)
            case 3:
                menu_acrescentar_emprestimos(index_biblioteca)
            case 4:
                menu_reduzir_emprestimos(index_biblioteca)
            case 0:
                return

    
def menu_acrescentar_estoque(index_biblioteca):
    while True:
        clear()
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
        clear()
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

def menu_acrescentar_emprestimos(index_biblioteca):
    while True:
        clear()
        print("Selecione um dos livros para acrescentar o número de empréstimos:\n")
        print_estoques(index_biblioteca)

        str_menu = """\n0. voltar
\n>>> """

        opcao_escolhida = int(input(str_menu))

        if opcao_escolhida == 0:
            return

        index_livro = opcao_escolhida - 1 

        valor_acrescentar = int(input("Qual a quantidade a ser acrescentada (número inteiro)?\n>>> "))

        novo_emprestimos = valor_acrescentar + obter_emprestimos(index_biblioteca, index_livro)

        if (not atualizar_emprestimo(novo_emprestimos, index_biblioteca, index_livro)):
            print("Falha ao atualizar empréstimos!.")
        else:
            print("Empréstimo acrescentado com sucesso!")

def menu_reduzir_emprestimos(index_biblioteca):
    while True:
        clear()
        print("Selecione um dos livros para reduzir o número de empréstimos:\n")
        print_estoques(index_biblioteca)

        str_menu = """\n0. voltar
\n>>> """

        opcao_escolhida = int(input(str_menu))

        if opcao_escolhida == 0:
            return

        index_livro = opcao_escolhida - 1 

        valor_reduzir = int(input("Qual a quantidade a ser reduzida (número inteiro)?\n>>> "))

        novo_emprestimos = obter_emprestimos(index_biblioteca, index_livro) - valor_reduzir

        if (not atualizar_emprestimo(novo_emprestimos, index_biblioteca, index_livro)):
            print("Falha ao atualizar empréstimos.")
        else:
            print("Empréstimo reduzido com sucesso!")


def menu_escolher_relatorio():
    STR_MENU = """Selecione qual relatório deseja realizar: 

1. Pesquisar disponibilidade de livro

0. Voltar

>>> """

    while True:
        clear()
        opcao_escolhida = int(input(STR_MENU))

        match opcao_escolhida:
            case 1:
                menu_relatorio_disponibilidade()
            case 0:
                return


def menu_relatorio_disponibilidade():
    while True:
        STR_MENU = "Selecione um dos livros para pesquisar a disponibilidade:\n"

        for index_livro in range(obter_qtd_livros()):
            STR_MENU += f'{index_livro + 1}. {obter_nome_livro(index_livro)}\n'            

        STR_MENU += "\n0. Voltar\n>>> "

        clear()
        opcao_escolhida = int(input(STR_MENU))

        if opcao_escolhida == 0:
            return

        index_livro = opcao_escolhida - 1

        disponivel_em = pesquisar_disponibilidade_livro(index_livro)

        if len(disponivel_em) == 0:
            STR_DISPONIBILIDADE = "Este livro está indisponível!"
        else:
            STR_DISPONIBILIDADE = "O livro pesquisado está disponível nas seguintes bibliotecas:\n\n"
            for index_biblioteca in disponivel_em:
               STR_DISPONIBILIDADE += f'- {obter_nome_biblioteca(index_biblioteca)}\n'

        STR_DISPONIBILIDADE += '\nPressione qualquer tecla para voltar...\n>>> '

        input(STR_DISPONIBILIDADE)
        
menu_principal()
