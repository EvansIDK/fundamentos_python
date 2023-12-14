from itertools import product, zip_longest
"""teste=combinations('ABCDE', 2)
print(list(teste))"""

pizza_sabores= ["camarão", "mussarela", "frango", "calabresa", "portuguesa", "frango"]
pizza_valores= [15, 5, 8, 7, 10]
comb=product(zip_longest(pizza_sabores, pizza_valores, fillvalue=0))
print (list(comb))