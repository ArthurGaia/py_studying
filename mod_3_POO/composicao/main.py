from http import client
from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de janeiro', 'RJ')

cliente3 = Cliente('Joao', 19)
cliente3.insere_endereco('São Paulo', 'SP')