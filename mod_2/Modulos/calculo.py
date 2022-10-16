import math

# em Python não tem comstante, então por convensão 
# utilizar palavra com letras maiusculas 
PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__': # só executa se o arquivo atual for o main
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

print(__name__) # Quando importado, o modulo retorna seu nome em vez de main