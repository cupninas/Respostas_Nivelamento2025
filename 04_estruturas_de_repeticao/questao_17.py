#Questão 17
#FAÇA UM PROGRAMA QUE GERE OS PRIMEIROS N NÚMEROS TRIANGULARES(SEQUÊNCIA ONDE CADA TERMO É A SOMA DOS NATURAIS). EXEMPLO:1 , 3 , 6, 10, 15 # (1 , 1+2 , 1+2+3, …)
numero = int(input("Insira a quantidade de números que deseja: "))
soma = 0
for i in range (1,numero+1):
    soma += i
    print(soma)
