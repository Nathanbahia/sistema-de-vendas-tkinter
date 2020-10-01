from tkinter import *


class MyTable:
    def __init__(self, frame, posx, posy, colunas, header):        
        largura_total = 1280
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

        # CORPO               
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
            Button(
                cont,
                text="EDITAR",
                borderwidth=0,
                bg="#FF8000",
                width=17,
                command=lambda: print(self)
            ).pack(side=LEFT)
            cont.pack()                       

        table.place(x=posx, y=posy, w=largura_total, h=700-(posy+50))
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")  