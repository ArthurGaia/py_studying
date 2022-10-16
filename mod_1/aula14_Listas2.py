"""Jogo da Advinhação"""
import random

lista_sortida = ['Agnostico', 'Alvissaras', 'Balaustre', 'Balaustre', 'Cornucopia', 'Cuntatorio', 'Deleterio', 'Desasnado', 'Empedernido', 'Filantropo', 'Filaucioso', 'Gracolar', 'Hebdomadario', 'Horripilo', 'Iconoclasta', 'Idiossincrasia', 'Inocuo', 'Jocoso', 'Juvenilizante', 'Kafkaesco', 'Lancinante', 'Loquaz', 'Mendacioso', 'Modorrento', 'Nitidificar', 'Numismatica', 'Odiento', 'Osculo', 'Prognostico', 'Putrefato', 'Quimera', 'Quintessencia', 'Recondito', 'Rufiao', 'Sectario', 'Sumidade', 'Taciturno', 'Tergiversar', 'Ufanismo', 'Urdidura', 'Verossimilhanca', 'Vicissitude', 'Vituperio', 'Warrantagem', 'Xaropear', 'Xifopago', 'Yanomami', 'Zaragatoa', 'Zeugma', 'Zoomorfico']
lista_definicao = ['Aquele que não acredita em Deus e nem nega a sua existência.', 'Expressão de alegria por notícia recebida.', 'Pequena coluna ornamentada utilizada em cercas.', 'Consentimento ou aprovação.', 'Abundância, vaso em forma de chifre cheio de flores e frutos que representa a fartura.', 'Em que há demora.', 'Degradante, insalubre, prejudicial.', 'Que recebeu instrução, que desasnou.', 'Aquele que não se deixa persuadir ou não se comove.','Altruísta, benevolente.', 'Presunçoso.', 'Dizer graçolas ou brincadeiras.', 'Semanal.', 'Horripilante.', 'Aquele que contesta a veneração de símbolos religiosos.','Caraterística particular do temperamento de uma pessoa ou grupo.',
'Inofensivo.', 'Alegre, cômico.', 'Que rejuvenesce.', 'Que se assemelha às propostas de Kafka.', 'Pungente, agudo.','Eloquente, aquele que fala muito.', 'Aquele que mente.', 'Lento, apático, entediante.', 'Tornar nítido.', 'Estudo ou coleção de moedas e cédulas antigas.', 'Que guarda ódio.','Beijo, com o sentido de cumprimento ou conciliação.', 'Que indica previsão.', 'Em estado de apodrecimento.', 'Sonho que não é possível realizar.', 'Auge, máximo, primor.', 'Oculto.','Brigão, encrenqueiro, valentão, quem pratica bullying.', 'Intolerante, intransigente, extremista, fanático.', 'Aquele que se destaca pela erudição.', 'Sombrio, obscuro.', 'Fazer rodeios.', 'Aquele que se orgulha de algo de forma exagerada.',
'Trama, enredo, intriga.', 'Discurso que parece ser verdadeiro, coerente, plausível.', 'Sucessão de mudanças.', 'Comportamento ofensivo.', 'Garantia pelo título de crédito conhecido como warrant.', 'Aborrecer.','Gêmeo unido ao irmão por alguma parte do corpo, gêmeo siamês.', 'Denominação de povo indígena que habita o Brasil e a Venezuela.', 'Pequena haste com uma ponta absorvente utilizada para aplicação de medicamento ou coleta de material orgânico.', 'Figura de linguagem que consiste na omissão de um termo dito anteriormente.', 'Que apresenta forma de animal.']

x = random.randint(0, 50) # o ultimo valor não é incluído

secreto = lista_sortida[x].lower()
digitados = []

print(f'A palavra contém {len(secreto)} letras')
print(f'A definição dessa palavra é: {lista_definicao[x]}')

while True:
    letra = input('\nDigite uma letra: ')
    print("")

    if len(letra) > 1:
        print('Ahh, isso não vale, digite apenas uma letra.')
        continue # Encerra esse loop

    digitados.append(letra) # Adiciona o valor digitado a lista

    if letra in secreto:
        print(f'Uhullll, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Afff, a letra "{letra}" Não Existe na palavra secreta.')
        digitados.pop() # Deleta o valor inserido. Mantido apenas para treinamento

    secreto_temporario = ''
    for letra_secreta in secreto: # letra_secreta(contador) vai puxar letra a letra de secreto (palavra original).
        if letra_secreta in digitados: # se a letra digitada estiver na palavra secreta... Vai verificar letra a letra
            secreto_temporario += letra_secreta # Coloca a letra se correta na letra_secreta
        else:
            secreto_temporario += '*' # preenche o restante das letras 'não digitadas' NESSE LOOP
    if secreto_temporario == secreto:
        print(f'\nVocê ganhou, a palavra era "{secreto_temporario}"')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

# Desacomplamento

lista = ['a', 'b', 'c']
n1, n2, n3 = lista
print(n1, n2, n3)

# Erro - too many values to unpack (expected 2)
e1, e2 = lista

# Forma correta
e1, e2, *_ = lista # *_ é a forma correta, pois mostra ao restante dos prog que só interessa os outros valores. '_' continua sendo uma variávrl
# ou até e1, e2, *e3 = lista, sendo que e3 fica com o restante

# Pode desempacotar também dessa forma
listas = [1,2,3,4,5]
print(*listas)