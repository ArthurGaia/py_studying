"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome
"""
def saudacao(sau, nome):
    return f'{sau} {nome}'

print(saudacao('Olá', 'Arthur'))

"""
2 - Crie uma função que recebe 3 numeros como parâmetros e exiba a soma entre eles.
"""
def soma(n1, n2, n3):
    return n1 + n2 + n3

print(soma(1, 2, 3))
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""
def percentual(n1, percent):
    return n1 + (n1 * (percent / 100))

print(percentual(100, 50))
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o número enviado
"""

def FizzBuzz(n1):
    if n1 % 3 == 0 and n1 % 5 ==0:
        return 'FizzBuzz'
    if n1 % 3 == 0:
        return 'Fizz'
    if n1 % 5 ==0:
        return 'Buzz'
    return n1

print(FizzBuzz(8))