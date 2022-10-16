"""
Split, Join, Enumerate
# Split - Dividir uma string # str
# Join - Juntar uma lista # str
# Enumerate - Enumerar elementos da lista #iteráveis
"""
string = 'O Brasil é o pais do futebol, o Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'{valor}')

print(20*'#')

for valor in lista_2:
    print(f'{valor}')

print(20*'#')

for valor in lista_1:
    print(f'{valor}: {lista_1.count(valor)}')

# for valor in lista_2:
#     print(f'{lista_2.count(valor)}')