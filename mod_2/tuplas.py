# tuple1 = (1,2,3, 'a', 'lindao')
tuple1 = 1,2,3, 'a', 'lindao' # Pode ser declarado sem parênteses
# tuple1 = 1 Gera um inteiro, portanto deve ser
#           tuple1 = 1,

print(tuple1)
print(type(tuple1)) 

for valor in tuple1:
    print(valor)

print(tuple1[2:])

# tem comportamento similar a uma lista, só não são
# aletráveis

# Pode também ser concatenada
t1 = 1,2,3,4,5
t2 = 6,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_, n10 = t3
print(n10)

# transformar em lista
l1 = list(t1)
t1[1] = 10

# Tornar tupla novamente
t1 = tuple(t1)