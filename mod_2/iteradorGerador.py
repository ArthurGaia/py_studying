import sys
import time

# var = list(range(5))
var = [x for x in range(5)]

print(hasattr(var, '__iter__')) # lista é iterável

var = 1

print(hasattr(var, '__iter__')) # valor literal não é iterável

var = 'String'

print(hasattr(var, '__iter__')) # string é iterável

# for transforma um objeto interável em um iterador
print(hasattr(var, '__next__')) # busca se é um objeto iterador

var1 = [x for x in range(5)]
var1 = iter(var1) # torna a variável em um iterador
print(hasattr(var1, '__next__')) # Agora true
# Objeto iterável, pode ser executado usando next

print(next(var1)) # primeiro valor : 0
print(next(var1)) # segundo valor : 1
print(next(var1)) # terceiro valor : 2

var2 = list(range(1000))
# puxando os bytes de uma lista
print(sys.getsizeof(var2))

# Gerador - a função abaixo simula a lentidão do sistema com valores grandes
# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r

def gera(): # Função gerador
    for n in range(100):
        yield n # executa dando um valor por vez de retorno
        time.sleep(0.1)

g = gera()
print(hasattr(g, '__iter__')) # Iteradores também são iteráveis
print(hasattr(g, '__next__')) # será também iterador
# for v in g:
#     print(v)

# Exemplo 2
def gera1():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

g1 = gera1()
for v in g1:
    print(v)

# transformar lista em gerador 
lista = [x for x in range(1000)]
print(type(lista), sys.getsizeof(lista))
lista = (x for x in range(1000)) # gerador
print(type(lista), sys.getsizeof(lista))


