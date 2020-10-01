from datetime import datetime
import sqlite3
import re


class Banco:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("./database/bancodedados.db")
        except:
            self.conn = sqlite3.connect("../database/bancodedados.db")
        self.cursor = self.conn.cursor()

    # CLIENTES

    def create_table_clientes(self):
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
                'email': c[3],
                'endereco': c[4],
            } for c in self.cursor.execute(query).fetchall() if re.findall(nome, c[1].upper())]
        return clientes

    def show_all_clientes(self):
        query = "SELECT * FROM clientes"
        clientes = [ 
            {
                'id': c[0],
                'nome': c[1],
                'telefone': c[2],
                'email': c[3],
                'endereco': c[4],
            } for c in self.cursor.execute(query).fetchall()
        ]
        return clientes

    # CATERORIAS    

    def create_table_categorias(self):
        query = """
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL
            )
            """
        self.cursor.execute(query)
        self.conn.commit()
        print("Tabela de categorias criada com sucesso!")    

    def create_categoria(self, nome):       
        query = f"INSERT INTO categorias (nome) VALUES ('{nome}')"
        self.cursor.execute(query)
        self.conn.commit()
        print(f"Seção {nome} criada com sucesso!")

    def show_all_categorias(self):
        query = "SELECT * FROM categorias"
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

    # PRODUTO

    def create_table_produtos(self):
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade REAL NOT NULL,
            unidade TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()
        print("Tabela de produtos criada com sucesso!")

    def create_produto(self, nome, categoria, quantidade, unidade):    
        query = f"""
        INSERT INTO produtos (nome, categoria, quantidade, unidade) \
            VALUES ('{nome}', '{categoria}', {quantidade}, '{unidade}')"""
        self.cursor.execute(query)
        self.conn.commit()
        print(f"Produto {nome} cadastrado com sucesso!")

    def busca_produto(self, nome):        
        query = "SELECT * FROM produtos"
        retorno = self.cursor.execute(query)
        produtos = [{
                'id': p[0],
                'nome': p[1],
                'seção': p[2],
                'estoque': p[3],
                'unidade': p[4]
            } for p in retorno.fetchall() if re.findall(nome, p[1].upper())]
        return produtos        

    def show_all_produtos(self):
        query = "SELECT * FROM produtos"            
        produtos = [
            {
                'id': p[0],
                'nome': p[1],
                'seção': p[2],
                'estoque': p[3],
                'unidade': p[4]
            } for p in self.cursor.execute(query).fetchall()
        ]               
        return produtos
        

if __name__ == "__main__":
    banco = Banco()
    banco.create_table_clientes()
    banco.create_table_categorias()
    banco.create_table_produtos()
