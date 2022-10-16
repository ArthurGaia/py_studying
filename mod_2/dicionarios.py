d1 = {'chave':'valor da chave'} # Criar um dicionario
d1['nova_chave'] = 'Valor da nova chave' # Adicionar novo valor a um dicionário

print(d1['chave'])

# Outra forma de construir dicionarios em py
d2 = dict(chave='Valor da chave', chave1='Valoe da outra chave')

print(d2)

# Chaves precisam ser unicas
# Se elas se repetirem
# apenas a ultima declarada irá contar

# d2['nomenaoexiste'] = 'Agora existe'

print(d2.get('nomenaoexiste')) # Retorna None
if d2.get('nomenaoexiste') is not None: # Validação teste
    print(d2.get('nomenaoexiste'))

# Para atualizar o valor da chave
d1['str'] = 'String test'
d1['str'] = 'String apenas' # Sobrepõe se já existe valor
print(d1.get('str'))

# também pode utilizar a função update
d1.update({'str':'String'})
print(d1.get('str'))

# deletando regisro
del d1['str']
print('str' in d1) # V ou F
print('valor da chave' in d1.values()) # Checagem se há valor da chave nos valores do dicionario

# Tamanho são por pares
print(len(d1))

# Iterável
d3 = {
    'chave1':'Valor1',
    'chave2':'Valor2',
    'chave3':'Valor3',
}

for k in d3: # Iterar sobre chaves
    print(k)

for v in d3.values(): # Iterar sobre valores
    print(v)

for k in d3.items(): # Iterar sobre Items (Ambos)
    print(k)
    # print(k[0], k[1]) Valores separadamente

for k, v in d3.items():
    print(k, v) # Com desempacotamento

clientes = {
    'cliente1' : {
        'nome' : 'Arthur',
        'sobrenome' : 'Gaia',
    },
    'cliente2' : {
        'nome' : 'Hiato',
        'sobrenome' : 'Miyamura',
    },
    'cliente3' : {
        'nome' : 'Maria',
        'sobrenome' : 'Yamamoto',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# Para passar informações de um dicionário para uma 
# var qualquer, nao pode ser passado por v = d1, 
# pois ele referencia como ponteiro, e passa a ter 
# o mesmo valor de memória. Portanto:

v = d1.copy() # shallow copy
v[1] = 'Arthur'
print(v, d1)

# Porém ainda pode haver referência, 
# se houver uma lista dentro do dicionário

# Portanto:
import copy
v = copy.deepcopy(d1) # Cópia correta, Valor de um não referencia o outro

# Converter Lista/tuplas em dict
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d4 = dict(lista)
print(d4)

# pop em dict
# d4.popotem() Apaga último valor
d4.pop('c3')
print(d4)

# Concatenar dict
d4.update(d3)
print(d4)