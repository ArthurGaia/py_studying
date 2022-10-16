"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    
    input <- Nova tarefa
"""
# V1
# def undo(resposta_anterior, lista):
#     if len(lista) == 2:
#         print('Nada a dar Undo')
#         return lista, resposta_anterior

#     resposta_anterior = lista[-1]
#     lista.pop()
#     return lista, resposta_anterior

# def redo(resposta_anterior, lista):
#     if resposta_anterior == '':
#         print('Nada a dar Redo')
#         return lista, resposta_anterior

#     lista.append(resposta_anterior)
#     resposta_anterior = ''
#     return lista, resposta_anterior



# def adicionaTarefa(resposta_anterior, lista, tarefa):
#     if tarefa.lower() == 'redo':
#         lista, resposta_anterior = redo(resposta_anterior, lista)
#         return lista, resposta_anterior
#     elif tarefa.lower() == 'undo':
#         lista, resposta_anterior = undo(resposta_anterior, lista)
#         return lista, resposta_anterior
#     else:
#         lista.append(tarefa)
#         return lista, resposta_anterior


# lista = ['Tarefa 1', 'Tarefa 2']
# print(len(lista))
# resposta_anterior = ''
# while True:
    
#     lista, resposta_anterior = adicionaTarefa(resposta_anterior, lista, input('Digite uma tarefa ou uma ação (Undo/Redo): '))
    
#     for i in lista:
#         print(i)

# V2
# def undo(resposta_anterior, lista):
#     if len(lista) == 2:
#         print('Nada a dar Undo')
#         return resposta_anterior
        
#     resposta_anterior = lista[-1]
#     lista.pop()
#     return resposta_anterior

# def redo(resposta_anterior, lista):
#     if resposta_anterior == '':
#         print('Nada a dar Redo')
#         return ''

#     lista.append(resposta_anterior)
#     return ''

# def ls(lista):
#     for i in lista:
#         print(i)


# if __name__ == '__main__':

#     lista_tarefas = ['Tarefa 1', 'Tarefa 2']
#     resposta_anterior = ''

#     while True:
#         resposta = input('Digite uma tarefa ou Undo, redo, ls: ')

#         if resposta.lower() == 'ls':
#             ls(lista_tarefas)
#             continue
#         elif resposta.lower() == 'redo':
#             resposta_anterior = redo(resposta_anterior, lista_tarefas)
#             continue
#         elif resposta.lower() == 'undo':
#             resposta_anterior = undo(resposta_anterior, lista_tarefas)
#             continue
#         else:
#             lista_tarefas.append(resposta)
# V3
def undo(resposta_anterior, lista):
    if len(lista) == 0:
        print('Nada a dar Undo')
        return
        
    resposta_anterior.append(lista[-1])
    lista.pop()

def redo(resposta_anterior, lista):
    if len(resposta_anterior) == 0:
        print('Nada a dar Redo')
        return

    lista.append(resposta_anterior[0])
    resposta_anterior.pop()

def ls(lista):
    print()
    for i in lista:
        print(i)
    print()


if __name__ == '__main__':

    lista_tarefas = []
    resposta_anterior = []

    while True:
        resposta = input('Digite uma tarefa ou Undo, redo, ls: ')

        if resposta.lower() == 'ls':
            ls(lista_tarefas)
            continue
        elif resposta.lower() == 'redo':
            redo(resposta_anterior, lista_tarefas)
            continue
        elif resposta.lower() == 'undo':
            undo(resposta_anterior, lista_tarefas)
            continue
        else:
            lista_tarefas.append(resposta)