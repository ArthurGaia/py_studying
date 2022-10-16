from pessoa import Pessoa

p1 = Pessoa('Luiz', 29) # O restante já tem valor padrão
p2 = Pessoa('João', 32)

p3 = Pessoa('Arthur', 21, True, True)
p4 = Pessoa.por_ano_nascimento('Arthur', 2001) # inicializa usando o método de classe (método que modifica a classe)

p3.falar('arroz')
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
