#Questão 18
#CALCULE A SOMA DA SÉRIE HARMÔNICA (1 + ½ + ⅓ + … + 1/N) ATÉ QUE O TERMO 1/N SEJA MENOR QUE 0.001
soma = 0
n = 1
while (1/n >0.001):
    if 1/n > 0.001:
        soma += 1/n
        n += 1
    print(soma)
