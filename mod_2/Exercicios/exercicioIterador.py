carrinho = []

carrinho.append(('Produto 1', 30.5))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

# Resolvido usando list comprehension
total = sum([float(y) for x, y in carrinho])
print(total)

# Forma errada - 1
total_errado1 = 0
for x in carrinho:
    total_errado1 += float(x[1])

print(total_errado1)

# Forma errada - 2
total_errado2 = []
for x in carrinho:
    total_errado2.append(float(x[1]))

print(sum(total_errado2))