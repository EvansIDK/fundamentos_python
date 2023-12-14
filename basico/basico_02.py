"""tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)
frutas = ('maçã', 'banana', 'laranja', 'uva')
print(frutas[0]) 
print(frutas[1])  
for fruta in frutas:
    print(fruta)"""


paises_europa = ('espanha', 'frança', 'itália', 'holanda') 
paises_africa = ('africa do sul', 'moçambique', 'camarões', 'marrocos', 'camarões')


def main():
  contar_tupla = tupla_metodo_count()
  indice_tupla = tupla_metodo_index()


def tupla_metodo_count():
  """
  tupla.count(elemento)
  """
  n_vezes = paises_africa.count('camarões')
  print("a palavra aparece",n_vezes)
 


def tupla_metodo_index():
  """
  tupla.index(elemento, inicio, fim)
  - elemento é obrigatório
  - índices de início e fim opcionais
  """
  indice_paises_europa = paises_europa.index('espanha' )
  print(indice_paises_europa)


if __name__ == "__main__":
  main()