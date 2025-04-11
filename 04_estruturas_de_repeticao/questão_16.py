#Questão 16
#FAÇA UMA CALCULADORA BÁSICA (SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO,DIVISÃO) QUE O USUÁRIO POSSA PARAR ELA A QUALQUER MOMENTO.

print("Bem vindo a calculadora, escolha uma opção \n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Sair")
escolha = int(input("Insira uma opção de (0 a 4): "))
continuar = True
while (continuar):
    numero_1 = int(input("Insira o primeiro número: "))
    numero_2 = int(input("Insira o segundo número: "))
    if numero_2 == 0:
        print("valor inserido para o numero 2 é invalido")
    else:
        soma = numero_1 + numero_2
        subtracao = numero_1 - numero_2
        divisao = numero_1 / numero_2
        multiplicacao = numero_1 * numero_2
        if (escolha == 1):
            print(f"O valor da soma é: {soma}")
        elif (escolha == 2):
            print(f"O valor da subtração é: {subtracao}")
        elif (escolha == 3):
            print(f"O valor da multiplicação é: {multiplicacao}")
        elif(escolha == 4):
            print(f"O valor da divisão é: {divisao}")
        else:
            print("o valor inserido é invalido")
        escolha2 = int(input("Deseja continuar? 1-sim 0-encerrar"))
        if escolha2 == 0:
            continuar = False
        if escolha2 != 1 or 0:
            print("Escolha inválida")
    print("Bem vindo a calculadora, escolha uma opção \n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n0-Sair")
    escolha = int(input("Insira uma opção de (0 a 4): "))