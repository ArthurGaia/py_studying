# Modulos padrão do Python
# Módulos são arquivos .py (que contém código python) 
# e servem para expandir as funcionalidades padrão 
# da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

# import sys - Importa módulo inteiro
# print(sys.platform)

from sys import platform
print(platform)

import random
# from random import randint as randint_original
# from random import * Importa tudo, não mte recomendado......
for i in range(10):
    print(random.randint(0,10))
    # print(randint(0,10))
