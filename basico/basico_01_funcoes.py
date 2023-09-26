def pizzaria():
    valores =[15, 5, 8, 7, 10]
    sabores = ["camarão", "mussarela", "frango", "calabresa", "portuguesa"]
    for sabor, valor in zip (sabores, valores):
        print(sabor, valor)
pizzaria()
