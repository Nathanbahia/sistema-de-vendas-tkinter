from bancodedados import *


banco = Banco()

user = Usuario(
    nome='nathan',
    senha='123'
)

while True:

    print("""
    [1] PRODUTOS
    [2] SEÇÕES
    [3] CLIENTES
    [4] VENDAS
    """)
    opt = int(input("\nDigite a opção desejada: "))

    if opt == 1:        
        print("""
        [1] CONSULTAR
        [2] CADASTRAR
        [3] EDITAR
        [4] EXCLUIR
        """)

        opt_prod = int(input("\nDigite a opção desejada: "))

        if opt_prod == 2:
            nome = input("Nome: ").upper()
            categoria = input("Categoria: ").upper()
            quantidade = float(input("Quantidade: "))
            unidade = input("Unidade: ").upper()
            usuario = user

            produto = Produto(
                nome=nome,
                categoria=categoria,
                quantidade=quantidade,
                unidade=unidade,
                usuario=usuario
            )

            print(produto)

    if opt == 2:
        print("""
        [1] CONSULTAR
        [2] CADASTRAR
        [3] EDITAR
        [4] EXCLUIR
        """)

        opt_categ = int(input("\nDigite a opção desejada: "))

        if opt_categ == 1:
            banco.show_all_categorias()
        
        elif opt_categ == 2:
            banco.create_categoria(user)

        elif opt_categ == 3:
            banco.edit_categoria(user)

        elif opt_categ == 4:
            banco.delete_categoria(user)
            