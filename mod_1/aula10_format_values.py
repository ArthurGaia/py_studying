"""

:s - Texto (strings)
:d - Inteiros (int)
:f - Float 
:.(Numero)f - Quantidade de casas decimais (Float)
:(Caractere)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

##### Exemplo 1
num_1 = 1
print('{:0>10}'.format(num_1)) ## Format
print(f'{num_1:0>10}') ## f Strings
# Retorno: 0000000001

print('{:0<10}'.format(num_1)) ## Format
print(f'{num_1:0<10}') ## f Strings
# Retorno: 1000000000

print('{:0^10}'.format(num_1)) ## Format
print(f'{num_1:0^10}') ## f Strings
# Retorno: 0000100000

print('{:5^10}'.format(num_1)) ## Format
print(f'{num_1:5^10}') ## f Strings
# Retorno: 5555155555

# exemplo 2
a = 10
b = 3
divisao = a / b

print(f'{divisao:0>5.2f}')

nome = 'Arthur Gaia'
print(f'{nome:*^50}')
# Retorno: *******************Arthur Gaia********************    

# Right just
print(nome.rjust(30))
# Retorno:                    Arthur Gaia


# Left Just
print(nome.ljust(30))
# Retorno: Arthur Gaia

print(nome.lower()) # Tudo Minusculo
print(nome.upper()) # Tudo Maisculo
print(nome.title()) # Primeiras letras maisculas
