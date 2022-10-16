escolha = int(input("Escolha uma das opções de exercício do 1 ao 3: "))
if escolha == 1:
    #1
    try:
        num_1 = int(input('Digite um numero: '))
        if num_1 % 2 == 0:
            print("É par!")
        else:
            print("É impar!")
    except:
        print("O numero informado não é inteiro")

elif escolha == 2:
    #2
    try:
        num_2 = int(input("Digite o horário: "))

        if num_2 >=0 and num_2 <= 23:
            if num_2 <= 11:
                print("Bom dia!")
            elif num_2 >= 12 and num_2 <= 17:
                print("Boa tarde!")
            else:
                print("Boa noite!")
        else:
            print("Digite um horário entre 0 e 23 horas.")
    except:
        print("O Horario precisa ser inteiro!")
else:
    #3
    nome = input("Digite seu nome: ")
    if len(nome) <= 4:
        print("Seu nome é curto!")
    elif len(nome) in (5, 6):
        print("Seu nome é normal!")
    else:
        print("Seu nome é muito grande!")