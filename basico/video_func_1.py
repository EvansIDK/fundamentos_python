"""subprogramas são uma repetição de procedimentos, encapsulando um pedaço do software para poder ser reutilizado"""
def extract_audio(
    video_file, output_file, eq=True):
    path_1=extract_audio( 'video_1.mp4', 'result 1.wav', eq=False)
    """o codigo que aparece após o def é o nome do subprograma, em seguida vem os parametros (dentro dos parenteses) e após isto os passos,
    o nome indica como ela deve ser chamada, os parametros quando e os passos como"""
path_1=extract_audio( 'video_1.mp4', 'result 1.wav', eq=False)
path_2=extract_audio('video 2.mp4', 'result 2.wav', eq=False)
path_3=extract_audio('video 3.mp4', 'result 3.wav', eq=False)
path_4, path_eq_4=extract_audio('video_4.mp4', 'result_4.wav', eq=True)
"""nesses exemplo, podemos ver o subprograma sendo chamado por seu nome extract_audio em diferentes situações, o que se encontra antes 
do simbolo de igual se chama variavel"""

###
"""Procedimentos não retornam valores, no código abaixo por exemplo se solictia que seja enviado um email e embora a ação seja realizada,
não irá aparecer nada como resultado"""

def enviar_email(remetente, destinatario, assunto, corpo):
    mensgaem = f"""
    subject: {assunto}
    {corpo}"""

"""Ja função retorna valores, pois ele é focada em alterar valores, deve-senotar que enquanto parametro é o que é definido na função, 
já argumento é o que está sendo recebido
Parametro:(video_file, output_file, eq=True)
Argumento:( 'video_1.mp4', 'result 1.wav', eq=False)
OU: Nome é parametro, Eduardo é argumento"""
def extract_audio(video_file, output_file, eq=True):
    path_1=extract_audio('video_1.mp4', 'result 1.wav', eq=False)


"""Quando um subprograma altera o estado de todo o software(ou seja, globalmente) chamaos ele de efeito colateral, como no 
exemplo abaixo em que mesmo sem receber valores dentro da lista ele aumenta ela com os comandos que vem a seguir, quando não existe 
efeito colateral, é uma função pura"""
###Efeito colateral
lista=[]
def aumentar_lista(val):
    lista.append(val)

aumentar_lista(1)
[1]
aumentar_lista(2)
[1,2]
###Função Pura
def soma(x,y):
    return x+y

###

#Lambdas são funções que não podem ser reproduzidas sem alterações, elas contem apenas uma expressão e são anonimas (sem nome)
#Não há lambda que não seja função
(lambda x: x+1)(1)
("vai retornar 2")

def soma(x):
    return x+1
resultado=soma(10)
"""vai retornar 11"""

###Lambdas não possuem nome, definitions (def) possuem nome

#Para se criar variantes deve-se evitar usar maiusculas e NÃO USAR espaços nem começar com numeros ou caracteres especiais;
#Parametros posicionais depende da ordem que eles foram inseridos
#Parametros de chave e valor recebem nomes, não importando a ordem que recebem os valores já que deve-se informar qual parametro 
#receberá cada valor ao citar seu nome
###Posicional
def soma(x,y):
    return x+y
print(soma(1,2))

def soma(x,y):
    return x-y
print(soma(y=2,x=1))

#Quando se depara com uma situação em que será rcebido um número incontavel de valores, usa-se o empacotamento
#Usa-se o *args (podendo ser outro nome), eu irá receber todos os argumentos inseridos e criar uma tupla, usado para os posicionais
def somatorio(*args):
    acumulador = 0
    for val in args:
        acumulador += val
    return acumulador

result = somatorio(1, 2, 3, 4, 5)
print("A Soma é:", result)

#Para argumentos nomeados, usa-se *kwargs
def cadastro(nome, telefone, *kwargs):
    print(f'{nome=}, {telefone=}, {kwargs}')

cadastro("John Doe", "123456789")

#É possível usar uma função como argumento caso ela seja anonima
#Função que recebe função é função de ordem superior
print(f"reduce:{reduce(lambda x,y:x+y,[1,2,3,4])}")

#Através da anotação de parametros, é posível determinar dentro dos parametros como os valores devem ser tratados (float, int, etc..)

#É opcional
def simulacaodejuros(
        valor: float, taxa: float, parcelas: int)-> str:
        template= "juros em {}x parcelas: {}. Valor final: {}."

        juros=valor*taxa*parcelas
        valor_final=valor+juros

        return template.format(parcelas, juros, valor_final)

result = simulacaodejuros(1000.0, 0.5, 2)
print(result)