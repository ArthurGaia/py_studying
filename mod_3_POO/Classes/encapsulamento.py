"""
public, protected, private
convenções:
_ protected - Recomendação mais "fraca" (public com _)
__ private (forma de acessounica: _NOMECLASSE__nomeatributo)
"""
from turtle import update


class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados
    
    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1, 'Arthur')
bd.inserir_clientes(2, 'Gaia')
bd.inserir_clientes(3, 'Rose')
bd.__dados = 'outra coisa' # o python cria uma nova variável como resultado do uso de __
print(bd.__dados)
print(bd._BaseDeDados__dados) # Acessar a variável de Instância
bd.lista_clientes()
# bd.dados = 'Uma outra coisa' Quebra o código... acesso direto
# bd.apaga_cliente(2)
# bd.lista_clientes()