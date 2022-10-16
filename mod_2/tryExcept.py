# https://docs.python.org/3/library/exceptions.html
from traceback import print_tb


try:
    # print(a) Name Error
    
    # a = []
    # print(a[1]) Erro de index
    a = {}
    # print(a[1]) Key Error

except NameError as erro:
    print(erro)
except (IndexError,KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro: # Ela pega qualquer err que ocorrer no bloco try e não foi especificado
    print('Ocorreu um erro inesperado')
else: # Executa toda vez que o try for executado sem nenhuma exceção
    print(a)
finally: # Executa independente de ter sido lançado exceção ou não. Muito usado pra fechar arquivos abertos durante a execução
    print('finalmente')
    # a = None Muito usado pra dar um valor padrão se caso houver falha ne declaração

print('bora continuar') 

# Raise exceptions
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise
        
try: 
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)


# Levantar a própria excessão
def divide1(n1, n2):
     if n2 == 0:
        raise ValueError("Segundo número não pode ser 0") # não estando no bloco try, retorna erro
     return n1 / n2

try:
    print(divide1(2,0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    # print(error)

# Exemplo try como condicional
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return
        except ValueError:
            pass

while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Erro: Isso não é um número')
    else:
        print(numero * 2) 