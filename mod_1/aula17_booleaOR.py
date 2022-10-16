nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada =(')

# pode ser
print(nome or 'Você não digitou nada =(')
# print(nome or None or False or 0 or 'Você não digitou nada.')

a = 0 
b = None
c = False
d = []
e = {}
f = 22
g = 'Arthur'

variavel = a or b or c or d or e or f or g
print(variavel)

if a:
    variavel = a
elif b:
    variavel = b
#.
#.
#.
elif g:
    variavel = g