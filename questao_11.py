# Faça um programa que peça uma temperatura em Fahrenheit ao usuário, converta para graus Celsius e exiba o resultado.
#FAÇA UM PROGRAMA QUE PEÇA UMA TEMPERATURA EM FAHRENHEIT AO USUÁRIO, CONVERTA PARA GRAUS CELSIUS E EXIBA O RESULTADO.
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8

print(f'{fahrenheit}°F = {celsius}°C')
