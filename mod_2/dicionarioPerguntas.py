perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'a': '2',
            'b': '4',
            'c': '6',
            'd': '8'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 * 5 ?',
        'respostas': {
            'a': '15',
            'b': '35',
            'c': '20',
            'd': '25'
        },
        'resposta_certa': 'd',
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items(): 
    print(f'{pk}: \n{pv["pergunta"]}')

    print('Opções:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1
        print('Correto!')
    else:
        print('Errado')

    print()
print(f'Voce acertou {respostas_certas}')