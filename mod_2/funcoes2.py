def func(*args): # Utilizado para quando não se tem ideia da quantidade de argumentos a serem utilizados
    print(args) # args retorna uma tupla, então tem seu comportamento similar a uma lista
    args = list(args) # torna args em lista


func('Arthur')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(lista, '6') # se não desempacotar, ele entenderá que que a lista ocupa a posição 0 da tupla
func(*lista, *lista2) # Lista desempacotada

# **kwargs - argumentos chaves

def func2(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)

func2(*lista, *lista2, nome='Luiz', sobrenome='Miranda',idade=30)
