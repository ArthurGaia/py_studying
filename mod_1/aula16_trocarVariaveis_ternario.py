# Feito em outras linguagens de programação

from re import T


x = 10 # Luiz
y = 'Luiz' # 10

z = x # z = 10
x = y # x = 'Luiz'
y = z # y = 10

print(f'x={x} e y={y}')

# Forma Python
x = 10 # Luiz
y = 'Luiz' # 10
z = 'Arthur'

x, y, z = z, x, y

print(f'x={x}, y={y} e z={z}')

# Ternário
"""
logged_user = True

if logged_user:
    msg = 'Usuario logado.'
else:
    msg = 'Usuario precisa logar.'
print(msg)
"""
# Versão ternária
logged_user = True

msg = 'Usuário logado.' if logged_user else 'Usuario precisa logar.'

print(msg)

#ex2
"""
idade = 18

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar')
"""

idade = input('Qual tua idade?')
if not idade.isnumeric():
    print('Você precisa digitar apenas numeros')
else:
    idade = int(idade)
    eh_maior = (idade>=18)
    msg = 'Pode acessar' if eh_maior else 'Nao pode acessar'
    
    print(msg)
