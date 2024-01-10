from itertools import product, zip_longest, combinations, filterfalse, starmap, count, islice, permutations, cycle, pairwise, repeat, accumulate, takewhile, dropwhile, chain, compress
from functools import reduce
import time

def reducee():
    print(f"reduce:{reduce(lambda x,y:x+y,[1,2,3,4])}")


def exemplo_lambda():
    print(f"accumulate:{list (accumulate([1,2,3,4],lambda x,y:x+y))}")
def teste():
    def filtro(f):
        return f is True
    dado = [True, False, True, False, True, False]
    valores= filterfalse(filtro, dado)
    resultado = list(valores)
    print(f"funcao_filter_false:{resultado}")
    print("   ")
def main():
    
    qual=input("qual função gostaria de rodar? ")
    if qual=="falsefilter":
        pass

    elif qual=="accumulate":
        teste()

    elif qual=="reduce":
        reducee()
if __name__=="__main__":
    main()