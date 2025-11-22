bibliotecas = [
    'Hermann Berger',
    'Ponto do Alto',
    'Victorio Bravim',
    'Francisco Nascimento'
]

livros = [
    'Alice no País das Maravilhas',
    'Chapeuzinho Vermelho',
    'Romeu e Julieta'
]

mat_estoques = [ [0] * len(livros) for _ in range(len(bibliotecas)) ]

mat_emprestimos = [ [0] * len(livros) for _ in range(len(bibliotecas)) ]

def obter_nome_biblioteca(index):
    try:
        return bibliotecas[index]
    except IndexError:
        return None 

def obter_nome_livro(index):
    try:
        return livros[index]
    except IndexError:
        return None

def obter_qtd_bibliotecas():
    return len(bibliotecas)

def obter_qtd_livros():
    return len(livros)

def obter_estoque(index_biblioteca, index_livro):
    try:
        return mat_estoques[index_biblioteca][index_livro]
    except IndexError:
        return None

def obter_emprestimos(index_biblioteca, index_livro):
    try:
        return mat_emprestimos[index_biblioteca][index_livro]
    except IndexError:
        return None


def atualizar_estoque(valor, index_biblioteca, index_livro):
    if valor < 0:
        return False# TODO: throw exception -> valor negativo

    emprestimos_atual = obter_emprestimos(index_biblioteca, index_livro) 

    if emprestimos_atual == None:
        return False

    if valor < emprestimos_atual:
        return False # TODO: throw exception -> valor incompatível com empréstimos atuais
   
    try:
        mat_estoques[index_biblioteca][index_livro] = valor
    except IndexError:
        return False

    return True

def atualizar_emprestimo(valor, index_biblioteca, index_livro):
    if valor < 0:
        return False # TODO: throw exception -> valor negativo

    estoque_atual = obter_estoque(index_biblioteca, index_livro)
    
    if estoque_atual == None:
        return False

    if valor > estoque_atual:
        return False # TODO: throw exception -> emprestimos não podem ser superior ao estoque

    try:
        mat_emprestimos[index_biblioteca][index_livro] = valor
    except IndexError:
        return False

    return True

def print_estoques(index_biblioteca, marcador=None):
    print("Estoque de livros da biblioteca:", obter_nome_biblioteca(index_biblioteca))
    
    for index_livro in range(obter_qtd_livros()):
        nome = obter_nome_livro(index_livro) 
        estoque = obter_estoque(index_biblioteca, index_livro)
        emprestimos = obter_emprestimos(index_biblioteca, index_livro)

        print(f'{(marcador if marcador != None else index_livro + 1)} {nome}: {estoque} exemplares', 
              f"({emprestimos} em emprestimo)" if (emprestimos > 0) else "")

def pesquisar_disponibilidade_livro(index_livro, quantia=1):
    disponivel_em = []

    for index_biblioteca in range(len(bibliotecas)):
        estoque = obter_estoque(index_biblioteca, index_livro)

        if estoque < 1:
            continue

        emprestimos = obter_emprestimos(index_biblioteca, index_livro)

        if estoque - emprestimos >= quantia:
            disponivel_em.append(index_biblioteca)

    return disponivel_em
