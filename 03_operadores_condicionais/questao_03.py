# Peça um número ao usuário, verifique e exiba se o número é positivo, negativo ou zero

numero = int(input('informe um número:'))

if numero > 0: 
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo')
elif numero == 0: 
    print('O número é 0.')
