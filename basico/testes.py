from tkinter import *

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.criar_frames()
        janela.mainloop()

    def tela(self):
        self.janela.title('Entrar')
        self.janela.configure(background='mediumpurple1')
        self.janela.resizable(False, True)
        self.janela.maxsize(width=1000, height=900)
        self.janela.minsize(width=400, height=300)
        self.janela.geometry('800x500')  # alterado
#mudei o nome para evitar confusao pcom o outro
    def criar_frames(self):
        self.frame_1 = Frame(self.janela)
        self.frame_1.place(relx=0.1, rely=0.1, relwidth=0.9, relheight=0.5)

Application()
