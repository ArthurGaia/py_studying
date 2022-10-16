# https://docs.python.org/3/library/functions.html#open
# 'r' open for reading (default)
# 'w' abre pra escrever, mas apaga o arquivo primeiro
# 'x' open for exclusive creation, failing if the file already exists
# 'a' abre pra escrever, adicionando os valores aos valores já existentes, sem apagar eles
# 'b' binary mode
# 't' text mode (default)
# '+' open for updating (reading and writing)

file = open('abc.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0,0) # define o cursor para o topo do arquivo
print('Lendo linhas')
print(file.read()) # Lê o arquivo inteiro como uma String
print(20*'#')

file.seek(0,0)
print(file.readline(), end='') # Lê linha a linha 
print(file.readline(), end='') # End tira o parágrafo a mais
print(file.readline(), end='')

file.seek(0,0)
print(file.readlines()) # Retorno literal, como lista

file.close() # é imprescindível fechar

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
except:
    pass
finally:
    file.close()

# Gerenciador de contexto, forma mais pythonica de fazer as coisa
with open('abc.txt', 'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())

with open('abc.txt', 'a+') as file: # Adiciona coisas ao arquivo, sem cortar ele
    file.write('Linha4\n')
    file.write('Linha5\n')
    file.write('Linha6\n')

    file.seek(0)
    print(file.read())

import os 
os.remove('abc.txt') # Deleta arquivo

import json
d1 = {
    'Pessoa 1':{
        'nome':'Luiz',
        'idade': 25
    },
    'Pessoa 2':{
        'nome':'Rose',
        'idade': 30
    },
}
d1_json = json.dumps(d1, indent=True)
print(d1_json)
# Salvou o arquivo json
with open('abc.json', 'w+') as file:
    file.write(d1_json)
# Liu o arquivo Json
with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)