from itertools import groupby, tee

alunos = [
    {'nome':'Luiz', 'nota':'A'},
    {'nome':'Leticia', 'nota':'B'},
    {'nome':'Fabrício', 'nota':'A'},
    {'nome':'Rosemary', 'nota':'C'},
    {'nome':'Joana', 'nota':'D'},
    {'nome':'João', 'nota':'A'},
    {'nome':'Eduardo', 'nota':'B'},
    {'nome':'André', 'nota':'A'},
    {'nome':'Anderson', 'nota':'C'},
    {'nome':'José', 'nota':'B'},
]
ordena = lambda item: item['nota']
# Precisa ordenar primeiro para poder utilizar o group by
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados) # faz a cópia para duas outras variáveis, pois no código dentro consome totalmente o iterável

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram nota {agrupamento}')
    # for aluno in valores_agrupados:
    #     print(aluno)
    # print()