"""
1 - Crie uam função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada.
"""

def ola_mundo():
    return 'Olá Mundo!'

def mestre(funcao):
    return funcao()

exec = mestre(ola_mundo)
print(exec)

"""
2 - Crie uma função1 que receeb uma função2 como parâmetro e retorne o valor 
da função2 executada. Faça a função1 executar duas funções que recebam um numero 
diferente de argumentos
"""

def execucao(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = execucao(fala_oi, 'Arthur')
print(executando)

executando1 = execucao(saudacao, 'Arthur', saudacao='Bom dia!')
print(executando1)