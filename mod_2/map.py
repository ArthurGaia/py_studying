from dados import produtos, pessoas, lista

# Usar como list Comprehension
# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista] # com list comprehension
# print(list(nova_lista))
print(nova_lista)

# com dicionarios
precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)

# Ex1
# Para retornar o dicionario a forma que ele estava 
# precisa estar em funcao
def aumenta_precos(p):
    p['preco'] = round(p['preco'] * 1.05, 2) # Adiciona 5% ao valor, e arredonda em duas casas
    return p

novos_produtos = map(aumenta_precos, produtos)
for produto in novos_produtos:
    print(produto)

# Ex2 
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p
# nomes = map(lambda p: p['idade'] * 1.20, pessoas)
idades = map(aumenta_idade, pessoas)

for pessoa in idades:
    print(pessoa)