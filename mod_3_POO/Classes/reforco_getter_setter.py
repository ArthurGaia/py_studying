# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
class Pessoa:
    def __init__(self, nome):
        # self.nome = nome # Executa o setter
        self._nome = nome # inicializa a variável

    @property
    def nome(self):
        return self._nome
        # return self.nome Cria algo recursivo, executado infinitamente, pois ela está se chamando

    @nome.setter
    def nome(self, nome):
        # nome += 'Sei la'
        self._nome = nome
        #  return self.nome = nome Cria algo recursivo, executado infinitamente, pois ela está se chamando

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'


p1 = Pessoa('Otávio')
print(p1.nome)
print(p1.sobrenome)