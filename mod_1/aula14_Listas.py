"""
Lstas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max
range
"""
#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#        -5   -4   -3   -2   -1   -5

lista[5] = 'Qualquer outra coisa' # sobrepondo valores

print('Valor do indice [1]: ', lista[1])
print('Valor do indice [0] ao [2]: ', lista[0:3]) # Exibe os valores do 0 ao 2, excluindo o 3, nesse caso
print('Valor do indice [2] em diante: ', lista[2:]) # Exibe do dois até o ultimo
print('Valor da lista ao contrário: ', lista[-1]) # Exibe o ultimo valor
print('Lista com passo 2: ', lista[::2]) # Pula de dois em dois, define o passo. De trás pra frente [::-1]
print('Lista completa: ', lista) # Indice inteiro

# Funções de listas
l1 = [1,2,3] 
l2 = [4,5,6]
l3 = l1 + l2 # concatena os VALORES das duas listas

print('Lista concatenada: ', l3)

# Extend - Concatena valor com a lista dentro do ()
l4 = [1,2,3]
l4.extend(l2)

print('Lista com extend: ', l4)

# Append - Adiciona valor
l4.append('Val7')
print('Valor adicionado com append: ', l4)

# Insert - Insere o valor em determinado lugar
l4.insert(0, 0) # (posição, valor)
print('Valor adicionado com insert: ', l4)

# Pop - Exclui valor
l4.pop() # Deleta ultimo valor da lista
l4.pop(0) # Deleta primeiro valor
print('Valor removido com pop: ', l4)

# Del - Deletar
l5 = l4 + l3 # Retorno - [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
del(l5[6:]) # Deleta do Índice 6 em diante [início:fim] ou [indice Unico]
print(l5)

# Min - Max - Mínimo Máximo 
print(max(l4))
print(min(l4))

# Função list e range
l6 = list(range(0, 10)) # declara uma lista de 0 a 9
l7 = list(range(0,100,8)) # Lista 0 a 100 multiplos de 8
print(l6)
print(l7)