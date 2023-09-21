import customtkinter as tk
from modulo import*

check1 = CriarCheckBox(janela, "Marcar",4,6)

switch = CriarSwitch(janela, "Marcar",5,6)

progress = CriarProgressBar(janela, 200, 10, 7, 6, 0.2)



janela.mainloop()