# Faça um programa que receba via teclado o valor de um produto e o valor de desconto.
# Retorne o valor final a ser pago
valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto: "))

resultado = valor - (valor * (desconto/100))
print(resultado)