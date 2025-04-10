# Faça um programa que receba um número e exiba a soma dos dígitos desse número.

numero = input('Digite um número: ')
soma = 0

for digito in numero:
    soma += int(digito)

print(soma)
