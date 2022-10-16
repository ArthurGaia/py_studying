import calculo
# import vendas.calc_preco
# from vendas import calc_preco
from vendas.calc_preco import aumento, reducao
# from vendas.formata import preco o preco foi sobescrito no código
import vendas.formata.preco as formata

# print(__name__)

preco = 49.90
# preco_com_aumento = vendas.calc_preco.aumento(preco, 15)
# preco_com_aumento = calc_preco.aumento(preco, 15)
# preco_com_aumento = aumento(preco, 15) formata false
preco_com_aumento = aumento(preco, 15, formata=True)
print(preco_com_aumento)

# preco_com_reducao = reducao(preco, 15) formata false
preco_com_reducao = reducao(preco, 15, formata=True)
print(preco_com_reducao)