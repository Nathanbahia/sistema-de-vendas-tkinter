from tkinter import *
from classes import *
from bancodedados import *
from widgets.table import MyTable
from widgets.label import MyLabel
from widgets.entry import MyEntry
from widgets.button import MyButton
from widgets.option import MyOption


banco = Banco()


class App:    
    def __init__(self):
        self.bgPadrao = "#484848"
        self.fgPadrao = "#dddddd"
        self.fontePadrao = "Helvetica 11"

        self.temaClaro = "#cccccc"
        self.temaEscuro = "#484848"

        self.bgButtonConfirm = "#115293"
        self.bgButtonSearch = "#d32f2f"
        self.bgButtonEdit = "#388e3c"
        self.bgButtonCancel = "#dd8000"

        self.width = 1280
        self.height = 730
        
        self.master = Tk()
        self.master.title("Python")
        self.master.geometry(f"{self.width}x{self.height}")
        self.master.resizable(True, False)
        self.master.configure(background=self.bgPadrao)

        self.criaTitulo("")

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.menuGeral = Menu(self.menu, tearoff=False)        
        self.menu.add_cascade(label="Geral", menu=self.menuGeral)        
        self.menuGeral.add_command(label="Clientes", command=self.clientes)
        self.menuGeral.add_command(label="Produtos", command=self.produtos)
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
        Label(
            self.master,
            text="NBDev Desenvolvimento de Sistemas",
            bg=self.bgPadrao,
            fg=self.fgPadrao,
            font="Helvetica 24 bold").place(x=0, y=0, w=self.width)
        Label(
            self.master,
            text=texto,
            bg=self.bgPadrao,
            fg=self.fgPadrao,
            font="Helvetica 16 bold").place(x=0, y=50, w=self.width)

        # LOGO
        img = PhotoImage(file="./imagens/python.png")
        logo = Label(
            self.master,            
            image=img,            
            bg=self.bgPadrao)
        logo.image = img
        logo.place(x=20, y=20)



    def clientes(self, busca=None):
        def create_cliente():
            banco.create_cliente(
                nome=ent_nome.get(),
                telefone=ent_telefone.get(),
                email=ent_email.get(),
                endereco=ent_endereco.get()
            )
            self.clientes()        

        def busca_cliente():
            busca = banco.busca_cliente(ent_nome.get())                
            self.clientes(busca)


        self.limpaTela()
        self.criaTitulo("Cadastro de Clientes")
        
        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgPadrao, \
            x=270, y=100)        
        nome = MyEntry(frame=self.master, x=380, y=100, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", command=busca_cliente, \
            x=1190, y=100, largura=70)

        MyLabel(frame=self.master, texto="Endereço: ", fundo=self.bgPadrao, \
            x=270, y=140)  
        endereco = MyEntry(frame=self.master, x=380, y=140, largura=880)              

        MyLabel(frame=self.master, texto="Telefone: ", fundo=self.bgPadrao, \
            x=270, y=180)  
        telefone = MyEntry(frame=self.master, x=380, y=180, largura=300)                  

        MyLabel(frame=self.master, texto="E-mail: ", fundo=self.bgPadrao, \
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

    def produtos(self):
        def create_produto():
            banco.create_produto(
                nome=nome.entry.get(),
                categoria=categoria.var.get(),
                quantidade=quantidade.entry.get(),
                unidade=unidade.var.get()
            )
            self.produtos()

        self.limpaTela()
        self.criaTitulo("Cadastro de Produtos")
        

        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgPadrao, x=270, y=100)
        nome = MyEntry(frame=self.master, x=380, y=100, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", x=1190, y=100, largura=70, \
            command=lambda: print("clicado."))
        
        MyLabel(frame=self.master, texto="Categoria: ", fundo=self.bgPadrao, x=270, y=140)

        CAT = [ c['nome'].upper() for c in banco.show_all_categorias() ]
        CAT.append(None) if len(CAT) == 0 else CAT
        categoria = MyOption(frame=self.master, opcoes= CAT, x=380, y=140, largura=200)        

        MyButton(frame=self.master, texto="+", x=590, y=140, command=self.categorias)
        
        MyLabel(frame=self.master, texto="Unidade: ", fundo=self.bgPadrao, x=650, y=140)

        UNI = ['Unidade', 'Quilo']
        unidade = MyOption(frame=self.master, opcoes=UNI, x=730, y=140, largura=200)
        
        MyLabel(frame=self.master, texto="Quantidade: ", fundo=self.bgPadrao, x=270, y=180)
        quantidade = MyEntry(frame=self.master, x=380, y=180, largura=200)
        
        MyLabel(frame=self.master, texto="Custo: ", fundo=self.bgPadrao, x=650, y=180)
        custo = MyEntry(frame=self.master, x=730, y=180, largura=200)
        
        MyButton(frame=self.master, texto="Cadastrar", x=950, y=180, \
            largura=100, fundo=self.bgButtonConfirm, command=create_produto)            

        # TABELA        
        tabela = MyTable(frame=self.master, posx=20, posy=300, \
            colunas=banco.show_all_produtos(),
            header={
                'ID': 10,
                'Produto': 40,
                'Seção': 30,
                'Estoque': 10,
                'Unidade': 10,
                'Custo': 10,
                'Preço': 10,
            }
        )        

    def categorias(self, busca=None):
        def cria_categoria():
            banco.create_categoria(nome=nome.entry.get())  
            self.categorias()                

        def busca_categoria():            
            busca = banco.busca_categoria(ent_nome.get())
            self.categorias(busca)
            
        self.limpaTela()
        self.criaTitulo("Cadastro de Seções")

        MyLabel(frame=self.master, texto="Nome: ", fundo=self.bgPadrao, x=270, y=140)
        nome = MyEntry(frame=self.master, x=380, y=140, largura=800)
        
        MyButton(frame=self.master, texto="Buscar", x=1190, y=140, largura=70, \
            command=busca_categoria)

        MyButton(frame=self.master, texto="Cancelar", x=380, y=180, \
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
        
        # CATEGORIAS
        Label(
            self.master,
            text="Categoria: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)

        cat = StringVar()
        CATEGORIAS = ['Açougue','Padaria','Hortifruti']
        ent_categoria = OptionMenu(
            self.master,
            cat,
            *CATEGORIAS            
            )
        ent_categoria["highlightthickness"]=0
        ent_categoria["borderwidth"]=0
        ent_categoria["anchor"]="w"
        ent_categoria.place(x=100, y=100, w=500, h=20)

        # TABELA
        tabela = MyTable(
            frame=self.master, 
            posx=20,
            posy=140,
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

        # CLIENTE
        Label(
            self.master,
            text="Cliente: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master).place(x=100, y=100, w=440)

        # BOTÃO BUSCAR CLIENTE
        Button(
            self.master,
            text="Buscar",
            bg=self.bgButtonSearch,
            fg="#cccccc",
            borderwidth=0,
            font="Helvetica 9 bold",            
        ).place(x=550, y=100, w=50, h=20)

        # PRODUTO
        Label(
            self.master,
            text="Produtos: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=140)
        ent_produto = Entry(self.master).place(x=100, y=140, w=250)   

        # BOTÃO BUSCAR PRODUTO
        Button(
            self.master,
            text="Buscar",
            bg=self.bgButtonSearch,
            fg="#cccccc",
            borderwidth=0,
            font="Helvetica 9 bold",
        ).place(x=360, y=140, w=50, h=20)             

        # QUANTIDADE        
        Label(
            self.master,
            text="Quantidade: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=420, y=140)
        ent_quantidade = Spinbox(
            self.master,
            from_=0,
            to=100,
        ).place(x=500, y=140, w=90, h=20)

        # BOTAO ADICIONAR
        btn_confirma = Button(
            self.master,
            text="Adicionar Produto",
            bg=self.bgButtonConfirm,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=220, y=180, w=200)        

        # LISTBOX
        listbox = Listbox(
            self.master,
            borderwidth=2)
        listbox.config(height=12)
        listbox.place(x=20, y=220, w=600)

        # BOTAO REMOVER PRODUTO        
        btn_procura = Button(
            self.master,
            text="Remover",
            bg=self.bgButtonEdit,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=110, y=440, w=200)

        # BOTAO FINALIZAR VENDA      
        btn_procura = Button(
            self.master,
            text="Finalizar",
            bg=self.bgButtonConfirm,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=330, y=440, w=200)            

    def limpaTela(self):
        for widget in self.master.winfo_children():
            if not isinstance(widget, Menu):
                widget.destroy()    

    def alteraTema(self, tema):
        if tema == "claro":
            self.bgPadrao = self.temaClaro
            self.fgPadrao = self.temaEscuro
        elif tema == "escuro":
            self.bgPadrao = self.temaEscuro
            self.fgPadrao = self.temaClaro

        self.master.configure(background=self.bgPadrao)
        for widget in self.master.winfo_children():
            if isinstance(widget, Label):
                widget['bg'] = self.bgPadrao
                widget['fg'] = self.fgPadrao
        
    def sobre(self):
        self.limpaTela()
        Label(
            self.master,
            text="Versão 0.1 - Sitema de Gerenciamento de Vendas",
            font="Helvetica 14 bold",
            bg=self.bgPadrao,
            fg=self.fgPadrao).pack()

        Label(
            self.master,
            text="Desenvolvido por NBDev Desenvolvimento de Sistemas",
            font="Helvetica 12",
            bg=self.bgPadrao,
            fg=self.fgPadrao).pack()

        img = PhotoImage(file="./imagens/python.png")
        logo = Label(
            self.master,            
            image=img,            
            bg=self.bgPadrao)
        logo.image = img
        logo.place(x=0, y=120, w=self.width)

    def run(self):
        self.master.mainloop()
              

if __name__ == "__main__":
    app = App()
    app.run()
