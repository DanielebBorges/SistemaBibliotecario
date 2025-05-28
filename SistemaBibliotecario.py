from collections import deque

livros = [
    {'Codigo do Livro': '0001', 'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula'},
    {'Codigo do Livro': '0002', 'titulo': 'Percy Jackson e o Ladrão de Raios', 'ano': '2005', 'autor': 'Rick Riordan', 'genero': 'Fantasia'},
    {'Codigo do Livro': '0003', 'titulo': 'A Seleção', 'ano': '2012', 'autor': 'Kiera Cass', 'genero': 'Romance Distópico'},
    {'Codigo do Livro': '0004', 'titulo': 'Memórias Póstumas de Brás Cubas', 'ano': '1881', 'autor': 'Machado de Assis', 'genero': 'Romance'}
]

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
