"""
For in em Python
Iterando Strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'

for letra in texto:
    print(letra)

for n, letra in enumerate(texto):
    print(n, letra)

for n in range(5, 10, 2):
    print(n)

for n in range(100):
    if n % 8 == 0:
        print(n)

print(10*'################')

nova_string = ''
for letra in texto:
    if letra == 't' or letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

#For pode ter Else

lista = [ 'abc', 'def', 'ghi']
for valor in lista:
    if valor.lower().startswith('d'):
        break
else:
    print('Não há valor que começa com D')