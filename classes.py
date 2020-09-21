""" Criação das classes do sistema """

from datetime import datetime

class Base:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__criacao = datetime.now().date()
        self.__alteracao = datetime.now().date()

    @property
    def criacao(self):
        return self.__criacao

    @criacao.setter
    def criacao(self, data):
        self.__criacao = data

    @property
    def alteracao(self):
        return self.__alteracao
        
    @alteracao.setter
    def alteracao(self, data):
        self.__alteracao = data


class Usuario:
    def __init__(self, nome, senha):        
        self.__nome = nome
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome
    
    def __str__(self):
        return self.nome



class Categoria(Base):
    def __init__(self, nome, usuario):
        super().__init__(usuario)
        self.__usuario = usuario
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def usuario(self):
        return self.__usuario

    def __str__(self):
        return f"|{self.nome} | {self.criacao} | {self.alteracao} | {self.usuario}"


class Produto(Base):
    def __init__(self, nome, categoria, quantidade, unidade, usuario):
        super().__init__(usuario)
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidade = unidade
        self.usuario = usuario        

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Categoria: {self.categoria}
        Estoque: {self.quantidade}
        Unidade: {self.unidade}
        Cadastro: {self.criacao}
        Alteração: {self.alteracao}
        Usuário: {self.usuario.nome}        
        """
