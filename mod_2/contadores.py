"""
Count - Itertools
retorna sempre um ITERADOR
"""
from itertools import count
from turtle import clear

# contador = count()
# contador = count(start=5) # inicia pelo 5
# contador = count(start=5, step=2) # pula de dois em dois
contador = count(start=5, step=0.05) # aceita float
# contador = count(start=-1, step=-1) # Aceita valor retrogrado


# print(next(contador))

# for valor in contador:
#     print(valor)
# Loop infinito - pois count por padrão não possui fim

for valor in contador:
    # print(valor)
    print(round(valor, 2)) # arredonda em duas casas

    if valor >= 10 or valor <= -10:
        break


