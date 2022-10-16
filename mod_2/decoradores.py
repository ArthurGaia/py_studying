from time import time, sleep

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada')
        funcao(*args, **kwargs)
    return slave

@master # decorador
def fala_oi():
    print('Oi')

@master
def outra_funcao(msg):
    print(msg)

outra_funcao('Olá, eu sou o Arthur')
# fala_oi = master(fala_oi)
# A função já foi decorada em tempo de execução 
# mesmo que ela seja sobrescrita 
# fala_oi()

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000 # para retornar em ms
        print(f'\nA função {funcao.__name__} ' # __name__ retorna o nome da funcao
              f'levou {tempo:.2f} ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(10000):
        print(i, end='')
        # sleep(1)

demora()