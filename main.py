import customtkinter as tk
from modulo import *
from PIL import Image

def clique():
    pass

janela = CriarJanelaP("JanelaPrincipal", "400x400", 1)
l = janela.winfo_screenwidth()
a = janela.winfo_screenheight()
janela.geometry(f"{l}x{a}-10+0")

banner = CriarImagem(janela,"banner.png", 1300,253, 0, 1)
banner.grid(columnspan=12)

pesquisa = CriarCaixaTexto(janela, 200, 25, 1,0,"Busque aqui...")
pesquisa.grid(columnspan=12)

texto = CriarLabel(janela, "Pratos", 2,1)
pesquisa.grid(columnspan=2)

frango = CriarImagem(janela, "frango 2.png", 100, 100, 3, 1)
titulo1 = CriarLabel(janela, "Frango Grelhado", 3, 2)

janela.mainloop()