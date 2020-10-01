from tkinter import *


class MyEntry:
    def __init__(self, frame, x, y, tam_fonte=12, largura=None, altura=25):
        
        self.entry = Entry(
            frame,
            font=f"Helvetica {tam_fonte}"
        )

        self.entry.place(
            x=x,
            y=y,
            w=largura,
            h=altura
        )
