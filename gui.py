from tkinter import *


class App:
    width = 700
    height = 480    
    bg1 = "#3066be"
    bg2 = "#119da4"
    bg3 = "#6d9dc5"
    bg4 = "#80ded9"
    bg5 = "#aeecef"    
    fonte_grande = "Verdana 22 bold"
    fonte_botao = "Verdana 12"
    fonte_label = "Verdana 10"

    def __init__(self):
        self.master = Tk()
        self.master.configure(background=App.bg3)
        self.master.title("Gerenciamento de Vendas")
        self.master.geometry(f"{App.width}x{App.height}+100+100")
        self.master.columnconfigure(0, weight=int(App.width/10))        
        self.master.columnconfigure(1, weight=int(App.width/10))        
        self.master.columnconfigure(2, weight=int(App.width/10))        
        self.master.columnconfigure(3, weight=int(App.width/10))        
        self.master.columnconfigure(4, weight=int(App.width/10))        
        self.master.columnconfigure(5, weight=int(App.width/10))        
        self.master.columnconfigure(6, weight=int(App.width/10))        
        self.master.columnconfigure(7, weight=int(App.width/10))        
        self.master.columnconfigure(8, weight=int(App.width/10))        
        self.master.columnconfigure(9, weight=int(App.width/10))

        self.master.rowconfigure(0, weight=int(App.height/10))
        self.master.rowconfigure(1, weight=int(App.height/10))
        self.master.rowconfigure(2, weight=int(App.height/10))
        self.master.rowconfigure(3, weight=int(App.height/10))
        self.master.rowconfigure(4, weight=int(App.height/10))
        self.master.rowconfigure(5, weight=int(App.height/10))
        self.master.rowconfigure(6, weight=int(App.height/10))
        self.master.rowconfigure(7, weight=int(App.height/10))
        self.master.rowconfigure(8, weight=int(App.height/10))
        self.master.rowconfigure(9, weight=int(App.height/10))                

        """ Título da Janela """
        self.lbl_title = Label(
            self.master, 
            text="Meu Negócio",
            font=App.fonte_grande,
            bg=App.bg3
        )
        self.lbl_title.grid(row=0, column=0, columnspan=10, sticky=NS)

        
        """ Menu """

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.menu_produtos = Menu(self.menu, tearoff=False)
        self.menu_clientes = Menu(self.menu, tearoff=False)
        self.menu_vendas = Menu(self.menu, tearoff=False)
        self.menu_usuarios = Menu(self.menu, tearoff=False)
        self.menu_configuracoes = Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label="Produtos", menu=self.menu_produtos)
        self.menu.add_cascade(label="Clientes", menu=self.menu_clientes)
        self.menu.add_cascade(label="Vendas", menu=self.menu_vendas)
        self.menu.add_cascade(label="Usuários", menu=self.menu_usuarios)
        self.menu.add_cascade(label="Configurações", menu=self.menu_configuracoes)
        
        self.menu_produtos.add_command(label="Cadastrar", command=self.cadastrar_produto)
        self.menu_produtos.add_command(label="Consultar", command=self.consultar)        

        self.menu_clientes.add_command(label="Cadastrar", command=self.consultar)
        self.menu_clientes.add_command(label="Consultar", command=self.consultar)        

        self.menu_vendas.add_command(label="Nova", command=self.consultar)
        self.menu_vendas.add_command(label="Histórico", command=self.consultar)

    # PRODUTOS
    
    def cadastrar_produto(self):
        self.lbl_nome = Label(self.master, text="Nome", font=App.fonte_label).grid(column=1, row=2, sticky=E)
        self.lbl_categoria = Label(self.master, text="Categoria", font=App.fonte_label).grid(column=1, row=3, sticky=E)
        self.lbl_quantidade = Label(self.master, text="Quantidade", font=App.fonte_label).grid(column=1, row=4, sticky=E)
        self.lbl_unidade = Label(self.master, text="Unidade", font=App.fonte_label).grid(column=1, row=5, sticky=E)

        self.ent_nome = Entry(self.master, font=App.fonte_label).grid(column=3, row=2, sticky=W)
        self.ent_categoria = Entry(self.master, font=App.fonte_label).grid(column=3, row=3, sticky=W)
        self.ent_quantidade = Entry(self.master, font=App.fonte_label).grid(column=3, row=4, sticky=W)
        self.ent_unidade = Entry(self.master, font=App.fonte_label).grid(column=3, row=5, sticky=W)


    def consultar(self):
        print("Consulta banco de dados")




               


        

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()