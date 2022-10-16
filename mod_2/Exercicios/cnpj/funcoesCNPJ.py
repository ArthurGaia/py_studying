import re


def remover_pontos(cnpj):
    return list(re.sub(r'[^0-9]', '', cnpj))

def adiciona_pontos(cnpj):
    string = ''
    for i in range(18):
        if i < 2:
            string = string + str(cnpj[i])
        elif i == 2:
            string = string + '.'
        elif i > 2 and i < 6:
            string = string + str(cnpj[i-1])
        elif i == 6:
            string = string + '.'
        elif i > 6 and i < 10:
            string = string + str(cnpj[i-2])
        elif i == 10:
            string = string + '/'
        elif i > 10 and i < 15:
            string = string + str(cnpj[i-3])
        elif i == 15:
            string = string + '-'
        else:
            string = string + str(cnpj[i-4])
    return string

def comparaCNPJ(cnpj, cnpj_validado):
    cnpj_string = adiciona_pontos(cnpj)
    cnpj_string2 = adiciona_pontos(cnpj_validado)

    return (cnpj_string == cnpj_string2), cnpj_string

def somaNumeros(numero):
    numero = 11 - (numero % 11)
    if numero > 9:
        return 0
    return numero


def encontraNumeros(cnpj):
    cnpj_copia = [x for x in cnpj]
    primeiro_numero = encontraPrimeiroNumero(cnpj_copia)

    cnpj.append(primeiro_numero)
    cnpj_copia = [x for x in cnpj]
    segundo_numero = encontraSegundoNumero(cnpj_copia)

    cnpj.append(segundo_numero)
    return cnpj


def encontraPrimeiroNumero(cnpj):
    contador = 5
    primeiro_numero = 0

    for i in range(12):
        cnpj[i] = cnpj[i] * contador
        primeiro_numero = primeiro_numero + cnpj[i]
        contador -= 1

        if contador == 1:
            contador = 9
    return somaNumeros(primeiro_numero)


def encontraSegundoNumero(cnpj):
    contador = 6
    segundo_numero = 0

    for i in range(13):
        cnpj[i] = cnpj[i] * contador
        segundo_numero = segundo_numero + cnpj[i]
        contador -= 1

        if contador == 1:
            contador = 9
    return somaNumeros(segundo_numero)


if __name__ == '__main__':
    cnpj = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1]
    cnpj = encontraNumeros(cnpj)
    string = adiciona_pontos(cnpj)
    print(cnpj)
    print(string)
