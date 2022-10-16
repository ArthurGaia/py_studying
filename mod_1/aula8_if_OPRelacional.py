
a = (int(input("digite um valor: ")))


if a>=2:
    print("Verdadeiro")

    """
    Bloco if... após os dois pontos, seguir identação

    """
else:
    print("falso")


#Seguindo identação
if False:
    print("True")
    print("True")
    print("True")
print("Falso") # se torna o else pela identação

# Elif
# elif pode haver mais de uma opção em um mesmo if.. 
# Pode ter mais de um elif por bloco

if a==2:
    print("igual a dois")
elif a<2:
    print("Menor que dois")
else:
    print("Maior que dois")

#executa apenas uma opção

if False:
    print("1")
elif True:
    print("2") # executa o primeiro True
elif True:
    print("3")
else:
    print("4")

# Operadoes relacionais

#atribuição de bool

num_1 = 2
num_2 = 2

true = num_1 == num_2 # True
print(true)

true = num_1 > num_2 # False
print(true)

true = num_1 <= num_2 # True
print(true)

true = num_1 != num_2 # False
print(true)

# Operadores lógicos

#and or not

b = 0

if not b:
    print("Olá mundo")

nome = "Arthur"
if 'u' in nome:
    print("Existe a letra u em nome.")

if 'j' not in nome:
    print("Não existe j em nome")

j = (1, 2, 3, 4, 5)

if 1 in j:
    print("tem 1")