from backend.classes import Categoria
from datetime import datetime
import sqlite3


class Banco:
    def __init__(self):
        self.conn = sqlite3.connect("./database/bancodedados.db")
        self.cursor = self.conn.cursor()

    # CATERORIAS

    def create_table_categorias(self):
        """
        Função que cria a tabela de categorias nos banco de dados
        caso ainda não exista quando este arquivo for executado.
        """

        query = """
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            criacao TEXT NOT NULL,
            alteracao TEXT NOT NULL,
            criador TEXT NOT NULL,
            alterador TEXT NOT NULL,
            ativa INTEGER NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()
        print("Tabela de categorias criada com sucesso!")

    def show_all_categorias(self):
        """
        Função que exibe todas as categorias cadastradas no bando de dados
        """
        lista_categorias = []
        query = "SELECT * FROM categorias WHERE ativa=1"
        categorias = self.cursor.execute(query)                
        for cat in categorias.fetchall():
            indice, nome, criacao, alteracao = cat[:4]
            lista_categorias.append((indice, nome, criacao, alteracao))            
        return lista_categorias

    def create_categoria(self, nome, user):
        """
        Função que cria um novo registro de categoria no banco de dados
        """        
        secao = Categoria(nome=nome, usuario=user)
        query = f"INSERT INTO categorias (nome, criacao, alteracao, criador, alterador, \
ativa) VALUES ('{secao.nome}', '{secao.criacao}', '{secao.alteracao}', '{secao.usuario}', \
'{secao.usuario}', 1)"        

        self.cursor.execute(query)
        self.conn.commit()
        print(f"Seção {nome} criada com sucesso!")

    def select_categoria(self):
        """
        Função que exibe todas as categorias registradas no banco de dados
        e retorna a categoria selecionada através do índice
        """
        print("\nTodas categorias cadastradas: \n")
        self.show_all_categorias()
        indice = int(input("Digite o índice da categoria desejada: "))
        query = f"SELECT * FROM categorias WHERE id={indice}"
        cat = self.cursor.execute(query).fetchone()
        indice = cat[0]
        secao = Categoria(nome=cat[1], usuario=cat[4])
        secao.criacao = cat[2]
        secao.alteracao = cat[3]
        print(indice, secao)
        return indice

    def edit_categoria(self, user):        
        """
        Função que altera nome de categoria já registrada no banco de dados
        """

        indice = self.select_categoria()
        nome = input("[ATUALIZAÇÃO] Digite o nome da seção: ")
        data = datetime.now().date()
        query = f"UPDATE categorias SET nome='{nome}', alteracao='{data}', \
alterador='{user}' WHERE id = {indice}"
        self.cursor.execute(query)
        self.conn.commit()
        print("Seção atualizada com sucesso!")

    def delete_categoria(self, user):
        """
        Função que deleta registro do banco de dados
        """

        indice = self.select_categoria()        
        query = f"UPDATE categorias SET ativa=0, alterador='{user}' WHERE id = {indice}"
        self.cursor.execute(query)
        self.conn.commit()
        print("Seção removida com sucesso!")

    # PRODUTO
    def create_table_produtos(self):
        """
        Função que cria a tabela de produtos nos banco de dados
        caso ainda não exista quando este arquivo for executado.
        """
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade REAL NOT NULL,
            unidade TEXT NOT NULL,            
            criacao TEXT NOT NULL,
            alteracao TEXT NOT NULL,
            criador TEXT NOT NULL,
            alterador TEXT NOT NULL,
            ativa INTEGER NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()
        print("Tabela de produtos criada com sucesso!")

    def create_produto(self, nome, categoria, quantidade, unidade, usuario):
        data = datetime.now().date()
        query = f"""
        INSERT INTO produtos (nome, categoria, quantidade, unidade, criacao, \
alteracao, criador, alterador, ativa) VALUES ('{nome}', '{categoria}', {quantidade}, \
'{unidade}', '{data}', '{data}', '{usuario}', '{usuario}', 1)        
        """
        self.cursor.execute(query)
        self.conn.commit()
        print(f"Produto {nome} cadastrado com sucesso!")
        

if __name__ == "__main__":
    banco = Banco()
    banco.create_table_categorias()
    banco.create_table_produtos()
