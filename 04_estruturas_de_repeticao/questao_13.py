# Faça um programa que recebe uma string e exiba a string invertida.

texto = input('Digite um texto: ')
texto_invertido = ''

for letra in texto:
    texto_invertido = letra + texto_invertido

print(texto_invertido)
