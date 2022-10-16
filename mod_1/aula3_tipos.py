"""
Tipos de dados
str - String
int - Integer
float - float
bool - boolean
"""

from pickle import TRUE


print('Arthur',type('Arthur'))
print(10,type(10))
print(10.01,type(10.01))

# comparação boolean:
# boolean não pode ser declarado como 0 ou 1, mas sim como True/False

print(True,type(True)) 
print(10==10, type(10==10))
print('l'=='L',type('l'=='L')) # false, case sensitive

#typecast
print('Arthur', type('Arthur'), bool('Arthur'))

#false
print(bool(0))
print(bool('')) #coisas vazias o python costuma traduzir em falso

#String para inteiro/float

#print('Arthur', int('Arthur')) Exception

print('10', int('10'), type(int('10')))
print('10.1', float('10.1'), type(float('10.1')))


# concatenar
print('10' + '10')

#nome, idade, float, maior de idade
print('Arthur', type('Arthur'), 21, type(21), 1.8, type(1.8), 21>18, type(21>18))