# add (adiciona), update (atualiza), clear, discard 
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_differene ^ (Elementos que estão nos dois sets, mas não em ambos)

# s1 = {} Cria um DICIONÁRIO, e não um conjunto
s1 = {1,2,3,4,5} # criação do conjunto
print(type(s1))
# print(s1[0]) Não pode ser acessado dessa forma

for v in s1:
    print(v)

s2 = set() # Cria set vazio

# add valores
s2.add(1)
s2.add(2)
s2.add('1')
print(s2)

# exclui valores
s2.discard(2)
print(s2)

# Update - intera sobre cada elemento
s3 = set()
s3.update('Python') # Conjuntos não respeitam ordem
s3.update([1,2,3,4,5], {5,6,7,8,9}) # Não grava elementos duplicados
print(s3)

# Uso comum
l1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,'Arthur','Arthur']
l1 = set(l1)
print(l1) # Removeu duplicados
l1 = list(l1)
print(l1) # Retorna sem repetidos... Pode voltar desorganizado


s4 = {1,2,3,4,5}
s5 = {3,4,5,6,7,8}

# Union 

#s6 = s4 | s5 Pipeline... une da mesma forma
uniao = s4.union(s5)
print(uniao)

# Intersecção - apenas o presente em ambos os conjuntos
interseccao = s4 & s5
print(interseccao)

# Diferença - Diferença de elementos entre os conjuntos
# A ordem importa. Ele pegará os elementos da esquerda e subtrair o da direita
diferenca = s4 - s5
print(diferenca)

# Diferança simétrica - retira valores repetidos e traz valores que não existem no outro set comparado
dif_simetrica = s4 ^ s5
print(dif_simetrica)

#
l2 = ['Arthur', 'Joao', 'Maria']
l3 = ['Arthur', 'Joao', 'Maria', 'Joao', 'Maria', 'Arthur', 'Joao', 'Maria']
print(l2 == l3)
# Sem comprometer a lista original
print(set(l2) == set(l3))

l2 = set(l2)
l3 = set(l3)
print(l2 == l3)