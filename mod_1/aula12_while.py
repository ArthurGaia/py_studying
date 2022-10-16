# Continua pulando apenas uma volta do loop
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

# Termina a execução - break
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break
    
    print(x)
    x = x + 1

# While com else

contador = 1
acumulador = 1

while contador <=10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else!')

# While com else sem executar

contador = 1
acumulador = 1

while contador <=10:
    print(contador, acumulador)

    if contador > 5:
        break       #devido ao break, não executa o restante dos loops nesse caso

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else!')

# iterando com Strings
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    print(nova_string, frase[contador])
    nova_string += frase[contador]
    contador += 1

"""
# Exemplo 2
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    if contador > 0 and not nova_string[contador-1] == ' ':
        print(nova_string)#, frase[contador])
    
    if frase[contador-1] == ' ':
        nova_string += frase[contador].upper()
    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)