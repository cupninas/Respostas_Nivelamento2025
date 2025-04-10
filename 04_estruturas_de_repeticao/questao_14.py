# Faça um programa que recebe uma string e verifique se ela é um palíndromo.

texto = input('Digite um texto: ')
texto_invertido = ''

for letra in texto:
    texto_invertido = letra + texto_invertido

if texto == texto_invertido:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')
