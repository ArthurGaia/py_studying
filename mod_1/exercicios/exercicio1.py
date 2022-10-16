nome = 'Arthur'
idade = 21
altura = 1.8
peso = 77.02
ano = 2022
ano_nasc = 2022 - idade
imc = peso/altura**2

print('{} tem {} anos, {:.2f} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {0} é {1:.2f}.'.format(nome, imc))
print('{n} nasceu em {a}.'.format(n=nome,a=ano_nasc))