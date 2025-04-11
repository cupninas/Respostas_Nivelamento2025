#Questão 19
#PEÇA UM NÚMERO N AO USUÁRIO, CALCULE E EXIBA OS PRIMEIROS N TERMOS DA SEQUÊNCIA DE FIBONACCI.
Objetivo = int(input("Insira quantos termos devem ser calculados: "))
numero1 = 0
numero2 = 1
print(numero1)
print(numero2)
for i in range (1,Objetivo):
    proximo = numero1 + numero2
    print(proximo)
    numero1 = numero2
    numero2 = proximo