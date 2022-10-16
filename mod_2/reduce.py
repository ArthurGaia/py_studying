from dados import pessoas, produtos, lista
from functools import reduce

# Acumulador
acumula = 0
for item in lista:
    acumula += item
print(acumula)

# Reduce faz a mesma coisa
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos)) # Média de preços

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))