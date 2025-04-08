# Crie um programa que recebe dois valores e depois troca os valores entre eles. 

valor1 = int(input('informe um valor:'))
valor2 = int(input('informe outro valor:'))

auxiliar = valor2
valor2 = valor1
valor1 = auxiliar

print(f'A = {valor1}\nB = {valor2}')
