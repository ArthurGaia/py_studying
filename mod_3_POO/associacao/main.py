from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina)

# Associação - forma mais fraca
escritor.ferramenta = maquina # caneta
escritor.ferramenta.escrever()