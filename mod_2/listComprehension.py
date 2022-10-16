l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v,v2) for v in l1 for v2 in range(3)]
#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), 
# (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), 
# (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), 
# (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), 
# (9, 0), (9, 1), (9, 2)]

l2 = ['Luiz', 'Mauro', 'Maria']

ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = {
    ('chave', 'valor'),
    ('chave2', 'valor2')
}
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
# ex6 = [v for v in l3 if v % 2 == 0]
ex6 = [v for v in list(range(100)) if v % 3 == 0 if v % 8 == 0]
print(ex6)

# com else
# ex7 = [v if v % 3 == 0 else 0 for v in l3]
ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)

# formato dos if
# [if : operador ternário ... for ... if : Filtros dos valores listados]

# É o mesmo que:
#  for l in range(1,11):
    # for c in range (1,6):
    #   print(x, y) 


linhas_e_colunas = [
    (l, c)
    for l in range(1,11)
    for c in range (1,6) 
]

# Tronar listas flat
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [
    y # Trás valor em y
    for x in numeros # trás a sublista no valor de x
    for y in x] # seleciona um valor de y dentro de x (sublista)

print(numeros)
print(flat)

# Com dicionarios
lista = {
    ('chave', 'valor'),
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
}

d1 = {x:y for x, y in lista}
# d1 = {x.upper():y*2 for x, y in lista}

d2 = {x:y for x, y in range(5)} # dict comprehension
# d2 = {f'chave_{x}':x**2 for x range(5)}
# d2 = {x for x in range(5)} Set Comprehension

print(d1)