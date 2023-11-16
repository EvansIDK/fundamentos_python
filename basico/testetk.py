from tkinter import *

janela = Tk()

class Application():

  def __init__(self):
    self.janela = janela
    self.tela_entrar()
    self.frames_da_tela_entrar()
    self.widgets_entrar()
    janela.mainloop()

  def tela_entrar(self):
    self.janela.title('Entrar')
    self.janela.configure(background='lavender')
    self.janela.geometry("700x500")
    self.janela.resizable(True, True)
    self.janela.maxsize(width=900, height=700)
    self.janela.minsize(width=400, height=300)

  def frames_da_tela_entrar(self):
    self.frame_entrar = Frame(self.janela,
                         bd=4,
                         bg='lightblue',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_entrar.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)

  def widgets_entrar(self):
    self.bt_entrar = Button(self.frame_entrar, text='Entrar', bg='white', command=self.on_login_button_click)
    self.bt_entrar.place(relx=0.76, rely=0.85, relwidth=0.2, relheight=0.1)
    self.lb_logo = Label(self.frame_entrar, text='Libby', bg='lightblue',fg='DarkOrchid4', font=("Bahnschrift", 25, 'bold'))
    self.lb_logo.place(relx=0.33, rely=0.1, relwidth=0.35, relheight=0.1)
    self.lb_codigo = Label(self.frame_entrar, text='Digite seu código empresarial:', bg='lightblue')
    self.lb_codigo.place(relx=0.33, rely=0.35, relwidth=0.35, relheight=0.05)
    self.codigo_entry = Entry(self.frame_entrar)
    self.codigo_entry.place(relx=0.33, rely=0.43, relwidth=0.35, relheight=0.05)
    self.lb_sinopse = Label(self.frame_entrar, text='Digite sua senha:', bg='lightblue')
    self.lb_sinopse.place(relx=0.33, rely=0.5, relwidth=0.35, relheight=0.05)
    self.sinopse_entry = Entry(self.frame_entrar)
    self.sinopse_entry.place(relx=0.33, rely=0.58, relwidth=0.35, relheight=0.05)

  def on_login_button_click(self):
    if self.codigo_entry.get().lower() == "login" and self.sinopse_entry.get().lower() == "pass":
      self.frame_entrar.destroy()
      self.tela_menu()

  def tela_menu(self):
    self.janela.title('Menu')
    self.janela.configure(background='lavender')
    self.frame_menu = Frame(self.janela, bd=4, bg='lightblue', highlightbackground='black', highlightthickness=2)
    self.frame_menu.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)
    self.bt_sair = Button(self.frame_menu, text='Sair', bg='white')
    self.bt_sair.place(relx=0.84, rely=0.92, relwidth=0.15, relheight=0.07)
    self.bt_add_livro = Button(self.frame_menu, text='Adicionar livro', bg='lavender', command=self.navigate_to_adicionar_livro)
    self.bt_add_livro.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.1)
    self.bt_aprovar = Button(self.frame_menu, text='Aprovar compras', bg='lavender', command=self.navigate_to_aprovar_compra)
    self.bt_aprovar.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.1)
    self.bt_creditos = Button(self.frame_menu, text='Adicionar créditos', bg='lavender', command=self.navigate_to_adicionar_creedito)
    self.bt_creditos.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    self.lb_logo = Label(self.frame_menu, text='Menu', bg='lightblue',fg='DarkOrchid4', font=("Bahnschrift", 25, 'bold'))
    self.lb_logo.place(relx=0.32, rely=0.1, relwidth=0.35, relheight=0.1)

  def navigate_to_adicionar_livro(self):
    self.frame_menu.destroy()
    self.tela_adicionar_livro()

  def navigate_to_aprovar_compra(self):
    self.frame_menu.destroy()
    self.tela_aprovar_compra()


  def navigate_to_adicionar_creedito(self):
    self.frame_menu.destroy()
    self.tela_adicionar_creedito()

  def tela_adicionar_livro(self):
    self.janela.title('Adicionar livro')
    self.janela.configure(background='lavender')
    self.frame_1 = Frame(self.janela,
                         bd=4,
                         bg='lightblue',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)
    self.bt_enviar = Button(self.frame_1, text='Enviar')
    self.bt_enviar.place(relx=0.76, rely=0.85, relwidth=0.2, relheight=0.1)
    self.bt_voltar = Button(self.frame_1, text='Voltar', command=self.navigate_to_menu)
    self.bt_voltar.place(relx=0.76, rely=0.72, relwidth=0.2, relheight=0.1)
    # ... (Remaining code for the "Adicionar livro" screen)
  #botao capa
    self.bt_capa = Button(self.frame_1, text='Clique para adicionar a capa')
    self.bt_capa.place(relx=0.76, rely=0.05, relwidth=0.2, relheight=0.5)
  #botao arquivo do livro
    self.bt_arquivo = Button(self.frame_1, text='Clique para adicionar o arquivo')
    self.bt_arquivo.place(relx=0.025, rely=0.75, relwidth=0.4, relheight=0.1)

  #criacao das labels
  #titulo
    self.lb_titulo = Label(self.frame_1, text='Título do livro', bg='lightblue')
    self.lb_titulo.place(relx=0.01, rely=0.05, relwidth=0.35, relheight=0.05)
    self.titulo_entry = Entry(self.frame_1)
    self.titulo_entry.place(relx=0.01, rely=0.1, relwidth=0.44, relheight=0.05)
  #sinopse
    self.lb_sinopse = Label(self.frame_1, text='Sinopse', bg='lightblue')
    self.lb_sinopse.place(relx=0.01, rely=0.15, relwidth=0.35, relheight=0.05)
    self.sinopse_entry = Entry(self.frame_1)
    self.sinopse_entry.place(relx=0.01, rely=0.2, relwidth=0.44, relheight=0.05)
  #preco
    self.lb_preco = Label(self.frame_1, text='Preço (pontos)', bg='lightblue')
    self.lb_preco.place(relx=0.01, rely=0.25, relwidth=0.35, relheight=0.05)
    self.preco_entry = Entry(self.frame_1)
    self.preco_entry.place(relx=0.01, rely=0.3, relwidth=0.44, relheight=0.05)
  #conteudo
    self.lb_conteudo = Label(self.frame_1, text='Conteúdo (digitado/arquivo)', bg='lightblue')
    self.lb_conteudo.place(relx=0.01, rely=0.5, relwidth=0.35, relheight=0.05)
    self.conteudo_entry = Entry(self.frame_1)
    self.conteudo_entry.place(relx=0.01, rely=0.55, relwidth=0.44, relheight=0.15)


  def tela_aprovar_compra(self):
    self.janela.title('Aprovar compras')
    self.janela.configure(background='lavender')
    self.janela.geometry("700x500")
    self.janela.resizable(True, True)
    self.janela.maxsize(width=900, height=700)
    self.janela.minsize(width=400, height=300)
    self.frame_1 = Frame(self.janela,
                         bd=4,
                         bg='lightblue',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)
    self.frame_2 = Frame(self.frame_1,
                         bd=4,
                         bg='white',
                         highlightbackground='snow2',
                         highlightthickness=1.5)
    self.frame_2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.63)
    self.frame_3 = Frame(self.janela,
                         bd=4,
                         bg='lavender',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_3.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.27)
    #botao Voltar
    self.bt_Voltar = Button(self.frame_1, text='Voltar', bg='white')
    self.bt_Voltar.place(relx=0.84, rely=0.92, relwidth=0.15, relheight=0.07)
    #botoes clientes
    self.bt_cliente1 = Button(self.frame_1, text='Cliente1', bg='snow2')
    self.bt_cliente1.place(relx=0.1, rely=0.33, relwidth=0.35, relheight=0.06)
    self.bt_cliente2 = Button(self.frame_1, text='Cliente2', bg='snow2')
    self.bt_cliente2.place(relx=0.1, rely=0.41, relwidth=0.35, relheight=0.06)
    self.bt_cliente3 = Button(self.frame_1, text='Cliente3', bg='snow2')
    self.bt_cliente3.place(relx=0.1, rely=0.49, relwidth=0.35, relheight=0.06)
    #botao aprovar
    self.bt_Adicionar = Button(self.frame_3, text='Aprovar', bg='white', font=("Bahnschrift", 13, 'bold'))
    self.bt_Adicionar.place(relx=0.04, rely=0.11, relwidth=0.45, relheight=0.3)
    #Desaprovar
    self.bt_Desaprovar = Button(self.frame_3, text='Desaprovar', bg='white', font=("Bahnschrift", 13, 'bold'))
    self.bt_Desaprovar.place(relx=0.53, rely=0.11, relwidth=0.45, relheight=0.3)
    #Cancelar
    self.bt_Cancelar = Button(self.frame_3, text='Cancelar', bg='white', font=("Bahnschrift", 13, 'bold'))
    self.bt_Cancelar.place(relx=0.3, rely=0.6, relwidth=0.45, relheight=0.3)

    #criacao das labels
    #logo
    self.lb_logo = Label(self.frame_1, text='Aprovar compras', bg='lightblue',fg='DarkOrchid4', font=("Bahnschrift", 25, 'bold'))
    self.lb_logo.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.1)
    #selecione
    self.lb_selecione = Label(self.frame_1, text='Selecione o cliente para aprovar/desaprovar a compra', bg='lightblue', font=("Arial", 12, 'bold'))
    self.lb_selecione.place(relx=0.13, rely=0.135, relwidth=0.748, relheight=0.1)
    #tabela
    self.lb_fun = Label(self.frame_1, text='Funcionário', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_fun.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.05)

    self.lb_pontos = Label(self.frame_1, text='Pontos disponíveis', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_pontos.place(relx=0.45, rely=0.25, relwidth=0.24, relheight=0.05)

    self.lb_valor = Label(self.frame_1, text='Valor da compra', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_valor.place(relx=0.69, rely=0.25, relwidth=0.21, relheight=0.05)

    self.lb_pontos1 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos1.place(relx=0.45, rely=0.33, relwidth=0.24, relheight=0.06)
    self.lb_pontos2 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos2.place(relx=0.45, rely=0.41, relwidth=0.24, relheight=0.06)
    self.lb_pontos3 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos3.place(relx=0.45, rely=0.49, relwidth=0.24, relheight=0.06)

    self.lb_venda = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda.place(relx=0.69, rely=0.33, relwidth=0.21, relheight=0.06)
    self.lb_venda2 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda2.place(relx=0.69, rely=0.41, relwidth=0.21, relheight=0.06)
    self.lb_venda3 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda3.place(relx=0.69, rely=0.49, relwidth=0.21, relheight=0.06)

  def tela_adicionar_creedito(self):
    self.janela.title('Adicionar créditos')
    self.janela.configure(background='lavender')
    self.janela.geometry("700x500")
    self.janela.resizable(True, True)
    self.janela.maxsize(width=900, height=700)
    self.janela.minsize(width=400, height=300)
    self.frame_1 = Frame(self.janela,
                         bd=4,
                         bg='lightblue',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)
    self.frame_2 = Frame(self.frame_1,
                         bd=4,
                         bg='white',
                         highlightbackground='snow2',
                         highlightthickness=1.5)
    self.frame_2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.63)
    #botao Voltar
    self.bt_Voltar = Button(self.frame_1, text='Voltar', bg='white')
    self.bt_Voltar.place(relx=0.84, rely=0.92, relwidth=0.15, relheight=0.07)
    #botoes clientes
    self.bt_cliente1 = Button(self.frame_1, text='Cliente1', bg='snow2', command=self.navigate_to_add_cree)
    self.bt_cliente1.place(relx=0.1, rely=0.33, relwidth=0.35, relheight=0.06)
    self.bt_cliente2 = Button(self.frame_1, text='Cliente2', bg='snow2', command=self.navigate_to_add_cree)
    self.bt_cliente2.place(relx=0.1, rely=0.41, relwidth=0.35, relheight=0.06)
    self.bt_cliente3 = Button(self.frame_1, text='Cliente3', bg='snow2', command=self.navigate_to_add_cree)
    self.bt_cliente3.place(relx=0.1, rely=0.49, relwidth=0.35, relheight=0.06)
    
    #criacao das labels
    #logo
    self.lb_logo = Label(self.frame_1, text='Adicionar créditos', bg='lightblue',fg='DarkOrchid4', font=("Bahnschrift", 25, 'bold'))
    self.lb_logo.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.1)
    #selecione
    self.lb_selecione = Label(self.frame_1, text='Selecione o funcionário para adicionar créditos', bg='lightblue', font=("Arial", 12, 'bold'))
    self.lb_selecione.place(relx=0.13, rely=0.135, relwidth=0.748, relheight=0.1)
    #tabela
    self.lb_fun = Label(self.frame_1, text='Funcionário', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_fun.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.05)

    self.lb_pontos = Label(self.frame_1, text='Pontos disponíveis', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_pontos.place(relx=0.45, rely=0.25, relwidth=0.24, relheight=0.05)

    self.lb_valor = Label(self.frame_1, text='Valor da compra', bg='white', highlightbackground='black', highlightthickness=1, font=("Arial", 11))
    self.lb_valor.place(relx=0.69, rely=0.25, relwidth=0.21, relheight=0.05)

    self.lb_pontos1 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos1.place(relx=0.45, rely=0.33, relwidth=0.24, relheight=0.06)
    self.lb_pontos1 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos1.place(relx=0.45, rely=0.41, relwidth=0.24, relheight=0.06)
    self.lb_pontos1 = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_pontos1.place(relx=0.45, rely=0.49, relwidth=0.24, relheight=0.06)

    self.lb_venda = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda.place(relx=0.69, rely=0.33, relwidth=0.21, relheight=0.06)
    self.lb_venda = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda.place(relx=0.69, rely=0.41, relwidth=0.21, relheight=0.06)
    self.lb_venda = Label(self.frame_1, text='000000', bg='white', highlightbackground='black', highlightthickness=1)
    self.lb_venda.place(relx=0.69, rely=0.49, relwidth=0.21, relheight=0.06)
    


  def navigate_to_add_cree(self):
    self.frame_1.destroy()
    self.tela_add_cree()

  def tela_add_cree(self):
    self.janela.title('Adicionar')
    self.janela.configure(background='lavender')
    self.janela.geometry("700x500")
    self.janela.resizable(True, True)
    self.janela.maxsize(width=900, height=700)
    self.janela.minsize(width=400, height=300)
    self.frame_3 = Frame(self.janela,
                         bd=4,
                         bg='lavender',
                         highlightbackground='black',
                         highlightthickness=2)
    self.frame_3.place(relx=0.2, rely=0.26, relwidth=0.6, relheight=0.33)
#botao Adicionar
    self.bt_Adicionar = Button(self.frame_3, text='Adicionar', bg='white', font=("Bahnschrift", 13, 'bold'))
    self.bt_Adicionar.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.2)
    #Cancelar
    self.bt_Cancelar = Button(self.frame_3, text='Cancelar', bg='white', font=("Bahnschrift", 13, 'bold'))
    self.bt_Cancelar.place(relx=0.55, rely=0.7, relwidth=0.4, relheight=0.2)
    self.lb_add = Label(self.frame_3, text='Digite a quantidade de pontos a serem adicionados:', bg='lavender', font=("Arial", 11))
    self.lb_add.place(relx=0.01, rely=0.01, relwidth=1, relheight=0.13)
    self.add_entry = Entry(self.frame_3)
    self.add_entry.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.18)

  def navigate_to_menu(self):
    self.frame_1.destroy()
    self.tela_menu()

Application()
