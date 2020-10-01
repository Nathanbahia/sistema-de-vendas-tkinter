from tkinter import *


class MyButton:
    def __init__(self, frame, texto, x, y, command=None, largura=50, \
        altura=25, cor="#000000", fundo="#cccccc", tam_fonte=12):

        self.button = Button(
            frame,
            text=texto,
            fg=cor,
            bg=fundo,
            font=f"Helvetica {tam_fonte}",
            command=command,
            borderwidth=0,
        )

        self.button.place(
            x=x,
            y=y,
            w=largura,
            h=altura,
        )