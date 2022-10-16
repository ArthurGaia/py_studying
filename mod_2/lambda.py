# def funcao(x, y):
#     return x * y

# var = funcao(2,5)
# print(var)
# é o mesmo que:

a = lambda x, y: x * y
print(a(2,2))

# funcionalidade

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# Ordenar sem salvar a lista modificada
print(sorted(lista, key=lambda i: i[0], reverse=True))
# Ordenar pelo nome
print(sorted(lista, key=lambda i: i[1], reverse=True))
# Ordenar pelo numero

# Ordenar mudando valor
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)