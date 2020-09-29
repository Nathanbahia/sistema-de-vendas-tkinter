from tkinter import *
from classes import *
from bancodedados import *


banco = Banco()


class Tabela:
    def __init__(self, frame, posx, posy, colunas, header):        
        largura_total = 1240
        larg_colunas = []

        table = Frame(frame)
        canvas = Canvas(table)
        scroll = Scrollbar(table, orient="vertical", command=canvas.yview)
        scroll_frame = Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor=NW)
        canvas.configure(yscrollcommand=scroll.set)

        # CABEÇALHO        
        container_head = Frame(frame)
        for h in header:
            Label(
                container_head,
                text=h.upper(),
                bg="#FF8000", 
                anchor=W,
                font="Helvetica 10",
                padx=5,
                width=header[h]
            ).pack(side=LEFT, fill=BOTH)            
            larg_colunas.append(header[h])
        container_head.place(x=posx, y=posy, w=largura_total)
                        
        for elemento in colunas:
            indice = 0
            x = posx
            cont = Frame(scroll_frame)            
            for dados in elemento:                
                Label(
                    cont,
                    text=str(elemento[dados]).upper(),
                    borderwidth=1,
                    relief="groove",                      
                    anchor=W,
                    font="Helvetica 10",
                    padx=5,
                    width=larg_colunas[indice]
                ).pack(side=LEFT, fill=BOTH)
                indice += 1
            cont.pack()                       

        table.place(x=posx, y=posy, w=largura_total, h=700-posy)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")       

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

        # LOGO
        img = PhotoImage(file="./imagens/python.png")
        logo = Label(
            self.master,            
            image=img,            
            bg=self.bgPadrao)
        logo.image = img
        logo.place(x=20, y=40)

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao,
            font=self.fontePadrao).place(x=270, y=100)
        ent_nome = Entry(self.master, font=self.fontePadrao)
        ent_nome.place(x=350, y=100, w=840, h=25)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg=self.bgButtonSearch,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,
            command=busca_cliente
            )
        btn_procura.place(x=1200, y=100, w=50, h=25)        

        # ENDEREÇO
        Label(
            self.master,
            text="Endereço: ",
            bg=self.bgPadrao,
            font=self.fontePadrao,     
            fg=self.fgPadrao).place(x=270, y=150)
        ent_endereco = Entry(self.master, font=self.fontePadrao)
        ent_endereco.place(x=350, y=150, w=900, h=25)        

        # TELEFONE        
        Label(
            self.master,
            text="Telefone: ",
            bg=self.bgPadrao,
            font=self.fontePadrao,     
            fg=self.fgPadrao).place(x=270, y=200)
        ent_telefone = Entry(self.master, font=self.fontePadrao)
        ent_telefone.place(x=350, y=200, w=300, h=25)

        # EMAIL
        Label(
            self.master,
            text="E-mail: ",
            bg=self.bgPadrao,
            font=self.fontePadrao,
            fg=self.fgPadrao).place(x=660, y=200)
        ent_email = Entry(self.master, font=self.fontePadrao)
        ent_email.place(x=740, y=200, w=300, h=25)              

        # BOTÃO CONFIRMA
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg=self.bgButtonConfirm,
            fg="#cccccc",
            font="Helvetica 12 bold",
            borderwidth=1,            
            highlightbackground="#cccccc",
            highlightcolor="#ffffff",
            relief=GROOVE,
            underline=10,
            command=create_cliente,
            ).place(x=1050, y=200, w=200, h=25)

        # TABELA 
        tabela = Tabela(
            frame=self.master,
            posx=20,
            posy=300,            
            header={
                'ID': 10,
                'Nome': 40,
                'Telefone': 20,
                'E-mail': 25,
                'Endereço': 60                
            },
            colunas=banco.show_all_clientes() if busca == None else busca
        )               

    def produtos(self):
        def create_produto():
            banco.create_produto(
                nome=ent_nome.get(),
                categoria=cat.get(),
                quantidade=ent_quantidade.get(),
                unidade=uni.get()
            )
            self.produtos()

        self.limpaTela()
        self.criaTitulo("Cadastro de Produtos")

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master)
        ent_nome.place(x=100, y=100, w=440)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg=self.bgButtonSearch,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=550, y=100, w=50, h=20)       

        # CATEGORIA
        Label(
            self.master,
            text="Categoria: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=140)

        cat = StringVar()
        CATEGORIAS = [ c['nome'].upper() for c in banco.show_all_categorias() ]
        CATEGORIAS.append(None) if len(CATEGORIAS) == 0 else print()
        ent_categoria = OptionMenu(
            self.master,
            cat,
            *CATEGORIAS,            
            )
        ent_categoria["highlightthickness"]=0
        ent_categoria["borderwidth"]=0
        ent_categoria["anchor"]="w"
        ent_categoria.place(x=100, y=140, w=150, h=20)

        # BOTÃO ADICIONAR SEÇÃO
        Button(
            self.master,
            text="+",
            bg=self.bgButtonConfirm,
            fg="#FFFFFF",
            borderwidth=0,
            command=self.categorias).place(x=260, y=140, w=40, h=20)        

        # UNIDADE
        uni = StringVar()
        UNIDADES = ['Unidade', 'Quilo']
        Label(
            self.master,
            text="Unidade: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=320, y=140)
        ent_unidade = OptionMenu(
            self.master,
            uni,
            *UNIDADES
            )
        ent_unidade["highlightthickness"]=0
        ent_unidade["borderwidth"]=0
        ent_unidade["anchor"]="w"
        ent_unidade.place(x=400, y=140, w=200, h=20)

        # QUANTIDADE
        Label(
            self.master,
            text="Quantidade: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=180)
        ent_quantidade = Entry(self.master)
        ent_quantidade.place(x=100, y=180, w=200)

        # CUSTO
        Label(
            self.master,
            text="Custo: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=320, y=180)
        ent_custo = Entry(self.master)
        ent_custo.place(x=400, y=180, w=200)        

        # BOTÃO CADASTRO
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg=self.bgButtonConfirm,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,
            command=create_produto,
            ).place(x=220, y=220, w=200)

        # TABELA        
        tabela = Tabela(
            frame=self.master, 
            posx=20,
            posy=260,
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
            banco.create_categoria(nome=ent_nome.get())  
            self.categorias()                

        def busca_categoria():            
            busca = banco.busca_categoria(ent_nome.get())
            self.categorias(busca)
            
        self.limpaTela()
        self.criaTitulo("Cadastro de Seções")

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master)
        ent_nome.place(x=100, y=100, w=440)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg=self.bgButtonSearch,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,
            command=busca_categoria
            ).place(x=550, y=100, w=50, h=20)        
    
        # BOTÃO CONFIRMA
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg=self.bgButtonConfirm,
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,
            command=cria_categoria
            ).place(x=220, y=140, w=200)

        # TABELA
        tabela = Tabela(
            frame=self.master, 
            posx=20,
            posy=180,
            header={
                'ID': 10,
                'Seção': 90,
            },
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
        tabela = Tabela(
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
