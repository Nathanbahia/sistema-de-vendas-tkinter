from widgets.table import MyTable
from widgets.label import MyLabel
from widgets.entry import MyEntry
from widgets.button import MyButton
from widgets.option import MyOption

from bancodedados import *
from tkinter import *


banco = Banco()


class App:    
    def __init__(self):
        self.bgPadrao = "#484848"
        self.fgPadrao = "#dddddd"
        self.fontePadrao = "Helvetica 11"
        self.bgFaixa = "#6B8E23"

        self.temaClaro = "#cccccc"
        self.temaEscuro = "#484848"

        self.bgButtonConfirm = "#FFD700"
        self.bgButtonSearch = "#00FF7F"
        self.bgButtonEdit = "#388e3c"
        self.bgButtonCancel = "#B22222"
       
        self.master = Tk()        
        self.master.title("Python")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry(f"{self.width}x{self.height}")        
        self.master.configure(background=self.bgPadrao)

        self.criaTitulo("")

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.menuGeral = Menu(self.menu, tearoff=False)        
        self.menu.add_cascade(label="Geral", menu=self.menuGeral)        
        self.menuGeral.add_command(label="Clientes", command=self.clientes)
        self.menuGeral.add_command(label="Produtos", command=self.produtos)
        self.menuGeral.add_command(label="Seções", command=self.categorias)
        self.menuGeral.add_command(label="Vendas", command=self.vendas)
        self.menuGeral.add_command(label="Estoque", command=self.estoques)

        self.menuConfig = Menu(self.menu, tearoff=False)        
        self.menu.add_cascade(label="Configurações", menu=self.menuConfig)        
        self.temaConfig = Menu(self.menuConfig, tearoff=False)                
        self.menuConfig.add_cascade(label="Tema", menu=self.temaConfig)                
        self.temaConfig.add_command(label="Claro", command=lambda: self.alteraTema("claro"))
        self.temaConfig.add_command(label="Escuro", command=lambda: self.alteraTema("escuro"))                
        
        self.menuSobre = Menu(self.menu, tearoff=False)        
        self.menu.add_cascade(label="Sobre", menu=self.menuSobre)        
        self.menuSobre.add_command(label="Desenvolvedor", command=self.sobre)        

        self.menuSair = Menu(self.menu, tearoff=False)        
        self.menu.add_cascade(label="Sair", menu=self.menuSair)        
        self.menuSair.add_command(label="Sair", command=lambda:self.master.destroy())       

    def criaTitulo(self, texto):        
        faixa = Frame(self.master)
        faixa.configure(background=self.bgFaixa)
        faixa.place(x=0, y=0, h=270, w=self.width)

        MyLabel(frame=self.master, texto="NBDev Desenvolvimento de Sistemas", \
                fundo=self.bgFaixa, font_size=24, x=0, y=0, largura=self.width)

        MyLabel(frame=self.master, texto=texto, \
                fundo=self.bgFaixa, font_size=16, x=0, y=40, largura=self.width)        

        # LOGO
        try:
            img = PhotoImage(file="./imagens/python.png")
        except:
            img = PhotoImage(file="../imagens/python.png")
        logo = Label(self.master, image=img, bg=self.bgFaixa)
        logo.image = img
        logo.place(x=20, y=0)


    def clientes(self, busca=None):
        def create_cliente():
            banco.create_cliente(
                nome=nome.entry.get(),
                endereco=endereco.entry.get(),
                telefone=telefone.entry.get(),
                email=email.entry.get(),                
            )
            self.clientes()        

        def busca_cliente():
            busca = banco.busca_cliente(nome.entry.get())                
            self.clientes(busca)


        self.limpaTela()
        self.criaTitulo("Cadastro de Clientes")
        
        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgFaixa, \
            x=270, y=100)        
        nome = MyEntry(frame=self.master, x=380, y=100, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", command=busca_cliente, \
            x=1190, y=100, largura=70, fundo=self.bgButtonSearch)

        MyLabel(frame=self.master, texto="Endereço: ", fundo=self.bgFaixa, \
            x=270, y=140)  
        endereco = MyEntry(frame=self.master, x=380, y=140, largura=880)              

        MyLabel(frame=self.master, texto="Telefone: ", fundo=self.bgFaixa, \
            x=270, y=180)  
        telefone = MyEntry(frame=self.master, x=380, y=180, largura=300)                  

        MyLabel(frame=self.master, texto="E-mail: ", fundo=self.bgFaixa, \
            x=690, y=180)  
        email = MyEntry(frame=self.master, x=780, y=180, largura=300)              
          
        MyButton(frame=self.master, texto="Cadastrar", fundo=self.bgButtonConfirm, \
            x=1090, y=180, largura=170, command=create_cliente)            
        
        tabela = MyTable(frame=self.master, posx=20, posy=300,            
            header={
                'ID': 10,
                'Nome': 40,
                'Telefone': 20,
                'E-mail': 25,
                'Endereço': 40,
                'Selecionar': 15,
            },
            colunas=banco.show_all_clientes() if busca == None else busca
        )               

    def produtos(self, busca=None):
        def create_produto():
            banco.create_produto(
                nome=nome.entry.get(),
                categoria=categoria.var.get(),
                quantidade=quantidade.entry.get(),
                unidade=unidade.var.get()
            )
            self.produtos()

        def busca_produto():
            busca = banco.busca_produto(nome.entry.get())                
            self.produtos(busca)            

        self.limpaTela()
        self.criaTitulo("Cadastro de Produtos")
        
        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgFaixa, x=270, y=100)
        nome = MyEntry(frame=self.master, x=380, y=100, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", x=1190, y=100, largura=70, \
            command=busca_produto, fundo=self.bgButtonSearch)
        
        MyLabel(frame=self.master, texto="Categoria: ", fundo=self.bgFaixa, x=270, y=140)

        CAT = [ c['nome'].upper() for c in banco.show_all_categorias() ]
        CAT.append(None) if len(CAT) == 0 else CAT
        categoria = MyOption(frame=self.master, opcoes= CAT, x=380, y=140, largura=310)        

        MyButton(frame=self.master, texto="+", x=700, y=140, largura=70, \
                 command=self.categorias, fundo=self.bgButtonSearch)
        
        MyLabel(frame=self.master, texto="Unidade: ", fundo=self.bgFaixa, x=780, y=140)
        UNI = ['Unidade', 'Quilo']
        unidade = MyOption(frame=self.master, opcoes=UNI, x=860, y=140, largura=400)
        
        MyLabel(frame=self.master, texto="Quantidade: ", fundo=self.bgFaixa, x=270, y=180)
        quantidade = MyEntry(frame=self.master, x=380, y=180, largura=310)
        
        MyLabel(frame=self.master, texto="Custo: ", fundo=self.bgFaixa, x=780, y=180)
        custo = MyEntry(frame=self.master, x=860, y=180, largura=200)
        
        MyButton(frame=self.master, texto="Cadastrar", x=1070, y=180, \
            largura=190, fundo=self.bgButtonConfirm, command=create_produto)            

        # TABELA        
        tabela = MyTable(frame=self.master, posx=20, posy=300, \
            header={
                'ID': 10,
                'Produto': 40,
                'Seção': 30,
                'Estoque': 10,
                'Unidade': 10,
                'Custo': 10,
                'Preço': 10,
            },
            colunas = banco.show_all_produtos() if busca == None else busca
        )        

    def categorias(self, busca=None):
        def cria_categoria():
            banco.create_categoria(nome=nome.entry.get())  
            self.categorias()                

        def busca_categoria():            
            busca = banco.busca_categoria(nome.entry.get())
            self.categorias(busca)
            
        self.limpaTela()
        self.criaTitulo("Cadastro de Seções")

        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgFaixa, x=270, y=140)
        nome = MyEntry(frame=self.master, x=380, y=140, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", x=1190, y=140, largura=70, \
            command=busca_categoria, fundo=self.bgButtonSearch)

        MyButton(frame=self.master, texto="Voltar", x=380, y=180, \
            largura=100, fundo=self.bgButtonCancel, command=self.produtos)    
    
        MyButton(frame=self.master, texto="Cadastrar", x=490, y=180, \
            largura=100, fundo=self.bgButtonConfirm, command=cria_categoria)  
        
        MyTable(frame=self.master, posx=20, posy=300,
            header={'ID': 10, 'Seção': 90},
            colunas = banco.show_all_categorias() if busca == None else busca
        )                       

    def estoques(self):
        self.limpaTela()
        self.criaTitulo("Estoques")        

        MyLabel(frame=self.master, texto="Seção: ", x=300, y=140, fundo=self.bgFaixa)
        CAT = [ c['nome'].upper() for c in banco.show_all_categorias() ]
        CAT.append(None) if len(CAT) == 0 else CAT
        categoria = MyOption(frame=self.master, opcoes= CAT, x=380, y=140, largura=880) 
        
        # TABELA
        tabela = MyTable(frame=self.master, posx=20, posy=300,
            header={
                'ID': 10,
                'Produto': 30,
                'Seção': 20,
                'Estoque': 10,
                'Unidade': 10,
                'Custo': 10,
                'Preço': 10,
            },
            colunas=[
                {
                'ID': 1,
                'Produto': 'Refrigerante Mantiqueira',
                'Seção': 'Bebidas',
                'Estoque': 20,
                'Unidade': 'Unid',
                'Custo': 2.99,
                'Preço': 5.00,
                }
            ],
        )

    def vendas(self):
        self.limpaTela()
        self.criaTitulo("Vendas")                  

    def limpaTela(self):
        for widget in self.master.winfo_children():
            if not isinstance(widget, Menu):
                widget.destroy()    

    def alteraTema(self, tema):
        if tema == "claro":
            self.bgPadrao = self.temaClaro
            self.fgPadrao = self.temaEscuro
            self.bgFaixa = "#90EE90"
        elif tema == "escuro":
            self.bgPadrao = self.temaEscuro
            self.fgPadrao = self.temaClaro
            self.bgFaixa = "#6B8E23"

        self.master.configure(background=self.bgPadrao)

        for w in self.master.winfo_children():
            if isinstance(w, MyLabel):
                w.fundo = self.bgFaixa
                w.cor = self.fgPadrao
            if isinstance(w, Label):
                w["bg"] = self.bgFaixa
            if isinstance(w, Frame):
                w.configure(background=self.bgFaixa)
        
    def sobre(self):
        self.limpaTela()
        self.criaTitulo("Informações do Sistema")

        MyLabel(frame=self.master, texto="Versão 0.1 - Sitema de Gerenciamento de Vendas", \
                fundo=self.bgPadrao, x=0, y=310, largura=self.width, font_size=24)

        MyLabel(frame=self.master, texto="Desenvolvido por NBDev Desenvolvimento de Sistemas", \
                fundo=self.bgPadrao, x=0, y=360, largura=self.width, font_size=18)        

    def run(self):
        self.master.mainloop()
              

if __name__ == "__main__":
    app = App()
    app.run()
