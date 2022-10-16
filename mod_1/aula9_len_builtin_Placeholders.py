"""
    função len, contagem de caracteres
"""

usuario = input("digite seu usuário: ")

if len(usuario) > 6:
    print("Tudo certo!")
else:
    print("Errado!")

print(usuario.__len__())

#built-in types
#https://docs.python.org/3/library/stdtypes.html

"""
    Função de checagem de numeros
"""

from curses.ascii import isdigit
import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
 
# False
print(is_number('123a'))  # False


"""
    isnumeric()
    isdigit()
    isdecimal()
"""
#Sample
num1 = input("Digite um numero: ")
num2 = input("Digite um numero: ")

if is_number(num1) and is_number(num2):
    num1 - float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('ERROR!')

#bloco Try

try:
    num1 - float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR!')

#Pass e elipsis - placeholders

valor = True

#pass
if valor:
    pass
else:
    print('Tchau')

#elipsis
if valor:
    ...
else:
    print('Tchau')