
# Sistema Bibliotecario

Esse sistema em Python simula uma biblioteca simples, com funcionalidades para gerenciar livros, leitores, empréstimos, devoluções, histórico e desfazer empréstimos

## Como executar o sistema?
Você possui duas maneiras de execução:
- Clonando o repositorio com o Git 
- Baixando o projeto na maquina

### Clonando o repositorio
Primeiro, no terminal digite:
```
git clone https://github.com/danielebborges/SistemaBibliotecario.git
```

Depois entre na pasta do Sistema Bibliotecario com:
```
cd SistemaBibliotecario
```  
E por fim rode o projeto:
```
python SistemaBibliotecario.py
``` 

### Download (.zip)
A interface, possui um botão verde escrito "code" 
assim como a imagem a baixo:

![Botão](https://res.cloudinary.com/practicaldev/image/fetch/s--vVXcCtiu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qtzts78b6ctikq3b9wa4.png)  
Após clicar em code ira abrir essa janela, e é só clicar em Download ZIP assim como a seta esta indicando     

![Download](https://user-images.githubusercontent.com/101413385/185686126-23339f8c-ecf9-44b8-9c52-996c50750254.png)

Depois é só descompactar o aquivo clicando com o botão direito na pasta que acabou de ser feito o Download, e abrir o aquivo **SistemaBibliotecario.py** no VSCode ou outra plataforma que preferir, e por fim executar o codigo no VSCode, tera um triangulo na parte superior a direita é só clicar que abrira direto ja funcionando. Caso prefirir pode rodar pela aba terminal no VSCode tambem, apos clicar o terminal abrira e é só digitar igual o codigo abaixo:
```
python SistemaBibliotecario.py
```
Assim ja estará clonado e poderá utilizar seu codigo como preferir.

## Como o sistema funciona?  
Os **leitores estão classificados em uma estrutura de lista**. A lista externa armazena todos os leitores no geral já as listas internas armazenam cada leitor individualmente, cada lista interna contém 3 elementos sendo eles: Nome, CPF e Telefone. Com essa estrutura é possível acessar seus dados por meio do índice assim como demonstrado nas funções "adicionar_leitor" e "mostrar leitores" usando o nome do elemento com o índice que deseja na frente. Essa estrutura é fácil de ser manipulada e muito pratica para conjuntos pequenos assim como esse com apenas 3 elementos. 

```
leitores = [
    ['Ana Souza', '111.222.333-44', '(11) 98765-4321'],
    ['Carlos Lima', '555.666.777-88', '(21) 91234-5678'],
    ['Beatriz Santos', '999.888.777-66', '(31) 99876-5432']
]
```
**emprestimos** está criando um dicionário onde cada chave representa o código de um livro cadastrado, o valor de cada chave é um deque(), uma fila que armazena os nomes dos leitores que solicitaram um livro. Quando um leitor solicita o empréstimo de um livro, seu nome é adicionado ao final da fila append() e quando o livro está disponível, ele é entregue ao primeiro da fila popleft(), seguindo a lógica FIFO. Utilizamos essa estrutura porque combina dicionários com filas (deque), que são ideais para representar o relacionamento entre livros e leitores  que estão aguardando o empréstimo.

```
emprestimos = {
    '0001': deque(),
    '0002': deque(),
    '0003': deque(),
    '0004': deque()
}
```
A estrutura **disponibilidade** é outro dicionário onde cada chave representa o código de um livro, e o valor booleano (True ou False) mostra se o livro está disponível para empréstimo. Sempre que um livro e emprestado, seu valor altera para False, indicando que ele não pode ser emprestado até ser devolvido, e quando ele é devolvido seu valor volta para True, liberando ele para novos empréstimos. O uso desse dicionário nos ajuda a ter um controle simples e direto da disponibilidade de cada livro. Cada entrada funciona como um status para o livro correspondente, o que torna as verificações no sistema rápidas.
```
disponibilidade = {
    '0001': True,
    '0002': True,
    '0003': True,
    '0004': True
}
```
A variável **histórico** é uma lista utilizada para registrar todos os empréstimos que já foram realizados no sistema. Toda vez que um livro é emprestado para o leitor uma tupla contendo o título do livro e o nome do leitor é adicionado a lista. Por exemplo, após um empréstimo, o histórico pode ficar assim: [('O Pequeno Príncipe', 'Ana Souza'), ('A Seleção', 'Carlos Lima')]. Escolhemos a lista porque os empréstimos precisam ser adicionados ao final da sequência, sem necessidade de busca por chave ou estrutura complexa. O uso de tuplas dentro da lista faz com que cada registro fique compacto e claro, mostrando apenas informações essenciais de forma imutável.
```
historico = []
```

A função **listar leitores**, como o próprio nome indica, exibe todos os leitores cadastrados na lista. O bloco começa com um if que verifica se a lista está vazia. Caso não esteja, o código entra em um for que percorre cada leitor na lista e imprime seus dados na ordem: nome, CPF e telefone, que são obtidos dos índices 0, 1 e 2, respectivamente. Por fim, se a lista estiver vazia, a função informa ao usuário que nenhum leitor está cadastrado.  

```
def listar_leitores():
    if leitores:
        print("\nLista de Leitores:")
        for leitor in leitores:
            print(f"Nome: {leitor[0]}, CPF: {leitor[1]}, Telefone: {leitor[2]}")
    else:
        print("Nenhum leitor cadastrado.")
```

A função **adicionar leitor** tem a entrada via input onde o usuário insere o nome, o cpf e o telefone, assim que o usuário cadastra todos os dados necessários, um for é iniciado para conferir se o cpf já não foi cadastrado, ele percorre os leitores na lista e se o leitor tiver o mesmo cpf que algum outro já cadastrado irá printar que o cpf já está cadastrado no leitor tal. Se o cpf não for encontrado o append vai adicionar o novo leitor na lista de leitores e por fim printar que o leitor foi cadastrado com sucesso.   

```
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
```
A função **solicitar_emprestimo()** é responsável por registrar a solicitação de empréstimo feita por um leitor, ela recebe dois parâmetros o código do livro e o nome do leitor. Primeiro ela verifica se o código informado existe no dicionário, se o código não for encontrado, significa que o livro não está cadastrado, aí ela exibe uma mensagem de erro e encerra. Já se o livro existir, o nome do leitor é adicionado ao final da fila (deque) correspondente aquele livro com o método append(). Em seguida a função verifica dois casos, se o livro está disponível em (disponibilidade[codigo] == True) e se o leitor recém adicionado é o primeiro da fila em (empréstimos[codigo][0] == leitor), se ambas forem verdadeiras significa que o livro pode ser entregue para o leitor, e a função (emprestar_livro(codigo)) é chamada para realizar o empréstimo. Essa função foi criada para gerenciar de forma organizada a entrada dos leitores nas filas de espera dos livros, ela utiliza deque para garantir o funcionamento correto da fila, e o dicionário emprestimos para associar cada livro a sua devida fila. A verificação dupla de disponibilidade e posição na fila garante que o empréstimo seja realizado de forma justa e automática, caso o livro esteja livre. 

```
def solicitar_emprestimo(codigo, leitor):
    if codigo not in emprestimos:
        print(f"Erro: Livro com código {codigo} não existe.")
        return
    emprestimos[codigo].append(leitor)
    print(f"{leitor} entrou na fila para o livro {codigo}.")
    if disponibilidade[codigo] and emprestimos[codigo][0] == leitor:
        emprestar_livro(codigo)
```

**Mostrar histórico** é uma função que verifica se há registros de empréstimos e conta quantas vezes cada livro já foi emprestado. O bloco começa verificando se a lista histórico está vazia ou não. Se não estiver vazia, o código continua. Em seguida, é criado um dicionário chamado qtd que vai guardar as quantidades de empréstimos para cada título.
Depois, um laço for percorre cada item na lista histórico. Cada item é uma tupla com duas informações: o título do livro e o nome do leitor. O código pega o título do livro, que está no índice 0 da tupla (item[0]), e verifica se ele já existe no dicionário qtd. Se já existir, ele soma mais 1 ao valor. Se for a primeira vez que o título aparece, o código adiciona o título ao dicionário com o valor 1.
Depois disso, um segundo for percorre o dicionário qtd. O items() transforma o dicionário em pares de (título, quantidade), e cada par vira uma tupla. Esses dois valores são armazenados nas variáveis título e quantidade. Por fim, o código imprime o nome do livro e o total de vezes que ele foi emprestado.

```
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
```
A função **desfazer_ultimo_emprestimo()** tem como objetivo reverter o último empréstimo registrado no sistema. Ela começa verificando se há algum empréstimo no histórico, se estiver vazio, exibe uma mensagem e retorna. Se houver, ela remove o ultimo item da lista **historico** usando o método pop(), que retorna uma tupla com o titulo do livro e nome do leitor. Em seguida, percorre a lista de livros para descobrir o código correspondente aquele título. Com o codigo do livro, a função acessa a fila de emprestimos (deque) associada a esse livro no dicionário **emprestimos**, se o leitor que foi removido do historico ainda for o primeiro da fila, ele é retirado da fila com popleft().
```
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
```

O **menu de escolha** do usuário é feito com um laço while True, que mantém o programa em execução até que o usuário deseje sair. Ele começa com os print() das opções disponíveis e um input() para que o usuário insira sua escolha. A cada número escolhido, é chamada a função correspondente. Algumas opções, como 2, 5 e 6, exigem que o usuário forneça mais informações, como dados do livro ou do leitor, e por isso já possuem novos input() dentro delas. O else serve para tratar casos em que o usuário insere um valor incompatível com as opções disponíveis, exibindo uma mensagem de erro. O programa só é encerrado quando a opção '9' é escolhida, nesse momento, é exibida a mensagem "Saindo..." e o laço é interrompido com break.

```
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

```




## Desenvolvido por:
| Alunos | RA | Turma|
| -------- | ----- | ----------- |
|Barbara Luani Rrebechi Santana|     |Turma C|
|Caio Garbin Silva|1988521|Turma C|
|Daniele Barbosa Borges|1989236|Turma C |  
