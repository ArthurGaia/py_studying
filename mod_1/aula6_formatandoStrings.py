nome = 'Arthur'
idade = 21
altura = 1.8
e_maior = idade > 18
peso = 77
imc = peso/altura**2

print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)

#string formatada

stringFormatada = f'{nome} tem {idade} de idade e seu imc é: {imc:.2f}'
print(stringFormatada)

#format
stringFormat_1 = '{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc)
print(stringFormat_1)

# no format, as variáveis são listadas, portanto pode
# ser organizado por atribuir valores as chaves (Valores
# de listagem)
stringFormat_2 = '{1} tem {2:.2f} anos de idade e seu imc é: {0}'.format(nome, idade, imc)
print(stringFormat_2)

# atribuir parâmetros nomeados
stringFormat_3 = '{n} tem {o} anos de idade e seu imc é: {p:.2f}'.format(n=nome, o=idade, p=imc)
print(stringFormat_3)