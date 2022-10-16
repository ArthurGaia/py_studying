def saudacao(msg='Olá', nome='usuario'): # define valores padrões
    print(msg, nome)

saudacao()
saudacao(nome='Zezim') # define o valor por variável
saudacao(nome='Arthur', msg='Hallo!') # Valores podem ser invertidos
saudacao('Oi', 'Luiz') # dessa forma o valor é sobreposto

""" Sem retorno ela possui o valor 'None'"""
def funcao(var):
    #print(var)
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')

"""  """

def divisao(n1, n2):
    if n2 == 0:
        return # retorna valor 'None'
    return n1 / n2

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta inválida.')

""" Retornam qualquer tipo de dado """

def dumb():
    return [1,2,3,4,5]
    #return ('Arthur', 'Gaia') # retorna tuplas

print(dumb(), type(dumb()))