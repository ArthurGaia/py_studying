"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
import itertools

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
# combinations(Lista, numero de valores do conjunto)
for grupo in itertools.combinations(pessoas, 2):
    print(grupo)
# A ordem não importa, poque ('Luiz', 'André') = ('André', 'Luiz')

for grupo in itertools.permutations(pessoas, 2):
    print(grupo)

for grupo in itertools.product(pessoas, repeat=2):
    print(grupo)