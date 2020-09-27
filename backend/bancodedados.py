from datetime import datetime
from classes import Categoria
import re
import sqlite3


class Banco:
    def __init__(self):
        self.conn = sqlite3.connect("./database/bancodedados.db")
        self.cursor = self.conn.cursor()

    # CLIENTES
    def create_table_clientes(self):
        """
        Função que cria a tabela de clientes nos banco de dados
        caso ainda não exista quando este arquivo for executado.
        """
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL            
        )
        """
        self.cursor.execute(query)
        self.conn.commit()
        print("Tabela de clientes criada com sucesso!")

    def create_cliente(self, nome, telefone, email, endereco):
        query = f"""
        INSERT INTO clientes (nome, telefone, email, endereco)
        VALUES ('{nome}','{telefone}','{email}','{endereco}')
        """
        self.cursor.execute(query)
        self.conn.commit()
        print(f"Cliente {nome} cadastrado com sucesso!")

    def busca_cliente(self, nome):
        query = "SELECT * FROM clientes"
        clientes = [ 
            {
                'id': c[0],
                'nome': c[1],
                'telefone': c[2],
                'email': c[3]
            } for c in self.cursor.execute(query).fetchall() if re.findall(nome, c[1].upper())]
        return clientes

    def show_all_clientes(self):
        query = "SELECT * FROM clientes"
        clientes = [ 
            {
                'id': c[0],
                'nome': c[1],
                'telefone': c[2],
                'email': c[3]
            } for c in self.cursor.execute(query).fetchall()
        ]
        return clientes

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

    def create_categoria(self, nome, user):
        """
        Função que cria um novo registro de categoria no banco de dados
        """
        secao = Categoria(nome=nome, user=user)
        query = f"INSERT INTO categorias (nome, criacao, alteracao, criador, alterador, \
ativa) VALUES ('{secao.nome}', '{secao.criacao}', '{secao.alteracao}', '{secao.usuario}', \
'{secao.usuario}', 1)"        

        self.cursor.execute(query)
        self.conn.commit()
        print(f"Seção {nome} criada com sucesso!")

    def show_all_categorias(self):
        """
        Função que exibe todas as categorias cadastradas no bando de dados
        """
        query = "SELECT * FROM categorias WHERE ativa=1"
        categorias = [
            {
                'id': c[0],
                'nome': c[1]
            } for c in self.cursor.execute(query).fetchall()
        ]               
        return categorias        

    def busca_categoria(self, nome):        
        query = "SELECT * FROM categorias"
        retorno = self.cursor.execute(query)
        categorias = [{
                'id': c[0],
                'nome': c[1]
            } for c in retorno.fetchall() if re.findall(nome, c[1].upper())]
        return categorias

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
    banco.create_table_clientes()
    banco.create_table_categorias()
    banco.create_table_produtos()
