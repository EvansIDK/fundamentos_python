nome = "maria fernanda de moura souza"
pizza_valor= 10
#print(type(nome), pizza_valor)
pizza_sabores= ["camarão", "mussarela", "frango", "calabresa", "portuguesa", "frango"]
pizza_valores= [15, 5, 8, 7, 10]
pizza= f"a pizza de {pizza_sabores[0]} custa {pizza_valores[0]}"
print (len(pizza))
total= pizza_valores[0]*2
print(total)
print(pizza_valores[0:3])
#append
pizza_sabores.append("strogonoff")
print(pizza_sabores)
#len
print("existem", len(pizza_sabores), "sabores")
sorted(pizza_sabores)
pizza_sabores.reverse()
print(pizza_sabores)
#tirar palavra repetida
def tupla_metodo_index():
    n_vezes = pizza_sabores.count("frango")
    print("a palavra aparece",n_vezes)

    if n_vezes>=2:
        pizza_sabores.remove("frango")
        print (pizza_sabores)
    else:
        print(pizza_sabores)
tupla_metodo_index()

#conjunto/seth é interseccional

# dicionario
pessoa1 = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
pessoa2 = {'nome': 'Maria', 'idade': 30, 'cidade': 'Rio de Janeiro'}
pessoa3 = {'nome': 'Carlos', 'idade': 22, 'cidade': 'Belo Horizonte'}


print(f"Nome: {pessoa1['nome']}, Idade: {pessoa1['idade']}, Cidade: {pessoa1['cidade']}")
print(f"Nome: {pessoa2['nome']}, Idade: {pessoa2['idade']}, Cidade: {pessoa2['cidade']}")
print(f"Nome: {pessoa3['nome']}, Idade: {pessoa3['idade']}, Cidade: {pessoa3['cidade']}")

