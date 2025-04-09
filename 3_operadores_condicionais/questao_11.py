# Faça um programa que calcule o IMC de uma pessoa e classifique se é
# abaixo do peso (IMC menor que 18.5),
# normal (IMC entre 18.5 e 25),
# sobrepeso (IMC entre 25 e 30) ou
# obesidade (IMC maior que 30).

altura = float(input('Digite a altura em metros: '))
peso = float(input('Digite o peso em quilogramas: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Normal.')
elif imc < 30:
    print('Sobrepeso.')
else:
    print('Obesidade.')
