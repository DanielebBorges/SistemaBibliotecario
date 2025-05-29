from collections import deque

livros = [
    {'Codigo do Livro': '0001', 'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula'},
    {'Codigo do Livro': '0002', 'titulo': 'Percy Jackson e o Ladrão de Raios', 'ano': '2005', 'autor': 'Rick Riordan', 'genero': 'Fantasia'},
    {'Codigo do Livro': '0003', 'titulo': 'A Seleção', 'ano': '2012', 'autor': 'Kiera Cass', 'genero': 'Romance Distópico'},
    {'Codigo do Livro': '0004', 'titulo': 'Memórias Póstumas de Brás Cubas', 'ano': '1881', 'autor': 'Machado de Assis', 'genero': 'Romance'}
]

leitores = [
    ['Ana Souza', '111.222.333-44', '(11) 98765-4321'],
    ['Carlos Lima', '555.666.777-88', '(21) 91234-5678'],
    ['Beatriz Santos', '999.888.777-66', '(31) 99876-5432']
]

emprestimos = {
    '0001': deque(),
    '0002': deque(),
    '0003': deque(),
    '0004': deque()
}

disponibilidade = {
    '0001': True,
    '0002': True,
    '0003': True,
    '0004': True
}

historico = []

def listar_livros():
    print("\nCatálogo de Livros:")
    for livro in livros:
        print(livro)

def adicionar_livro(codigo, titulo, ano, autor, genero, emprestimos, disponibilidade):
    for livro in livros:
        if livro['Codigo do Livro'] == codigo:
            print(f"\nErro: Já existe um livro com o código {codigo}.")
            return
    novo_livro = {
        'Codigo do Livro': codigo,
        'titulo': titulo,
        'ano': ano,
        'autor': autor,
        'genero': genero
    }
    livros.append(novo_livro)
    emprestimos[codigo] = deque()
    disponibilidade[codigo] = True
    
    print(f"\nLivro '{titulo}' adicionado com sucesso.")

def listar_leitores():
    if leitores:
        print("\nLista de Leitores:")
        for leitor in leitores:
            print(f"Nome: {leitor[0]}, CPF: {leitor[1]}, Telefone: {leitor[2]}")
    else:
        print("Nenhum leitor cadastrado.")

def adicionar_leitor():
    nome = input("Nome do leitor: ")
    cpf = input("CPF do leitor (xxx.xxx.xxx-xx): ")
    telefone = input("Telefone do leitor: ")

    for leitor in leitores:
        if leitor[1] == cpf:
            print(f"Erro: CPF {cpf} já cadastrado para o leitor {leitor[0]}.")
            return
    
    leitores.append([nome, cpf, telefone])
    print(f"Leitor '{nome}' cadastrado com sucesso.")

def solicitar_emprestimo(codigo, leitor):
    if codigo not in emprestimos:
        print(f"Erro: Livro com código {codigo} não existe.")
        return
    emprestimos[codigo].append(leitor)
    print(f"{leitor} entrou na fila para o livro {codigo}.")
    if disponibilidade[codigo] and emprestimos[codigo][0] == leitor:
        emprestar_livro(codigo)

def emprestar_livro(codigo):
    if codigo not in emprestimos:
        print(f"Erro: Livro com código {codigo} não existe.")
        return
    leitor = emprestimos[codigo][0]
    disponibilidade[codigo] = False
    for livro in livros:
        if livro['Codigo do Livro'] == codigo:
            titulo = livro['titulo']
            break
    historico.append((titulo, leitor))
    print(f"Livro {codigo} emprestado para {leitor}.")

def devolver_livro(codigo):
    if codigo not in emprestimos:
        print(f"Erro: Livro com código {codigo} não existe.")
        return
    if not emprestimos[codigo]:
        print("Nenhum leitor na fila.")
        return
    leitor = emprestimos[codigo].popleft()
    print(f"{leitor} devolveu o livro {codigo}.")
    if emprestimos[codigo]:
        emprestar_livro(codigo)
    else:
        disponibilidade[codigo] = True

def mostrarHistorico():
    if historico:
        qtd = {}
        for item in historico:
            titulo = item[0]
            if titulo in qtd:
                qtd[titulo] += 1
            else:
                qtd[titulo] = 1

        print("\nHistórico de empréstimos:")
        for titulo, quantidade in qtd.items():
            print(f"Livro: {titulo}, Total de empréstimos: {quantidade}")
    else:
        print("\nHistórico está vazio.")

def desfazer_ultimo_emprestimo():
    if not historico:
        print("Nenhum empréstimo para desfazer.")
        return

    titulo, leitor = historico.pop()
    codigo = None
    
    for livro in livros:
        if livro['titulo'] == titulo:
            codigo = livro['Codigo do Livro']
            break
    else:
        print("Livro não encontrado no sistema.")
        return

    if codigo in emprestimos:
        fila_emprestimos = emprestimos[codigo]
    else:
        fila_emprestimos = []
    
    if fila_emprestimos and fila_emprestimos[0] == leitor:
        fila_emprestimos.popleft() 
        if fila_emprestimos:
            emprestar_livro(codigo) 
        else:
            disponibilidade[codigo] = True 
        print(f"Empréstimo de '{titulo}' para {leitor} desfeito. Estado do sistema atualizado.")
    else:
        print(f"Empréstimo de '{titulo}' para {leitor} removido do histórico.")

while True:
    print("\nMENU SISTEMA BIBLIOTECARIO")
    print("1 - Listar livros")
    print("2 - Adicionar livro")
    print("3 - Listar leitores")
    print("4 - Adicionar leitor")
    print("5 - Solicitar empréstimo")
    print("6 - Devolver livro")
    print("7 - Mostrar histórico")
    print("8 - Desfazer último empréstimo")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        listar_livros()

    elif opcao == '2':
        codigo = input("Código do Livro: ")
        titulo = input("Título: ")
        ano = input("Ano: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        adicionar_livro(codigo, titulo, ano, autor, genero, emprestimos, disponibilidade)

    elif opcao == '3':
        listar_leitores()

    elif opcao == '4':
        adicionar_leitor()

    elif opcao == '5':
        leitor = input("Nome do leitor: ")
        codigo = input("Código do livro: ")
        solicitar_emprestimo(codigo, leitor)

    elif opcao == '6':
        codigo = input("Código do livro: ")
        devolver_livro(codigo)

    elif opcao == '7':
        mostrarHistorico()

    elif opcao == '8':
        desfazer_ultimo_emprestimo()

    elif opcao == '9':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
