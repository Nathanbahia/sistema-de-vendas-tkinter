import unittest
from gui import *

class TestGui(unittest.TestCase):    
    def test_contagem_de_elementos_janela_principal_na_criacao(self):
        app = App()
        widgets = app.master.winfo_children()
        self.assertEqual(len(widgets), 3)
        app.master.destroy()

    def test_textos_das_labels_na_criacao(self):
        app = App()
        widgets = app.master.winfo_children()        
        labels = [w for w in widgets if isinstance(w, Label)]        
        self.assertEqual(labels[0]["text"], "NBDev Desenvolvimento de Sistemas")
        self.assertEqual(labels[1]["text"], "")
        app.master.destroy()
        
    def test_contagem_de_elementos_funcao_produtos(self):
        app = App()
        app.produtos()         
        widgets = app.master.winfo_children()        
        self.assertEqual(len(widgets), 18)
        app.master.destroy()

    def test_textos_das_labels_na_funcao_produtos(self):
        app = App()
        app.produtos()
        widgets = app.master.winfo_children()        
        labels = [w for w in widgets if isinstance(w, Label)]        
        self.assertEqual(labels[0]["text"], "NBDev Desenvolvimento de Sistemas")
        self.assertEqual(labels[1]["text"], "Cadastro de Produtos")
        app.master.destroy()        

    def test_contagem_de_elementos_funcao_sobre(self):
        app = App()
        app.sobre()
        widgets = app.master.winfo_children()        
        self.assertEqual(len(widgets), 4)
        app.master.destroy()

    def test_textos_das_labels_na_funcao_sobre(self):
        app = App()
        app.sobre()
        widgets = app.master.winfo_children()        
        labels = [w for w in widgets if isinstance(w, Label)]        
        self.assertEqual(labels[0]["text"], "Versão 0.1 - Sitema de Gerenciamento de Vendas")
        self.assertEqual(labels[1]["text"], "Desenvolvido por NBDev Desenvolvimento de Sistemas")
        self.assertEqual(labels[2]["text"], "")        
        app.master.destroy()

    def test_funcao_altera_tema(self):
        app = App()
        app.alteraTema("claro")
        self.assertEqual(app.bgPadrao, app.temaClaro)
        self.assertEqual(app.fgPadrao, app.temaEscuro)
        app.alteraTema("escuro")
        self.assertEqual(app.bgPadrao, app.temaEscuro)
        self.assertEqual(app.fgPadrao, app.temaClaro)        
        app.master.destroy()

    def test_criacao_objeto_app(self):
        app = App()
        self.assertEqual(isinstance(app, App), True)
        self.assertEqual(isinstance(app.master, Tk), True)
        app.master.destroy()
        

if __name__ == "__main__":
    unittest.main()
