import customtkinter as tk
from modulo import *
from PIL import Image

def clique():
    pass

janela = CriarJanela("JanelaPrincipal", "400x400", 1)
l = janela.winfo_screenwidth()
a = janela.winfo_screenheight()
janela.geometry(f"{l}x{a}-10+0")

banner = CriarImagem(janela,"banner.png", 0,0, 255, 1300)
banner.grid(columnspan=12)

abas = CriarAbas(janela,2,6,100,30,"Pratos","Bebidas","Sobremesa")
abas.configure(fg_color="DarkRed")
abas.grid(stick="NW")

#       COLUNA DE PRATOS

frame = CriarFrame(abas.tab("Pratos"), 2, 0,2050,370)
frame.configure(fg_color="DarkRed", corner_radius=0)
frame.grid(sticky="W",columnspan=13)

prato = CriarLabel(frame, "Pratos", 1,0)
prato.configure(text_color="White")
prato.grid(sticky="N", columnspan=13)

#       Caixinha do frango
framefrango = CriarFrame(frame, 3,1,200,330)
framefrango.grid(sticky="NW", columnspan=3)
frango = CriarImagem(framefrango, "frango 2.png", 2, 1, 100, 150)
titulo1 = CriarLabel(framefrango, "Frango Grelhado",1, 1)
descri = CriarLabel(framefrango, "Descrição do prato",3, 1)
carrinho = CriarImagem(framefrango,"carrinho.png",4,1,15,15)
carrinho.grid(sticky="SW", columnspan=3)
valor = CriarLabel(framefrango,"R$20,00",4,1)
valor.grid(sticky="S", columnspan=3)
botão = CriarBotão(framefrango,"QUERO JÁ",clique,5,1,100,30)
botão.grid(sticky="S", columnspan=3)


#       Caixinha do Parmediana
frameparmedi = CriarFrame(frame, 3,4,200,330)
frameparmedi.grid(sticky="NW")
parmedi = CriarImagem(frameparmedi, "parmediana.png", 2, 4, 100, 150)
t_parmedi = CriarLabel(frameparmedi, "Parmediana", 1, 4)
descri = CriarLabel(frameparmedi, "Descrição do prato",3, 4)
carrinho = CriarImagem(frameparmedi,"carrinho.png",4,4,15,15)
carrinho.grid(sticky="SW", columnspan=3)
valor = CriarLabel(frameparmedi,"R$30,00",4,4)
valor.grid(sticky="S", columnspan=3)
botão = CriarBotão(frameparmedi,"QUERO JÁ",clique,5,4,100,30)
botão.grid(sticky="S", columnspan=3)

#       Caixinha do macarrão
frameparmedi = CriarFrame(frame, 3,8,200,330)
frameparmedi.grid(sticky="NW")
parmedi = CriarImagem(frameparmedi, "macarrão.png", 2, 8, 100, 150)
t_parmedi = CriarLabel(frameparmedi, "Macarrão", 1, 8)
descri = CriarLabel(frameparmedi, "Descrição do prato",3, 8)
carrinho = CriarImagem(frameparmedi,"carrinho.png",4,8,15,15)
carrinho.grid(sticky="SW", columnspan=3)
valor = CriarLabel(frameparmedi,"R$40,00",4,8)
valor.grid(sticky="S", columnspan=3)
botão = CriarBotão(frameparmedi,"QUERO JÁ",clique,5,8,100,30)
botão.grid(sticky="S", columnspan=3)

#       Caixinha do strognoff
frameparmedi = CriarFrame(frame, 3,8,200,330)
frameparmedi.grid(sticky="NW")
parmedi = CriarImagem(frameparmedi, "macarrão.png", 2, 8, 100, 150)
t_parmedi = CriarLabel(frameparmedi, "Macarrão", 1, 8)
descri = CriarLabel(frameparmedi, "Descrição do prato",3, 8)
carrinho = CriarImagem(frameparmedi,"carrinho.png",4,8,15,15)
carrinho.grid(sticky="SW", columnspan=3)
valor = CriarLabel(frameparmedi,"R$40,00",4,8)
valor.grid(sticky="S", columnspan=3)
botão = CriarBotão(frameparmedi,"QUERO JÁ",clique,5,8,100,30)
botão.grid(sticky="S", columnspan=3)



janela.mainloop()