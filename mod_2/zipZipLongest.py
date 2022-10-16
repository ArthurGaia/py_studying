"""
Zip - Unindo Iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count
indice = count()

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

print(dict(cidades_estados))

# for valor in cidades_estados:
#     print(valor)

# Zip Longest
cidades_estados_longest = zip_longest(
    estados, 
    cidades, 
    fillvalue='Estado') 
# fillvalue - definir valor padrão
print(list(cidades_estados_longest))

# Count - para não dar loop infinito 
cidades_estados_count = zip(
    indice,
    estados, 
    cidades, 
) 


for indice, estado, cidade in cidades_estados_count:
    print(indice, estado, cidade)

# Exemplo gerador usando zip
variavel = ((x, y) for x, y in zip('Alo','Alo'))
print(list(variavel))