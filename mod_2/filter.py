from dados import produtos, pessoas, lista

# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))

# Em list comprehension
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

nova_lista = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista:
    print(produto)

def filtra(produto):
    if produto['preco'] > 50:
        return True

nova_lista = filter(filtra, produtos)
for produto in nova_lista:
    print(produto)

def filtraIdade(pessoa):
    if pessoa['idade'] < 18:
        return True

nova_lista = filter(filtraIdade, pessoas)
for pessoa in nova_lista:
    print(pessoa)