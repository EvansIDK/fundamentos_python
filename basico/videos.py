from itertools import product, zip_longest, combinations, filterfalse, starmap, count, islice, permutations, cycle, pairwise, repeat, accumulate, takewhile, dropwhile, chain, compress
from functools import reduce
import time

"""
COMBINATIONS: O exemplo abaixo é de uma função combinatória do itertool, o combination, que consiste em uma função que cria possibilidades
de combinação ao receber um valor de 'itens' serem combinados, neste caso ABCDE, e o numero de itens que podem estar presentes,
neste caso em especifico 2. É importante se atentar ao fato que, na combinação, a ordem apresenta um papel importante.
"""
#combination exemplo do vídeo
combinacao=combinations('ABCDE', 2)
print(f"combiations: {list(combinacao)}")
print("   ")

###

"""
PERMUTATIONS:O exemplo abaixo é de uma função combinatória do itertool, o permutation, que, talqual o combination, consiste em uma função  
que cria possibilidades de combinação ao receber um valor de 'itens' serem combinados, neste caso ADFV, e o numero de itens que podem 
estar presentes nesta combinação, neste caso em especifico 4. É importante se atentar ao fato que, na permutação, 
a ordem que os valores são inseridos não apresenta um papel importante, visto que as combinação permitem valores se repitam em ordens
diferentes, por exemplo, podem aparecer na seqûencia tanto A,D quando D,A.
"""
#permutation
permutacao=permutations('ADFV',4)
print(f"permutations: {list(permutacao)}")
print("   ")

###

"""
PRODUCT:Abaixo se encontra a função combinatória product que utiliza das lista que lhe forem oferecidas para criar uma terceira lista
contendo as possibilidades de combinações das duas primeiras.
"""
#product
cores= ["azul", "verde", "roxo", "vermelho", "amarelo", "laranja"]
num= [15, 5, 8, 7, 10,6]
produto=(product(cores, num))
produto_final=list(produto)
print (f"products: {produto_final}")
print("   ")

###

"""
PAIRWISE: Outra função combinátoria é o pair wise que, ao ser fornecido com uma lista de itens, cria uma lista de tuplas de possibilidades, 
contudo, é limitado a apenas resultados com dois valores e não é capaz de mesclar listas, apenas criando pares como seu nome indica.
"""
#pairwise
pizza_sabores= ["camarão", "mussarela", "frango", "calabresa", "portuguesa", "frango"]
pares=(pairwise(pizza_sabores))
pares_final=list(pares)
print (f"Pares : {pares_final}")
print("   ")

###

"""
ZIP_LONGEST:Abaixo se encontra a função zip_longest, que exerce seu papel através da sua capacidade de unir listas de tamanhos diferentes 
visto que, é possível inserir o comando 'fillvalue=n' ao lado das listas que serão unidas, permitindo assim que o valor ausente seja 
preenchido com o que estiver escrito após o =.
"""
#zip_longest
pizza_sabores= ["camarão", "mussarela", "frango", "calabresa", "portuguesa", "frango"]
pizza_valores= [15, 5, 8, 7, 10]
juncao=(zip_longest(pizza_sabores, pizza_valores, fillvalue=None))
uniao=list(juncao)
print (f"União : {uniao}")
print("   ")

###

"""FILTER: Filter é uma função que como o própio nome indica, é capaz de filtrar e ignorar determinados valores dentro de uma lista
no momento de exibi-la. Para utiliza-la, é preciso criar uma função que estabeleça o que exatamente deve ser buscado, neste caso,
ao ser alimentada pela lista, a função irá buscar pela nome jose, que é como a varivel s foi definida. Após isto, se cria a lista
com os elemento e, logo na linha seguinte, se cria uma nova varivel que ir"""
#filter
def funcao_filter(s):
    return s=='jose'
dados = [True, True, 'jose']
filters = filter(funcao_filter,dados) #precisa de 2 valores, um indicando como filtrar e o outro onde filtrar
result = list(filters)
print(f"funcao_filter:{result}")
print("   ")

###

"""FILTERFALSE: filterfalse é como o nome indica, uma função oposta ao do filter, inserindo na lista final o contrário do que foi proposto,
como no exemplo a seguir em que ao ser solicitado o true, é retornado apenas o false."""
#filter false usando booleano
def filtro(f):
    return f is True
dado = [True, False, True, False, True, False]
valores= filterfalse(filtro, dado)
resultado = list(valores)
print(f"funcao_filter_false:{resultado}")
print("   ")

###

"""STARMAP: starmap é uma função que permite apllicar determinadas funções dentro de tuplas, como no exemplo abaixo em que
a função de somar os valores abaixo agrega valores de x e y para números das tuplas e determina que sejam somados, assim, se torna possível 
aplicar o procedimento a lista de tuplas."""
#starmap
def star_map(x, y):
    return x+y
pares = [(1, 2), (3, 4), (5, 5)]
somado = starmap(star_map, pares)
result = list(somado)
print(f"funcao_star_map:{result}")
print("   ")

###

"""COUNT e ISLICE: A função count pcria um contador em uma váriavel; nela é criada uma varivel que receberá a função e 
dentro dela um start, para determinar em qual número a contagem deve começar, e um step para definiir de quanto em quanto a contagem deve 
andar (por exemplo de dois em dois). Já o slice permite "andar" dentro desta váriavel, tornando a função lazy e fazendo com que seja 
preciso informar o número desejad de valores do contador para que sejam exibidos."""
#count e islice(para que tenha um limite)
valoress = count(start=0, step=3)
result = islice(valoress, 5)
print(f"count_islice:{list(result)}")
print("   ")

###

"""CYCLE e REPEAT: A função cycle cria, coo o nome indica, um ciclo de elementos que será repetido seguindo a ordem indicada.
Já a o repeat faz com que a função em questão seja repetida um determinado número de vezes. Nesse caso em questão a união deles permitiu
se criar um semafaro, onde a variavel semafaro recebe uma lista, em seguida se é criado a variavel ciclo, que vai receber a aplicação da
função cycle na lista semafaro. Para o repeat, se cria um "for" para andar pela lista, em que a varivel usada deve receber o nome do que 
está sendo lido e o next, para sempre passar para o próximo item do ciclo, no número de vezes que for informado dentro do repeat, neste 
caso 6."""
#cycle
semafaro = ['verde', 'amarelo', 'vermelho']
ciclo = cycle(semafaro)
for i in repeat(ciclo,6):
    i = next(ciclo)
    print(f"ciclo_repeat:{i}")
    time.sleep(0)
print("   ")

###

"""ACCUMULATE: A função accumulate, como o nome indica, realiza a acumulação ao realizar o ato que for solicitado dentro do lambda, 
no caso abaixo sendo a soma, assim ela passa de elemento em elemento, fazendo 1, 1+2, 3+3, 6+4"""
#accumulate
print(f"accumulate:{list (accumulate([1,2,3,4],lambda x,y:x+y))}")
print("   ")

###

"""TAKEWHILE: A função takewhile faz com que a lista seja lida até que se encontre um elemento diferente do proposto na lambda"""
#takewhile
lista=takewhile(lambda x:x!=3,[1,2,3,4])
print(f"takewhile:{list(lista)}")
print("   ")
###

"""DROPWHILE: A função dropwhile faz com que a lista seja lida a partir do momento que se e contra um elemento diferente do proposto na 
lambda, coo neste caso ao se pedir algo diferente de 3, a lista só vai começar a ser lida do número 3 em diante, já que ele irá o que vem 
antes desse elemento em questão."""
#dropwhile
lista=dropwhile(lambda x:x!=3,[1,2,3,4])
print(f"dropwhile:{list(lista)}")
print("   ")

###

"""CHAIN: Une dois iterados em um único."""
#chain
print(f"juncao_iterados:{list(chain(iter('abc'), iter('defg')))}")
print("   ")

###

"""COMPRESS: Relaciona valores de determinada lista com respectivos valores de outra, agregando caracteristas de verdadeiro ou falso."""
#compress
dados=['a','b','c']
dados2=[True,False,True]

for i in compress(dados,dados2):
    print(f"Verdadeiros:{i}")
    print("   ")

"""REDUCE: Reduce é uma função do functools, outro banco de funções, que realiza algo de maneira semelhante ao accumulate, porém de forma
direta."""
#functools reduce
print(f"reduce:{reduce(lambda x,y:x+y,[1,2,3,4])}")

###

def main():
    pass

if __name__=="__main__":
    main()