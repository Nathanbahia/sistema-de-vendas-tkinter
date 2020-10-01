from tkinter import *


class MyLabel:
    def __init__(self, frame, texto, x, y, cor="#000000", fundo="#1546ff", \
        font_size=12, largura=None, altura=None):

        self.label = Label(
            frame,
            text=texto,
            fg=cor,
            bg=fundo,
            font=f"Helvetica {font_size}",            
        )
        self.label.place(
            x=x,
            y=y,
            w=largura,
            h=altura
        )
    
    def __str__(self):
        return self.label["text"]
