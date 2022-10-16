from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    # self se refere a instância, ou seja, ao objeto instanciado
    
    # Construtor padrão, vem com o self 

    # def __init__(self) -> None:
    #     pass

    def __init__(self, nome, idade, comendo=False, falando=False): # construtor
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando
    
    @classmethod # Define que o método pertence a classe, e não a instância
    # Nesse caso, a instância não pode chamar o método.
    # tem o mesmo funcionamento de uma vareável global
    # Por convenção, se muda de selfie(instância) para cls(classe)
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) # Cls modifica a CLASSE
    # p1 = Pessoa.por_ano_nascimento('Arthur', 2001)

    @staticmethod # não precisa nem da instância e nem a classe >O<
    def gera_id(): # Não recebe informações nem da Instância (selfie) e nem da classe (cls)
        rand = randint(10000,19999)# Métodos estáticos estão aqui apenas por uma questão de organização
        return rand
    # Pessoa.gera_id()
    # p1.gera_id() Também funciona, mas não modifica nada na classe, só executa o método

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade