#O corpo do labda contém apenas uma expressão e não precisa do return
anonimo=lambda x:10 if x<10 else x
print(anonimo(21))
#def contem varias linhas
def simulacaodejuros(
        valor: float, taxa: float, parcelas: int)-> str:
        template= "juros em {}x parcelas: {}. Valor final: {}."

        juros=valor*taxa*parcelas
        valor_final=valor+juros

        return template.format(parcelas, juros, valor_final)

result = simulacaodejuros(1000.0, 0.5, 2)
print(result)
#procedimentos, embora teoricamente não tenham retorno, no python se comportam como função e resultam em none ou void

#é possível comprovar os booleanos através dos lambda
id=lambda x:x
TRUE=lambda x:lambda y:x
FALSE=lambda x: lambda y:y
OR =lambda x: lambda y:x(TRUE)(y)
AND =lambda x: lambda y:x(y)(FALSE)

#Em defs, usamos o alinhamento para inserir uma função dentro de outra, assim, ao chamarmos a função externa, também chamamos a interna
#Também é possível juntar funções dentro de lamdas, como se mostra nos exemplos a seguir
def add(x):
    def inner(y):
        return x+y
    return inner
print(add(1)(2))


def ola(nome):
    def formata():
        return f'Olá {nome}, tudo bem?'
    return formata()
print(ola("julia"))

oii= lambda nome: (lambda: f'Olá {nome}, tudo bem?')()
print(oii("julia"))

#compartilhamento de escopo: é como se a função tivesse uma memoria interna que sabe quem é x e quem é y
#É como se fosse um atributo do objeto da função
#O nome da memória tem closure
#Para polimorfismo se usa decoradores

#Existem as corrotinas: modelo de unidade de controle simétrico, em que a responsabilidade é dividida e os programas não param de ser executados
#O subprograma permanece trabalhando parcialmente, "trocando ideias" e não simplesmente parando
#Para isso, se usa a palavra yield

def corrotina():
    print("comecei")
    yield
    print("voltei")
    yield

c=corrotina()
next(c)
next(c)

#a corrotina seda a vez para o programa principal, com interrupção mas não fim, como em um ping pong (ex:semaforo)
#Existem debates se corrotinas podem ou não serem consideraos geradores
#Geradores criam dados
#Iteravel é desmonatvel, como em uma lista
#Com os geradores então se torna possível aplica-los em listas (como no for)

def gerador():
    yield 1
    yield 2
    yield 3
g=gerador()

for val in gerador():
    print(val)

#Da mesma forma, é possível tornar infinita
def gerador1():
    va=0
    while True:
        yield va
        va+=1
g1=gerador1()
#for va in gerador1():
    #print(va)

#lazy evaluation é quando se é preciso chama-lo
#cria-se subgeradores para delegar tarefas para geradores distintos

def subgerador():
    yield from gerador
for val in gerador():
    print(f'subgerador:{val+1}')

#map é um tipo de gerador (checar itertool para maiores dados)

"""
yield para
yield com algo na frente gera dados
yield from delega
yield com algo na atras recebe dados
"""

def corrotina1():
    print ('entrei')
    val=yield
    print(f'recebi:{val}')
co=corrotina1()
next(co)
co.send("igor")

#existe também o async (corrotinas assincronas) e o await que rabalha como se fosse o yoield from em uma corrotina assincrona
