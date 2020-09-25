from tkinter import *
from backend.classes import *
from backend.bancodedados import *

user = Usuario(nome='nathan', senha='123')
banco = Banco()


class App:    
    def __init__(self):
        self.bgPadrao = "#484848"
        self.fgPadrao = "#dddddd"

        self.temaClaro = "#cccccc"
        self.temaEscuro = "#484848"

        self.width = 640
        self.height = 480
        
        self.master = Tk()
        self.master.title("Python")
        self.master.geometry(f"{self.width}x{self.height}")
        self.master.resizable(False, False)
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

    def clientes(self):
        self.limpaTela()
        self.criaTitulo("Cadastro de Clientes")

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master).place(x=100, y=100, w=500)

        # ENDEREÇO
        Label(
            self.master,
            text="Endereço: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=140)
        ent_endereco = Entry(self.master).place(x=100, y=140, w=500)        

        # TELEFONE        
        Label(
            self.master,
            text="Telefone: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=180)
        ent_telefone = Entry(self.master).place(x=100, y=180, w=200, h=20)

        # EMAIL
        Label(
            self.master,
            text="E-mail: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=320, y=180)
        ent_email = Entry(self.master).place(x=400, y=180, w=200)              

        # BOTÃO CONFIRMA
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg="#5858FA",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=110, y=220, w=200)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg="#2E9AFE",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=330, y=220, w=200)

        # LISTBOX
        listbox = Listbox(
            self.master,
            borderwidth=2)
        listbox.config(height=10)
        listbox.place(x=20, y=260, w=600)

        # BOTÃO EDITAR
        btn_procura = Button(
            self.master,
            text="Editar",
            bg="#FE2E2E",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=220, y=440, w=200)

    def produtos(self):
        self.limpaTela()
        self.criaTitulo("Cadastro de Produtos")

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master).place(x=100, y=100, w=500)

        # CATEGORIA
        Label(
            self.master,
            text="Categoria: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=140)

        cat = StringVar()
        CATEGORIAS = banco.show_all_categorias()
        ent_categoria = OptionMenu(
            self.master,
            cat,
            *CATEGORIAS            
            )
        ent_categoria["highlightthickness"]=0
        ent_categoria["borderwidth"]=0
        ent_categoria["anchor"]="w"
        ent_categoria.place(x=100, y=140, w=150, h=20)

        # BOTÃO ADICIONAR SEÇÃO
        Button(
            self.master,
            text="+",
            bg="#FE2E2E",
            fg="#FFFFFF",
            borderwidth=0,
            command=self.categorias).place(x=260, y=140, w=40, h=20)        

        # QUANTIDADE
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

        # CUSTO
        Label(
            self.master,
            text="Quantidade: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=180)
        ent_quantidade = Entry(self.master).place(x=100, y=180, w=200)

        # UNIDADE
        Label(
            self.master,
            text="Custo: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=320, y=180)
        ent_custo = Entry(self.master).place(x=400, y=180, w=200)        

        # BOTÃO CONFIRMA
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg="#5858FA",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=110, y=220, w=200)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg="#2E9AFE",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=330, y=220, w=200)

        # LISTBOX
        listbox = Listbox(
            self.master,
            borderwidth=2)
        listbox.config(height=10)
        listbox.place(x=20, y=260, w=600)

        # BOTÃO EDITAR
        btn_procura = Button(
            self.master,
            text="Editar",
            bg="#FE2E2E",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,            
            ).place(x=220, y=440, w=200)

    def categorias(self):
        self.limpaTela()
        self.criaTitulo("Cadastro de Seções")

        # NOME
        Label(
            self.master,
            text="Nome: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master)
        ent_nome.place(x=100, y=100, w=500)
    
        # BOTÃO CONFIRMA
        btn_confirma = Button(
            self.master,
            text="Cadastrar",
            bg="#5858FA",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0,
            command=lambda: banco.create_categoria(nome=ent_nome.get(), user=user)
            ).place(x=110, y=140, w=200)

        # BOTÃO PROCURA
        btn_procura = Button(
            self.master,
            text="Buscar",
            bg="#2E9AFE",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=330, y=140, w=200)

        # LISTBOX
        listbox = Listbox(
            self.master,
            borderwidth=2)
        listbox.config(height=15)
        listbox.place(x=20, y=180, w=600)

        # BOTÃO EDITAR
        btn_procura = Button(
            self.master,
            text="Editar",
            bg="#FE2E2E",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=220, y=440, w=200)

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

        # LISTBOX
        listbox = Listbox(
            self.master,
            borderwidth=2)
        listbox.config(height=20)
        listbox.place(x=20, y=140, w=600)

    def vendas(self):
        self.limpaTela()
        self.criaTitulo("Vendas")

        # CLIENTE
        Label(
            self.master,
            text="Cliente: ",
            bg=self.bgPadrao,
            fg=self.fgPadrao).place(x=20, y=100)
        ent_nome = Entry(self.master).place(x=100, y=100, w=430)

        # BOTÃO BUSCAR CLIENTE
        Button(
            self.master,
            text="Buscar",
            bg="#FE2E2E",
            fg="#cccccc",
            borderwidth=0,
            font="Helvetica 9 bold",            
        ).place(x=540, y=100, w=50, h=20)

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
            bg="#FE2E2E",
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
            text="Cadastrar",
            bg="#5858FA",
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
            bg="#FE2E2E",
            fg="#cccccc",
            font="Helvetica 9 bold",
            borderwidth=0
            ).place(x=110, y=440, w=200)

        # BOTAO FINALIZAR VENDA      
        btn_procura = Button(
            self.master,
            text="Finalizar",
            bg="#FE2E2E",
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

        img = PhotoImage(file="imagens/python.png")
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
