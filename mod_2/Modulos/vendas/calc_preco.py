from vendas.formata import preco

def aumento(valor, porcentagem, formata=False):# Definido valor padrão, pois se não for definido, não vai formatar por padrão
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return preco.real(r)
    else:
        return round(r, 2)

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return preco.real(r)
    else:
        return round(r, 2)