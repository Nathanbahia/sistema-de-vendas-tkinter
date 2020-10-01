from tkinter import *


class MyOption:
    def __init__(self, frame, opcoes, x, y, largura=100, altura=25, \
        cor="#000000", fundo="#cccccc", tam_fonte=12, command=None):
        self.var = StringVar()
        self.option = OptionMenu(
            frame,
            self.var,
            *opcoes
        )
        self.option["highlightthickness"]=0
        self.option["borderwidth"]=0
        self.option["anchor"]="w"
        self.option["font"]="Helvetica 12"

        self.option.place(
            x=x,
            y=y,
            w=largura,
            h=altura
        )
